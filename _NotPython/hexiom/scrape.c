#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "scrape.h"
#include "ui.h"

#define R(x, y) (p[(h - (y) - 1) * w + (x)] & 0xffffff)
#define W(x, y) (p[(h - (y) - 1) * w + (x)])

static void
put16(FILE * f, u_int16_t d)
{
	fwrite(&d, 1, 2, f);
}

static void
put32(FILE *f, u_int32_t d)
{
	fwrite(&d, 1, 4, f);
}

static void
screenshot(unsigned *p, unsigned w, unsigned h)
{
	FILE *f;
	char magic[2] = { 'B', 'M' };
	unsigned rw, rh;
	int rx, ry, x, y;

	f = fopen("screenshot.bmp", "w");
	rw = w; rh = h;
	fwrite(magic, 1, 2, f);
	put32(f, 14 + 12 + rw * rh);	/* file size */
	put16(f, 0);			/* reserved */
	put16(f, 0);			/* reserved */
	put32(f, 14 + 12);		/* offset */

	put32(f, 12);				/* header */
	put16(f, w);			
	put16(f, h);			
	put16(f, 1);				/* color planes */
	put16(f, 24);				/* bits per pixel */

	for (ry = rh - 1; ry >= 0; --ry) {
		for (rx = 0; rx < rw; ++rx) {
			unsigned q = R(rx, ry);
			unsigned char d[3] = { q & 255, (q >> 8) & 255,
			    (q >> 16) & 255 };
			fwrite(d, 1, 3, f);
		}
	}
	fclose(f);
}

static int
diff(unsigned a, unsigned b)
{
	int r = 0;
	r += abs((int)(a & 255) - (int)(b & 255));
	r += abs((int)((a >> 8) & 255) - (int)((b >> 8) & 255));
	r += abs((int)((a >> 16) & 255) - (int)((b >> 16) & 255));
	return r;
}

static int
score(const char *a, const char *b)
{
	int i, sum = 0;
	for (i = 0; i < 9 * 16; ++i)
		if (a[i] == b[i])
			sum++;
	return sum;
}

static int
digit(unsigned *p, int w, int h, int x, int y, int bw, int bh)
{
	char *d;
	int a, b;
	int i, j, k = 0, max = -999999;

	d = (char *)malloc(bw * bh + 1);
	memset(d, ' ', bw * bh);
	d[bw * bh] = 0;
	for (b = 0; b < bh; ++b) {
		for (a = 0; a < bw; ++a) {
			unsigned c = R(x + a, y + b);
			unsigned g = (c & 255) + ((c >> 8) & 255) +
			    ((c >> 16) & 255);
			d[b * bw + a] = g >= 763 ? '*' : ' ';
		}
	}
	for (i = 0; font[i].s; ++i) {
		if (font[i].bw != bw || font[i].bh != bh)
			continue;
		int j, sum = 0;
		for (j = 0; j < bw * bh; ++j)
			if (d[j] == font[i].s[j])
				sum++;
			else
				sum--;
		if (sum > max) {
			k = font[i].n;
			max = sum;
		}
	}
	if (max < bw * bh * 9 / 10) {
		printf("max %d, k %d\n", max, k);
		for (b = 0; b < bh; ++b) {
			for (a = 0; a < bw; ++a)
				printf("%c", d[b * bw + a]);
			printf("\n");
		}
		printf("enter number: ");
		fflush(stdout);
		fscanf(stdin, "%d", &k);
		add_font(bw, bh, k, d);
	}
	free(d);
	return k;
}

static int
grey(unsigned c)
{
	int r = c & 255, g = (c >> 8) & 255, b = (c >> 16) & 255;
	int s = 0;

	s += abs(r - g);
	s += abs(r - b);
	s += abs(g - b);
	return s <= 32;
}

