# **********************************************************
# Makefile for slatreport Directory
# **********************************************************
MAKE=make
PREFIX=/Volumes/Seagate/Seagate_Dashboard/kaldi/tools/sctk
bindir=$(PREFIX)/bin

all: slatreport.pl

slatreport.pl: 
	chmod +x slatreport.pl

config:
	@echo -n " Checking gnuplot... "
	@if [ "`which gnuplot | egrep '^/'`" = "" ] ; then \
		echo "not found"; \
	else \
		echo `which gnuplot`; \
	fi

check: all
	@echo "Testing slatreport.pl"
	./slatTest.pl
	@echo "   slatreport.pl tests successfully completed"

install: all
	cp slatreport.pl $(bindir)

clean:

distclean: clean
	rm -r *~ makefile
