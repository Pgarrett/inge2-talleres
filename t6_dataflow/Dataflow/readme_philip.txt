# Ejercicio 1

Comando: `./gradlew soot -PtargetClass=com.example.Foo -Panalysis=jap.rdtagger`

## a
System.out.println(rv);
        virtualinvoke $stack5.<java.io.PrintStream: void println(int)>($stack4);
/*7*/
/*$stack5 has reaching def: $stack5 = <java.lang.System: java.io.PrintStream out>*/
/*$stack4 has reaching def: $stack4 = virtualinvoke $stack3.<com.example.Foo: int bar(int)>(0)*/

Respuesta: Imprimir en pantalla primero debe utilizar la llamada de sistema, que se guarda en la posición stack5 en el stack que tiene como definición la llamada misma a sistema.
Luego, stack4 usa la definición de que stack3 ejecute el método bar con el valor 0 pasado por parámtro. A su vez, stack3 es la instanciación del objeto Foo. Tiene sentido que todas estas
variables vivan en el stack por como Java maneja en memoria la instanciación de nuevos objetos.


## b
        return c;
/*17*/
/*c has reaching def: c = x*/
/*c has reaching def: c = x + 1*/

Respuesta: En este caso, tenemos dos posibles definiciones para c porque son las dos posibles ramas del if, donde se pregunta si el parámetro x es igual a 0 o no.



# Ejercicio 2

Comando `./gradlew soot -PtargetClass=com.example.ReachingDefinitionsExample -Panalysis=jap.rdtagger`

## a
a = c - a;
        a#8 = c - a#1_2;
/*16*/
/*c has reaching def: c = 1*/
/*c has reaching def: c = c + 2*/
/*a#1_2 has reaching def: a#1_2 = 8*/
/*a#1_2 has reaching def: a#1_2 = 5*/

Respuesta: En este caso, c tiene dos definciones, dependiendo de si se cumple la condición del while, donde c tendría definición c = c +2, o si no se cumple nunca la condición, c tiene definición la constante 1.


## b
return a;
        return a#8;
/*17*/
/*a#8 has reaching def: a#8 = c - a#1_2*/

Respuesta: La variable a usa la definición de c - a#1_2, que es la definición que se obtiene en la sentencia anterior, lo cual tiene sentido porque es la línea inmediata anterior la que modifica a `a`



# Ejercicio 3

Sentencia | a  | b  | c  | d  | r
d = a - b | SI | SI | SI | SI | NO
r = c     | NO | NO | NO | NO | SI
r = d     | NO | NO | NO | NO | SI
return r  | NO | NO | NO | NO | NO