TERMINOLOGIA: <v,l> (la variable v se define en la linea l).

# Ejercicio 1

Comando: `./gradlew soot -PtargetClass=com.example.Foo -Panalysis=jap.rdtagger`

## a: `System.out.println(rv);`

        virtualinvoke $stack5.<java.io.PrintStream: void println(int)>($stack4);
/*7*/
/*$stack5 has reaching def: $stack5 = <java.lang.System: java.io.PrintStream out>*/
/*$stack4 has reaching def: $stack4 = virtualinvoke $stack3.<com.example.Foo: int bar(int)>(0)*/

Respuesta:

IN[7] = OUT[6] = {<f,5>, <rv,6>}

Aqui tenemos que tener en cuenta la llamada a out alcanza su definicion en la misma lina 7 siendo guardada en el stack.

OUT[7] = (IN[7] - KILL[7]) union GEN[7]
        = ({<f,5>, <rv,6>} - {}) union {<out,7>} (KILL[7] es vacio ya que "out" no existe anteriormente)
        = {<f,5>, <rv,5>, <out,7>}

Luego, la salida 7 tiene una variable mas, la cual es "out" y ademas no borra ninguna de las variables definidas anteriormente.
En este caso entonces, imprimir en pantalla primero debe utilizar la llamada de sistema, que se guarda en la posición stack5 en el stack que tiene como definición la llamada misma a sistema.
Finalmente, stack4 usa la definición de que stack3 ejecute el método bar con el valor 0 pasado por parámtro. A su vez, stack3 es la instanciación del objeto Foo. Tiene sentido que todas estas variables vivan en el stack por como Java maneja en memoria la instanciación de nuevos objetos.


## b: `return c;`
        return c;
/*17*/
/*c has reaching def: c = x*/
/*c has reaching def: c = x + 1*/

Respuesta:
IN[17] = OUT[13] union OUT[15] = {<x,13>} union {<x,15>} = {<x,13>,<x,15>}
OUT[17] = IN[17] (ya que no tenemos una asignacion)
En este caso, tenemos dos posibles definiciones para c porque son las dos posibles ramas del if, donde se pregunta si el parámetro x es igual a 0 o no.
Siendo estas definiciones: `"c = x` y `c = x + 1`


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 2

Comando: `./gradlew soot -PtargetClass=com.example.ReachingDefinitionsExample -Panalysis=jap.rdtagger`

## a: `a = c - a;`

        a#8 = c - a#1_2;
/*16*/
/*c has reaching def: c = 1*/
/*c has reaching def: c = c + 2*/
/*a#1_2 has reaching def: a#1_2 = 8*/
/*a#1_2 has reaching def: a#1_2 = 5*/

Respuesta:
IN[16] = OUT[13] union OUT[14] = {<7,a>,<10,a>,<12,c>} union {<7,a>,<10,a>,<14,c>} = {<7,a>,<10,a>,<12,c>,<14,c>}
OUT[16] = (IN[16] - KILL[16]) union GEN[16]
        = ({<7,a>,<10,a>,<12,c>,<14,c>} - {<7,a>,<10,a>}) union {<16,a>}
        = {<12,c>,<14,c>,<16,a>}
De esta manera, `c` tiene dos definciones posbiles, dependiendo de si se cumple la condición del while.
En caso afirmativo `c` tendría definición `c = c + 2`, o si no se cumple nunca la condición, `c` tiene definición la constante `1`.


## b: `return a;`

        return a#8;
/*17*/
/*a#8 has reaching def: a#8 = c - a#1_2*/

Respuesta:
IN[17] = OUT[16] = {<12,c>,<14,c>,<16,a>}
OUT[17] = IN[17] (como no es una asignación tienen el mismo conjunto)
Por lo tanto, la variable a usa la definición de `c - a#1_2`, es la definición que se obtiene en la sentencia anterior.
Lo cual tiene sentido porque es la línea inmediata anterior la que modifica a `a`, mostrando entonces que la salida que nos da la linea 16 es lo que devuelve la salida de la linea 17.


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 3

Sentencia | a  | b  | c  | d  | r
d = a - b | SI | SI | SI | SI | NO
r = c     | NO | NO | NO | NO | SI
r = d     | NO | NO | NO | NO | SI
return r  | NO | NO | NO | NO | NO