/*
 * hexiom.c : Solving Hexiom using simulated annealing (multi-threaded)
 *
 * Copyright (c) 2012 Daniel Hartmeier <daniel@benzedrine.cx>
 * All rights reserved.
 *
 * Problem description and input files from
 *
 *   http://slowfrog.blogspot.com/2012/01/
 *     solving-hexiom-perhaps-you-can-help.html
 *
 * See also
 *
 *   http://en.wikipedia.org/wiki/Simulated_annealing
 *
 * Building on Windows (using Cygwin, see http://www.cygwin.com/)
 *
 *   gcc -O3 -o hexiom hexiom.c ui.c scrape.c random.c -lgdi32
 *
 * Building on Mac OS X
 *
 *   gcc -O3 -framework Cocoa -o hexiom hexiom.c scrape.c ui.c random.c
 *
 * Building on Unix
 *
 *   gcc -O3 -o hexiom hexiom.c ui.c scrape.c random.c -lm
 *
 * Solving a level read from file, print solution to console
 *
 *   ./hexiom level35.txt
 *
 * Solving a level (size 6) grabbed from an open browser window,
 * generating mouse events to reach the solution
 *
 *   ./hexiom
 *
 */

#include <errno.h>
#include <math.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "random.h"
#include "scrape.h"
#include "ui.h"

const unsigned	 maxcount = 100000;
const unsigned	 maxidle  = 1000;
const double	 cooling  = 0.9999;

static inline int
add(const char *a, const int m, const int x, const int y)
{
	if (x < 0 || y < 0 || x >= m || y >= m)
		return 0;
	return a[y * m + x] % 10 <= 6;
}

static inline int
color(const char *a, const int m, const int x, const int y)
{
	int i = a[y * m + x], j = 0;
	if (i % 10 > 6)
		return 0;
	j += add(a, m, x    , y - 1);
	j += add(a, m, x + 1, y - 1);
	j += add(a, m, x - 1, y    );
	j += add(a, m, x + 1, y    );
	j += add(a, m, x - 1, y + 1);
	j += add(a, m, x    , y + 1);
	return (i % 10) - j;
}

static int
rate(const char *a, const int m)
{
	int sum = 0, y, x;
	for (y = 0; y < m; ++y)
		for (x = 0; x < m; ++x)
			sum += abs(color(a, m, x, y));
	return sum;
}

static void
random_move(struct CMWC4096_ctx *ctx, char *a, const int m)
{
	int x, y;
	char t;

	do
		x = CMWC4096_random_uniform(ctx, m * m);
	while (a[x] > 7);
	do
		y = CMWC4096_random_uniform(ctx, m * m);
	while (x == y || a[y] > 7 || a[y] == a[x]);
	t = a[x];
	a[x] = a[y];
	a[y] = t;
}

static void
read(FILE *f, char *a, const int n)
{
	const int m = 2 * n - 1;
	int x = 0, y = 0, u = 0, v = 0;
	int i;
	for (i = 0; i < m * m; ++i) {
		if (x + y >= n - 1 && x + y < n + m - 1) {
			int locked = 0;
			int c;
			do
				c = fgetc(f);
			while (c == ' ' || c == '\r' || c == '\n');
			if (c == '+') {
				locked = 1;
				c = fgetc(f);
			}
			if (c == '.')
				a[y * m + x] = locked ? 17 : 7;
			else if (c >= '0' && c <= '9')
				a[y * m + x] = c - '0' + (locked ? 10 : 0);
			else {
				fprintf(stderr, "invalid input %d\n", c);
				exit(1);
			}
		} else
			a[y * m + x] = 99;
		if (y > 0 && x < m - 1) {
			x++;
			y--;
		} else {
			if (i < (m * m) / 2) {
				x = 0;
				y = ++u;
			} else {
				x = ++v;
				y = m - 1;
			}
		}
	}
}

