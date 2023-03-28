# Marina

Este proyecto trata sobre como crear un ordenador de 8bits, que cumpla los requisitos de una máquina de turing:

* Leer/Escribir caracteres de una memoria
* Poder moverse por esa memoria
* Actuar en base a unos estados definidos

Una vez nuestro ordenador cumpla todos estos requisitos, estaremos seguros de que podra ejecutar cualquier algoritmo de computación.

Todo esto inspirado por la serie de videos de Ben Eater y contado por mi.

## Problema

Queremos hacer un ordenador así que necesitaremos resolver estas cuestiones:

1. ¿Dónde lo vamos a montar?
2. ¿Qué diseño tendra el circuito?
3. Entender la base teorica detras de los ordenadores
4. Entender como funciona la parte practica
5. Ver que componentes necesita para la parte practica

## Soluciones

### 1º Cuestión:

Para crear el circuito de nuestro ordenador usaremos un programa de simulación de circuitos, en este caso yo he elegido logisim-evolution, pero se puede utilizar otro si quereis.

### 2º Cuestión:

A la hora de elegir que forma tendra el circuito se habren una infinidad de diseños, pero en lo personal prefiero usar uno basado en un BUS. Más concretamente el patrón SAP.

![](assets/imgs/SAP.png)

### 3º Cuestión:

Estamos siguiendo los pasos para crear un ordenador, pero. ¿Qué es un ordenador?, pues segun wikipedia es: `una máquina electrónica digital programable que ejecuta una serie de comandos para procesar los datos de entrada, obteniendo convenientemente información que posteriormente se envía a las unidades de salida` y eso es cierto, pero lo que yo quiero es la definición de su modelo teorico fundamental, la máquina de Turing.

#### ¿Qué es la máquina de Turing?

Es un dispositivo que manipula símbolos sobre una tira de cinta de acuerdo con una tabla de reglas.

![](assets/imgs/turing_machine.png)

Un ejemplo visual con una tabla sencilla, para que se entienda mejor:

![](assets/imgs/TuringBeispielAnimatedGIF.gif)

Y ahora con una tabla más compleja:

![](assets/imgs/turing_machine_complex.gif)

Simple ¿no?, pues solo con estas mecanicas tan cencillas se puede ejecutar cualquier algoritmo de computación. Y la verdad, suena a que es mentira o imposible, pero no lo es:

En terminos generales lo que hace la maquina es leer datos de una memoria y actuar en base a ellos siguiendo unas instrucciones predefinidas. ¿No os suena familiar?, es como programar un ordenador, este tambien cuenta con una memoria que se manipula siguiendo unos estados y instrucciones que le hemos dado.

Ahora con todo este contexto podemos decir que:

* Sabemos que es y que hace la máquina de Turing
* Que un ordenador moderno no es más que una máquina de Turing extremadamente compleja que funciona con circuitos electronicos
