lex.yy.c: P4.l
        flex P4.l

main.o: main.c
        gcc -c main.c

lex.yy.o: lex.yy.c
        gcc -c lex.yy.c

a.out: main.o lex.yy.o
        gcc main.o lex.yy.o -lfl

clean:
        rm -f a.out main.o lex.yy.i lex.yy.c

run: a.out
        ./a.out