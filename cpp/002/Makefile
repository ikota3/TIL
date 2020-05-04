file = 001.cpp

gcc_options = -std=c++17 -Wall --pedantic-errors

program: $(file) ../all.h all.h.gch
	g++ $(gcc_options) -include ../all.h -o $@ $<

all.h.gch: ../all.h
	g++ $(gcc_options) -x c++-header -o $@ $<

run: program
	./program

clean:
	rm -f ./program

cleanH:
	rm -f ./all.h.gch

.PHONY: run clean cleanH

