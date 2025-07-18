all: hexiom

hexiom: hexiom.c scrape.h scrape.c ui.h ui.c random.h random.c
	gcc -O3 -framework Cocoa -o hexiom hexiom.c scrape.c ui.c random.c

clean:
	rm -f hexiom

