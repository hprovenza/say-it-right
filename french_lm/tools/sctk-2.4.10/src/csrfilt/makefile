# **********************************************************
# Makefile for rfilter1 Directory
# **********************************************************
SHELL = /bin/sh
PREFIX=/Volumes/Seagate/Seagate_Dashboard/kaldi/tools/sctk
bindir = $(PREFIX)/bin
T=../test_suite

all: csrfilt.sh

csrfilt.sh: 
	chmod +x csrfilt.sh

setTests:
	./RunTests.pl setTests

check: all
	@echo "Testing csrfilt.sh"
	./RunTests.pl
	@echo "   csrfilt.sh successfully completed"

install: all
	cp csrfilt.sh $(bindir)

clean:

distclean: clean
	rm -r *~ makefile
