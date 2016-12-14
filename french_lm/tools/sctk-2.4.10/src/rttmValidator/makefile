SHELL = /bin/sh
PREFIX=/Volumes/Seagate/Seagate_Dashboard/kaldi/tools/sctk
bindir = $(PREFIX)/bin

all: rttmValidator.pl

rttmValidator.pl:
	chmod +x rttmValidator.pl

check: all
	(cd test_suite; $(SHELL) RunTest.sh ../rttmValidator.pl)

install: all
	cp rttmValidator.pl $(bindir)

clean:

distclean: clean
	rm -r *~ makefile
