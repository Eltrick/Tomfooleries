#ifndef __RANDOM_H__
#define __RANDOM_H__

struct CMWC4096_ctx *CMWC4096_init(const unsigned char *seed, unsigned off, unsigned len);
unsigned long CMWC4096_rand(struct CMWC4096_ctx *ctx);
unsigned long CMWC4096_random_uniform(struct CMWC4096_ctx *ctx, unsigned long m);

#endif
