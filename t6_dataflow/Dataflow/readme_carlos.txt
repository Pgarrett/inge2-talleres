TERMINOLOGIA: <v,l> (la variable v se define en la linea l).


Comando ejecutado para el ejercicio 1: ./gradlew soot -PtargetClass=com.example.Foo -Panalysis=jap.rdtagger

1)a)Esto nos tira Reaching Defs Tagger para la linea: System.out.println(rv);

--------------------------------------------------------------RESPUESTA--------------------------------------------------------------------

/*7*/
        virtualinvoke $stack5.<java.io.PrintStream: void println(int)>($stack4);
/*7*/
/*$stack5 has reaching def: $stack5 = <java.lang.System: java.io.PrintStream out>*/
/*$stack4 has reaching def: $stack4 = virtualinvoke $stack3.<com.example.Foo: int bar(int)>(0)*/

Nos devuelve esto por lo siguiente:
Vamos a analizar la entrada (IN) y la salida (OUT) de la linea 17, para saber cuando alcanza su definición cada variable hasta este punto:

IN[7] = OUT[6] = {<f,5>, <rv,6>}

Aqui tenemos que tener en cuenta la variable temporal out que alcanza su definicion en la misma lina 7 (de manera implicita,
ya que no hay una asignación en el código)

OUT[7] = (IN[7] - KILL[7]) union GEN[7]
        = ({<f,5>, <rv,6>} - {}) union {<out,7>} (KILL[7] es vacio ya que "out" no existe anteriormente)
        = {<f,5>, <rv,5>, <out,7>}

Aca claramente lo que dice que la salida 7 tiene una variable mas, la cual es "out" y ademas no borra ninguna de las variables
definidas anteriormente.

------------------------------------------------------------------------------------------------------------------------------------------

b)Esto nos tira Reaching Defs Tagger para la linea: return c;

--------------------------------------------------------------RESPUESTA--------------------------------------------------------------------

/*17*/
/*c has reaching def: c = x*/
/*c has reaching def: c = x + 1*/

Nos devuelve esto por lo siguiente:
Vamos a analizar la entrada (IN) y la salida (OUT) de la linea 17, para saber cuando alcanza su definición cada variable hasta este punto:

IN[17] = OUT[13] union OUT[15] = {<x,13>} union {<x,15>} = {<x,13>,<x,15>}
OUT[17] = IN[17] (ya que no tenemos una asignacion)
por ende tenemos "c = x" y "c = x + 1".

------------------------------------------------------------------------------------------------------------------------------------------

Comando ejecutado para el ejercicio 2: ./gradlew soot -PtargetClass=com.example.ReachingDefinitionsExample -Panalysis=jap.rdtagger

2)a) Esto nos tira Reaching Defs Tagger para la linea: a = c - a;

--------------------------------------------------------------RESPUESTA--------------------------------------------------------------------

/*16*/
/*c has reaching def: c = 1*/
/*c has reaching def: c = c + 2*/
/*a#1_2 has reaching def: a#1_2 = 8*/
/*a#1_2 has reaching def: a#1_2 = 5*/

Nos devuelve esto por lo siguiente:
Vamos a analizar la entrada (IN) y la salida (OUT) de la linea 16, para saber cuando alcanza su definición cada variable hasta este punto:

IN[16] = OUT[13] union OUT[14] = {<7,a>,<10,a>,<12,c>} union {<7,a>,<10,a>,<14,c>} = {<7,a>,<10,a>,<12,c>,<14,c>}
OUT[16] = (IN[16] - KILL[16]) union GEN[16]
        = ({<7,a>,<10,a>,<12,c>,<14,c>} - {<7,a>,<10,a>}) union {<16,a>}
        = {<12,c>,<14,c>,<16,a>}

Esto es lo que nos quiere decir la salida de soot para esta linea.

------------------------------------------------------------------------------------------------------------------------------------------

b) Esto nos tira Reaching Defs Tagger para la linea: return a;

--------------------------------------------------------------RESPUESTA--------------------------------------------------------------------

/*17*/
/*a#8 has reaching def: a#8 = c - a#1_2*/

Nos devuelve esto por lo siguiente:
Vamos a analizar la entrada (IN) y la salida (OUT) de la linea 17, para saber cuando alcanza su definición cada variable hasta este punto:

IN[17] = OUT[16] = {<12,c>,<14,c>,<16,a>}
OUT[17] = IN[17] (como no es una asignación tienen el mismo conjunto)

Aca claramente dice que la salida que nos da la linea 16 es lo que devuelve la salida de la linea 17.

------------------------------------------------------------------------------------------------------------------------------------------

Comando ejecutado para el ejercicio 3: ./gradlew soot -PtargetClass=com.example.LiveVariablesExample -Panalysis=jap.lvtagger

3)

Sentencia           a       b       c       d        r
--------------------------------------------------------
d = a - b;         si       si      si      si      no
r = c;             no       no      no      no      si
r = d;             no       no      no      no      si
return r;          no       no      no      no      no


-----------
d = a - b;
/*8*/
/*Live Variable: c*/
/*Live Variable: d*/
/*Live Variable: a*/
/*Live Variable: b*/

-------
r = c;
/*11*/
/*Live Variable: r*/

-------
r = d;
/*13*/
/*Live Variable: r*/

-------
label2:
return r;
/*15*/