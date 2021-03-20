prefix = /usr/local

all:
	$(CC) -o vtools vtools.c

install:
	gcc -o vtools vtools.c
	echo $(DESTDIR)
	echo $(prefix)
	install vtools $(DESTDIR)$(prefix)/bin
	install vtools.1 $(DESTDIR)$(prefix)/share/man/man1

clean:
	rm -f vtools