static int
tile(unsigned *p, int w, int h, int x, int y, int bw, int bh)
{
	unsigned c = 0xff0000;
	int r;
	int a, b;

	if (R(x + 4, y + 8) == 0x666666) {
		c = 0x000000;
		r = 7;
	} else if (R(x + 4, y + 8) == 0x6c6c6c) {
		c = 0x00f0ff;
		r = 17;
	} else {
		r = digit(p, w, h, x, y, bw, bh);
		if (grey(R(x - bw/2, y - bh/3))) {
			r += 10;
			c = 0x0000ff;
		}
	}
	for (a = 0; a < bw; ++a) {
		for (b = 0; b < bh; ++b) {
			unsigned f = R(x + a, y + b);
			unsigned g = (f & 255) + ((f >> 8) & 255) +
			    ((f >> 16) & 255);
			W(x + a, y + b) = g >= 763 ? 0xffffff : c;
		}
	}
	return r;
}

void
scan(char *a, unsigned *c)
{
	unsigned *p;
	int w, h;
	int n = 6, m = 2 * n - 1;
	int fx = -1, fy = -1;
	int gx = -1, gy = -1;
	int px, py;
	int x = 0, y = 0, u = 0, v = 0;
	int i;

	if (screen(&p, &w, &h))
		return;
	for (py = 0; py < h - 2; ++py) {
		for (px = 0; px < w - 2; ++px) {
			if (diff(R(px    , py    ), 0x25020B) <= 3 &&
			    diff(R(px + 2, py    ), 0x25020B) <= 3 &&
			    diff(R(px    , py + 2), 0x25020B) <= 3 &&
			    diff(R(px + 2, py + 2), 0x7F7F7F) <= 3) {
				fx = px + 2;
				fy = py + 2;
				W(fx, fy) = 0xFFFF00;
				py = h;
				break;
			}
		}
	}
	for (py = h - 1; py > 1; --py) {
		for (px = w - 1; px > 1; --px) {
			if (diff(R(px    , py    ), 0x25020B) <= 3 &&
			    diff(R(px - 2, py    ), 0x25020B) <= 3 &&
			    diff(R(px    , py - 2), 0x25020B) <= 3 &&
			    diff(R(px - 2, py - 2), 0x5F5F5F) <= 3) {
				gx = px - 2;
				gy = py - 2;
				W(gx, gy) = 0xFFFF00;
				py = 1;
				break;
			}
		}
	}
	double dx = (double)(gx - fx + 2) / 12.0;
	double dy = (double)(gy - fy + 2) / 12.0;
	for (i = 1; i <= 11; ++i) {
		int x = fx + i * (gx - fx + 2) / 12;
		int y = fy + i * (gy - fy + 2) / 12;
		W(x, y) = 0x0000FF;
	}

	for (i = 0; i < m * m; ++i) {
		if (x + y >= n - 1 && x + y < n + m - 1) { 
			px = fx + 0.85 * dx + x * dx;
			py = fy + 0.55 * dy - abs(m - 1 - x) * dy + 2.0 * y * dy;
			a[y * m + x] = tile(p, w, h, px, py, dx / 3.0, dy);
			c[y * m + x] = ((py + 8) << 16) | (px + 4);
		} else {
			a[y * m + x] = 99;
			c[y * m + x] = 0;
		}
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
	screenshot(p, w, h);
	free(p);
}

void
move(char *a, const char *b, const int n, const unsigned *c)
{
	const int m = 2 * n - 1;
	int i, j;
	char t;

	printf("making moves");
	while (memcmp(a, b, m * m)) {
		for (i = 0; i < m * m; ++i)
			if (a[i] != b[i])
				break;
		if (i == m * m)
			return;
		for (j = i + 1; j < m * m; ++j)
			if (a[j] != b[j] && a[i] == b[j] && a[j] == b[i])
				break;
		if (j == m * m) {
			for (j = i + 1; j < m * m; ++j)
				if (a[j] != b[j] && a[i] == b[j])
					break;
			if (j == m * m)
				return;
		}
		if (a[i] == 7) {
			int k = i;
			i = j;
			j = k;
		}
		t = a[i];
		a[i] = a[j];
		a[j] = t;
		drag(c[i] & 65535, c[i] >> 16, c[j] & 65535, c[j] >> 16);
		printf(".");
		fflush(stdout);
	}
	printf(" done\n");
}
