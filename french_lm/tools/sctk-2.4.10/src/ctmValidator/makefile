SHELL = /bin/sh
PREFIX=/Volumes/Seagate/Seagate_Dashboard/kaldi/tools/sctk
bindir = $(PREFIX)/bin

all: ctmValidator.pl

rttmValidator.pl:
	chmod +x ctmValidator.pl

check: all
	(cd test_suite; $(SHELL) RunTest.sh ../ctmValidator.pl)

install: all
	cp ctmValidator.pl $(bindir)

clean:

distclean: clean
	rm -r *~ makefile