static void
print(const char *a, const int n)
{
	const int m = 2 * n - 1;
	int x = 0, y = 0, u = 0, v = 0;
	int i;
	printf("%d", n);
	for (i = 0; i < m * m; ++i) {
		if (x + y >= n - 1 && x + y < n + m - 1) {
			int j = a[y * m + x];
			printf("%c", j >= 10 ? '+' : ' ');
			if (j % 10 == 7)
				printf(".");
			else
				printf("%d", j % 10);
		}
		if (y > 0 && x < m - 1) {
			x++;
			y--;
		} else {
			int off;
			if (i < (m * m) / 2) {
				off = m - 2 - u;
				x = 0;
				y = ++u;
			} else {
				off = v + 1;
				x = ++v;
				y = m - 1;
			}
			if (off < n) {
				printf("\n");
				while (off-- > 0)
					printf(" ");
			}
		}
	}
	printf("\n");
}

static volatile int done = 0;
struct Arg {
	const char *a;
	char *b;
	int n;
	struct CMWC4096_ctx *ctx;
};

static void *
solve_thread(void *varg)
{
	struct Arg *arg = (struct Arg *)varg;
	const char *a = arg->a;
	char *b = arg->b;
	const int n = arg->n;
	const int m = 2 * n - 1;
	struct {
		int	 v;
		char	 s[39691];	/* n <= 100 */
	} input, current, best, next;
	unsigned pass = 0;

	memcpy(input.s, a, m * m);
	input.v = rate(input.s, m);

	while (!done && input.v) {
		unsigned count = 0, idle = 0;
		double temp = 1.0;

		pass++;
		printf(".");
		fflush(stdout);
		best = current = input;
		while (!done && idle < maxidle && count < maxcount) {

			next = current;
			random_move(arg->ctx, next.s, m);
			next.v = rate(next.s, m);

			if (++idle == maxidle / 2)
				current = best;
			count++;
			if (next.v <= current.v) {
				if (next.v < best.v) {
					best = next;
					if (best.v == 0) {
						memcpy(b, best.s, m * m);
						done = 1;
						pthread_exit(0);
						return NULL;
					}
				}
				current = next;
				idle = 0;
			} else {
				double d = (double)current.v /
				    (double)next.v * temp;
				unsigned x = CMWC4096_random_uniform(arg->ctx,
				    1000000), chance = (exp(d * temp) - 1.0) /
				    (M_E - 1.0) * 1000000.0;
				if (x < chance)
					current = next;
			}
			temp *= cooling;
		}
	}
	pthread_exit(0);
	return NULL;
}

static int
solve(const char *a, char *b, const int n)
{
	const int threads = 4;
	pthread_t ids[threads];
	struct Arg arg[threads];
	int i, j;

	printf("solving");
	srand(time(NULL));
	for (i = 0; i < threads; ++i) {
		unsigned char seed[16384];
		for (j = 0; j < sizeof(seed); ++j)
			seed[j] = rand() % 256;
		arg[i].a = a;
		arg[i].b = b;
		arg[i].n = n;
		arg[i].ctx = CMWC4096_init(seed, 0, sizeof(seed));
		int r = pthread_create(&ids[i], NULL, &solve_thread, &arg[i]);
		if (r) {
			perror("pthread_create");
			return 1;
		}
	}
	for (i = 0; i < threads; ++i) {
		if (pthread_join(ids[i], NULL)) {
			perror("pthread_join");
			return 1;
		}
	}
	printf(" %s\n", done ? "success" : "failed");
	return !done;
}

int main(int argc, char *argv[])
{
	FILE *f = NULL;
	int n;
	char a[39601], b[39601];
	unsigned c[121];

	if (argc != 1 && argc != 2) {
		fprintf(stderr, "usage: %s [file]\n", argv[0]);
		return 1;
	}
	if (argc == 2 && !strcmp(argv[1], "-"))
		f = stdin;
	else if (argc == 2 && !(f = fopen(argv[1], "r"))) {
		fprintf(stderr, "fopen: %s: %s\n", argv[1], strerror(errno));
		return 1;
	}
	if (f != NULL) {
		if (fscanf(f, "%d", &n) != 1 || n < 2 || n > 100) {
			fprintf(stderr, "invalid input n %d\n", n);
			return 1;
		}
		read(f, a, n);
		fclose(f);
	} else {
		n = 6;
		load_fonts();
		scan(a, c);
	}

	print(a, n);
	if (solve(a, b, n))
		return 1;
	printf("found solution:\n");
	print(b, n);

	if (f == NULL)
		move(a, b, 6, c);

	return 0;
}
