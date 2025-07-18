#include <stdio.h>

#if defined(_WIN32) || defined(_WIN64) || defined (__CYGWIN__)

#include <windows.h>

void drag(int x1, int y1, int x2, int y2)
{
	const int w = GetSystemMetrics(SM_CXSCREEN),
	    h = GetSystemMetrics(SM_CYSCREEN), ms = 60;

	x1 = (65536 * x1) / w + 1;
	y1 = (65536 * y1) / h + 1;
	x2 = (65536 * x2) / w + 1;
	y2 = (65536 * y2) / h + 1;
	mouse_event(MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE, x1, y1, 0, 0);
	Sleep(ms);
	mouse_event(MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_ABSOLUTE, x1, y1, 0, 0);
	Sleep(ms);
	mouse_event(MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE, x2, y2, 0, 0);
	Sleep(ms);
	mouse_event(MOUSEEVENTF_LEFTUP | MOUSEEVENTF_ABSOLUTE, x2, y2, 0, 0);
}

int screen(unsigned **p, int *w, int *h)
{
	int nScreenWidth = GetSystemMetrics(SM_CXSCREEN);
	int nScreenHeight = GetSystemMetrics(SM_CYSCREEN);
	HWND hDesktopWnd = GetDesktopWindow();
	HDC hDesktopDC = GetDC(hDesktopWnd);
	HDC hCaptureDC = CreateCompatibleDC(hDesktopDC);
	HBITMAP hCaptureBitmap = CreateCompatibleBitmap(hDesktopDC,
	    nScreenWidth, nScreenHeight);
	HDC hdc = NULL;
	BITMAPINFO bmpInfo;

	SelectObject(hCaptureDC, hCaptureBitmap); 
	BitBlt(hCaptureDC, 0, 0, nScreenWidth, nScreenHeight, hDesktopDC,
	    0, 0, SRCCOPY); 

	hdc = GetDC(NULL);
	ZeroMemory(&bmpInfo, sizeof(BITMAPINFO));
	bmpInfo.bmiHeader.biSize = sizeof(BITMAPINFOHEADER);
        GetDIBits(hdc, hCaptureBitmap, 0, 0, NULL, &bmpInfo, DIB_RGB_COLORS);
	if (bmpInfo.bmiHeader.biSizeImage <= 0)
		bmpInfo.bmiHeader.biSizeImage = bmpInfo.bmiHeader.biWidth *
		    abs(bmpInfo.bmiHeader.biHeight) *
		    (bmpInfo.bmiHeader.biBitCount + 7) / 8;
        if ((*p = (unsigned *)malloc(bmpInfo.bmiHeader.biSizeImage)) == NULL) {
		return 1;
	}
        bmpInfo.bmiHeader.biCompression = BI_RGB;
        GetDIBits(hdc, hCaptureBitmap, 0, bmpInfo.bmiHeader.biHeight, *p,
	    &bmpInfo, DIB_RGB_COLORS);       
	*h = bmpInfo.bmiHeader.biHeight;
	*w = bmpInfo.bmiHeader.biWidth;
	if (*w % 4)
		*w += 4 - (*w % 4);

	ReleaseDC(NULL, hdc);
	ReleaseDC(hDesktopWnd, hDesktopDC);
	DeleteDC(hCaptureDC);
	DeleteObject(hCaptureBitmap);
	return 0;
}

#elif defined(__APPLE__)

#include <CoreGraphics/CoreGraphics.h>
#include <unistd.h>

void drag(int x1, int y1, int x2, int y2)
{
	static int first = 1;
	int us = 100000;

	if (first) {
		first = 0;
		drag(x1, y1, x1, y1);
	}
	CGEventRef move1 = CGEventCreateMouseEvent(NULL, kCGEventMouseMoved,
	    CGPointMake(x1, y1), kCGMouseButtonLeft);
	CGEventRef down = CGEventCreateMouseEvent(NULL, kCGEventLeftMouseDown,
	    CGPointMake(x1, y1), kCGMouseButtonLeft);
	CGEventRef move2 = CGEventCreateMouseEvent(NULL, kCGEventMouseMoved,
	    CGPointMake(x2, y2), kCGMouseButtonLeft);
	CGEventRef up = CGEventCreateMouseEvent(NULL, kCGEventLeftMouseUp,
	    CGPointMake(x2, y2), kCGMouseButtonLeft);
	CGEventPost(kCGHIDEventTap, move1);
	usleep(us);
	CGEventPost(kCGHIDEventTap, down);
	usleep(us);
	CGEventPost(kCGHIDEventTap, move2);
	usleep(us);
	CGEventPost(kCGHIDEventTap, up);
	CFRelease(up);
	CFRelease(move2);
	CFRelease(down);
	CFRelease(move1);
}

int screen(unsigned **p, int *w, int *h)
{
	CGImageRef image;
	CGDataProviderRef dataProvider;
	CFDataRef copyData;
	unsigned *data;
	int x, y, off;

	image = CGWindowListCreateImage(CGRectInfinite,
	    kCGWindowListOptionOnScreenOnly, kCGNullWindowID, 0);
	if (!image)
		return 1;
	*w = CGImageGetWidth(image);
	*h = CGImageGetHeight(image);

	if ((*p = (unsigned *)malloc(*w * *h * 4)) == NULL)
		return 1;
	if (!(dataProvider = CGImageGetDataProvider(image)))
		return 1;
	if (!(copyData = CGDataProviderCopyData(dataProvider)))
		return 1;

	data = (unsigned *)CFDataGetBytePtr(copyData);
	off = 0;
	for (y = 0; y < *h; ++y) {
		for (x = 0; x < *w; ++x) {
			(*p)[(*h - 1 - y) * *w + x] = data[off] & 0xffffff;
			off++;
		}
	}

	CFRelease(copyData);
	CGImageRelease(image);
	return 0;
}

#else

void drag(int x1, int y1, int x2, int y2)
{
}

int screen(unsigned **p, int *w, int *h)
{
	printf("screen grabbing not yet implemented on this platform\n");
	return 1;
}

#endif

struct {
	int bw, bh, n;
	char *s;
} font[1024];

void load_fonts()
{
	char s[256];
	FILE *f;
	int i, j = 0;

	if (!(f = fopen("fonts", "r")))
		return;
	while (fgets(s, sizeof(s), f)) {
		s[strlen(s) - 1] = 0;
		if (sscanf(s, "%d %d %d",
		    &font[j].bw, &font[j].bh, &font[j].n) != 3) {
			printf("syntax error: %s\n", s);
			break;
		}
		font[j].s = (char *)malloc(font[j].bw * font[j].bh + 1);
		for (i = 0; i < font[j].bh; ++i) {
			fgets(s, sizeof(s), f);
			memcpy(font[j].s + i * font[j].bw, s, font[j].bw);
		}
		j++;
	}
	fclose(f);
	font[j].s = NULL;
	printf("loaded %d font entries\n", j);
}

void add_font(int bw, int bh, int n, const char *s)
{
	FILE *f;
	int i;

	f = fopen("fonts", "a");
	fprintf(f, "%d %d %d\n", bw, bh, n);
	for (i = 0; i < bh; ++i) {
		fwrite(s + i * bw, 1, bw, f);
		fprintf(f, "\n");
	}
	fclose(f);
	for (i = 0; font[i].s; ++i)
		;
	font[i].bw = bw;
	font[i].bh = bh;
	font[i].n = n;
	font[i].s = strdup(s);
	font[++i].s = NULL;
}
