a.out: main.o lex.yy.o Project.tab.o
	gcc main.o lex.yy.o Project.tab.o -ll
	
main.o: main.c Project.tab.c
	gcc -c main.c

lex.yy.o: lex.yy.c
	gcc -c lex.yy.c
	
Project.tab.o: Project.tab.c
	gcc -c Project.tab.c
	
lex.yy.c: Project.l Project.tab.c
	flex Project.l
	
Project.tab.c: Project.y
	bison -d Project.y

clean:
	rm -f a.out main.o lex.yy.i lex.yy.c Project.tab.o Project.tab.c Project.tab.h

run: a.out
	./a.out
