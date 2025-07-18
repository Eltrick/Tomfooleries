#ifndef __UI_H__
#define __UI_H__

int	 screen(unsigned **p, int *w, int *h);
void	 drag(int x1, int y1, int x2, int y2);
void	 load_fonts();
void	 add_font(int bw, int bh, int n, const char *s);

extern struct {
	int bw, bh, n;
	char *s;
} font[];

#endif
