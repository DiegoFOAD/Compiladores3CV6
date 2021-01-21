/*Instituto Politécnico Nacional*/
/*Escuela Superior de Cómputo*/
/*Compiladores - 3CV6*/
/*Código tomado de: https://www.lysator.liu.se/c/ANSI-C-grammar-l.html */
/*Modificado y entregado por: Diego Armando Flores Alvarado - 2015340065*/

D			[0-9]
L			[a-zA-Z_]
H			[a-fA-F0-9]
E			[Ee][+-]?{D}+
FS			(f|F|l|L)
IS			(u|U|l|L)*

%{
#include <stdio.h>
%}

%%
"/*"			{ printf("<Comentario>\n"); }

"break"			{ printf("<Palabra reservada>\n"); }
"case"			{ printf("<Palabra reservada>\n"); }
"char"			{ printf("<Tipo de dato>\n"); }
"const"			{ printf("<Tipo de dato>\n"); }
"continue"		{ printf("<Palabra reservada>\n"); }
"default"		{ printf("<Palabra reservada>\n"); }
"do"			{ printf("<Ciclo>\n"); }
"double"		{ printf("<Palabra reservada>\n"); }
"else"			{ printf("<Condicional>\n"); }
"enum"			{ printf("<Palabra reservada>\n"); }
"extern"		{ printf("<Palabra reservada>\n"); }
"float"			{ printf("<Tipo de dato>\n"); }
"for"			{ printf("<Ciclo>\n"); }
"goto"			{ printf("<Palabra reservada>\n"); }
"if"			{ printf("<Condicional>\n"); }
"int"			{ printf("<Tipo de dato>\n"); }
"long"			{ printf("<Tipo de dato>\n"); }
"register"		{ printf("<Palabra reservada>\n"); }
"return"		{ printf("<Retorno>\n"); }
"short"			{ printf("<Tipo de dato>\n"); }
"signed"		{ printf("<Palabra reservada>\n"); }
"sizeof"		{ printf("<Palabra reservada>\n"); }
"static"		{ printf("<Palabra reservada>\n"); }
"struct"		{ printf("<Palabra reservada>\n"); }
"switch"		{ printf("<Palabra reservada>\n"); }
"typedef"		{ printf("<Palabra reservada>\n"); }
"union"			{ printf("<Palabra reservada>\n"); }
"unsigned"		{ printf("<Palabra reservada>\n"); }
"void"			{ printf("<Vacio>\n"); }
"volatile"		{ printf("<Palabra reservada>\n"); }
"while"			{ printf("<Ciclo>\n"); }

{L}({L}|{D})*		{ printf("<Identificador>\n"); }

0[xX]{H}+{IS}?		{ printf("<Literal entera base hexadecimal>\n"); }
0{D}+{IS}?		    { printf("<Literal entera base octal>\n"); }
{D}+{IS}?		    { printf("<Literal entera base decimal>\n"); }
L?'(\\.|[^\\'])+'	{ printf("<Literal caracter>\n"); }

{D}+{E}{FS}?		    { printf("<Literal numerica exponencial>\n"); }
{D}*"."{D}+({E})?{FS}?	{ printf("<Literal numerica real exponencial>\n"); }
{D}+"."{D}*({E})?{FS}?	{ printf("<Literal numerica real exponencial>\n"); }

L?\"(\\.|[^\\"])*\"	{ printf("<Literal cadena>\n"); }

"..."			{ printf("<Delimitador>\n"); }
">>="			{ printf("<Operador compuesto de asignacion\n"); }
"<<="			{ printf("<Operador compuesto de asignacion\n"); }
"+="			{ printf("<Operador compuesto de asignacion\n"); }
"-="			{ printf("<Operador compuesto de asignacion\n"); }
"*="			{ printf("<Operador compuesto de asignacion\n"); }
"/="			{ printf("<Operador compuesto de asignacion\n"); }
"%="			{ printf("<Operador compuesto de asignacion\n"); }
"&="			{ printf("<Operador compuesto de asignacion\n"); }
"^="			{ printf("<Operador compuesto de asignacion\n"); }
"|="			{ printf("<Operador compuesto de asignacion\n"); }
">>"			{ printf("<Operador a nivel de bits>\n"); }
"<<"			{ printf("<Operador a nivel de bits>\n"); }
"++"			{ printf("<Operador aritmetico>\n"); }
"--"			{ printf("<Operador aritmetico>\n"); }
"->"			{ printf("<Operador postfijo\n"); }
"&&"			{ printf("<Operador booleano>\n"); }
"||"			{ printf("<Operador booleano>\n"); }
"<="			{ printf("<Operador de comparacion>\n"); }
">="			{ printf("<Operador de comparacion>\n"); }
"=="			{ printf("<Operador de comparacion>\n"); }
"!="			{ printf("<Operador de comparacion>\n"); }
";"			    { printf("<Delimitador>\n"); }
("{"|"<%")		{ printf("<Delimitador>\n"); }
("}"|"%>")		{ printf("<Delimitador>\n"); }
","			    { printf("<Delimitador>\n"); }
":"			    { printf("<Delimitador>\n"); }
"="			    { printf("<Operador de asignacion>\n"); }
"("			    { printf("<Delimitador>\n"); }
")"			    { printf("<Delimitador>\n"); }
("["|"<:")		{ printf("<Delimitador>\n"); }
("]"|":>")		{ printf("<Delimitador>\n"); }
"."			    { printf("<Delimitador>\n"); }
"&"			    { printf("<Operador a nivel de bits>\n"); }
"!"			    { printf("<Operador booleano>\n"); }
"~"			    { printf("<Operador a nivel de bits>\n"); }
"-"			    { printf("<Operador aritmetico>\n"); }
"+"			    { printf("<Operador aritmetico>\n"); }
"*"			    { printf("<Operador aritmetico>\n"); }
"/"			    { printf("<Operador aritmetico>\n"); }
"%"			    { printf("<Operador aritmetico>\n"); }
"<"			    { printf("<Operador de comparacion>\n"); }
">"			    { printf("<Operador de comparacion>\n"); }
"^"			    { printf("<Operador a nivel de bits>\n"); }
"|"			    { printf("<Operador a nivel de bits>\n"); }
"?"			    { printf("<Operador Condicional>\n"); }

[ \t\v\n\f]		{ printf("<Saltos de linea>\n"); }
.			    { /* ignore bad characters */ }

%%

yywrap()
{
	return(1);
}
