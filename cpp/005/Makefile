file = 001.cpp

program: $(file) ../all.h ../all.h.gch
	g++ -std=c++17 -Wall --pedantic-errors -include ../all.h -o $@ $<

../all.h.gch: ../all.h
	g++ -std=c++17 -Wall --pedantic-errors -x c++-header -o $@ $<

run: program
	./program

clean:
	rm -f ./program

cleanH:
	rm -f ../all.h.gch

.PHONY: run clean cleanH