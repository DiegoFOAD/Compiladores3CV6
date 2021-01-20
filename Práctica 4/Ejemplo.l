%{
  #include<stdio.h>
%}
letras      [a-z]
vocales     [aeiou]
digito      [0-9]
espacios    [ \n\t]
%%
int             {printf("<palabra reservada>\n");}
{letras}+       {printf("<id>\n");}
";"             {printf("<separador>\n");}
[1-9]{digito}*  {printf("<cte>\n");}
"+"|"*"|"="     {printf("<separador>\n");}
%%

yywrap()
{
	return(1);
}