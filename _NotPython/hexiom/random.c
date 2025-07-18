/* $Id$
 *
 * Copyright (c) 2005-2012 Daniel Hartmeier <daniel@benzedrine.cx>
 * All rights reserved.
 *
 * There seems to be no portable thread-safe PRNG
 * George Marsaglia, 25 Feb 2003, sci.math, Re: RNGs
 * http://groups.google.com/group/sci.math/msg/9959175f66dd138f
 *
 */

#include <sys/types.h>
#include <limits.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#include "random.h"

struct CMWC4096_ctx {
	unsigned long Q[4096];
	unsigned long c;
	unsigned long i;
};

struct CMWC4096_ctx *
CMWC4096_init(const unsigned char *seed, unsigned off, unsigned len)
{
	struct CMWC4096_ctx *ctx;
	unsigned i;

	ctx = (struct CMWC4096_ctx *)malloc(sizeof(struct CMWC4096_ctx));
	ctx->c = 362436;
	ctx->i = 4095;
	for (i = 0; i < sizeof(ctx->Q); ++i)
		((unsigned char *)ctx->Q)[i] = seed[(i + off) % len];
	return ctx;
}

unsigned long
CMWC4096_rand(struct CMWC4096_ctx *ctx)
{
	unsigned long long t, a = 18782LL;
	unsigned long x, r = 0xfffffffe;
	ctx->i = (ctx->i + 1) & 4095;
	t = a * ctx->Q[ctx->i] + ctx->c;
	ctx->c = (t >> 32);
	x = t + ctx->c;
	if (x < ctx->c) {
		x++;
		ctx->c++;
	}
	return (ctx->Q[ctx->i] = r - x);
}

unsigned long
CMWC4096_random_uniform(struct CMWC4096_ctx *ctx, unsigned long m)
{
	unsigned long u = CMWC4096_rand(ctx);
	return (double)m * ((double)u / (double)ULONG_MAX);
}
