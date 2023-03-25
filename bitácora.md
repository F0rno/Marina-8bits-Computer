# ¿Cómo hacer un procesador de 8 bits?

## 05-03-2023 Día 1:

Busco información en general para darme contexto de mi objetivo.

* [https://www.instructables.com/How-to-Build-an-8-Bit-Computer/](https://www.instructables.com/How-to-Build-an-8-Bit-Computer)
* [https://dangrie158.github.io/SAP-1/](https://dangrie158.github.io/SAP-1/)
* [https://medium.com/@karlrombauts/building-an-8-bit-computer-in-logisim-part-1-building-blocks-a4f1e5ea0d03](https://medium.com/@karlrombauts/building-an-8-bit-computer-in-logisim-part-1-building-blocks-a4f1e5ea0d03)
* [https://www.linkedin.com/pulse/design-8-bit-cpu-ross-mcgowan/](https://www.linkedin.com/pulse/design-8-bit-cpu-ross-mcgowan/)

Procesadores de referencia

* [https://github.com/eddiewastaken/logisim-discrete-CPU](https://github.com/eddiewastaken/logisim-discrete-CPU)
* [https://github.com/leonicolas/computer-8bits](https://github.com/leonicolas/computer-8bits)

Preguntando a ChatGPT sobre cual es la secuenciea que sigue el procesador a dicho [respuesta](examples/cycle.md)

## 06-03-2023 Día 2:

Estoy atascado, he mirado otros procesadores y ya tengo un entendimiento sobre la parte fisica como para empezar a plantear el mio, sin embargo no tengo idea alguna de cual es su funcíonamiento logico a la hora de ejecutar las instrucciones de la memoria.

Empezare por entender control matrix:

* La Control Matrix es una técnica utilizada en el diseño y desarrollo de sistemas electrónicos digitales, que se utiliza para coordinar y controlar el flujo de señales en el sistema.
* En esencia, la Control Matrix es una tabla que describe cómo las diferentes señales en el sistema interactúan entre sí y cómo se coordinan para producir los resultados deseados. La Control Matrix describe las entradas, salidas y señales internas del sistema, y cómo se combinan para realizar operaciones específicas.

Esa es la difinicon de ChatGPT, pero eso no importa, al buscar informacion acerca del "control matrix" me ha llevado de nuevo al canal de [Ben Eater](https://www.youtube.com/@BenEater), con la diferencia de que ahora me he fijado mejor en una serie de [videos](https://www.youtube.com/watch?v=dXdoim96v5A&list=PLowKtXNTBypGqImE405J2565dvjafglHU&index=37) que explican justamente lo que me habia dejado atascado, olé.

## 10-03-2023 Día 3:

Estoy trasteando un poco con los componentes (j-k flip flop) para crear mis propios registros de 8bits

## 11-03-2023 Día 4:

Al final sustitui los j-k por registers (que se puende utilizar más de 1 bit). He tenido problemas para editar la apariencia de mis circutitos custom, pero como no... era que habia que habilitar que se vieran de la manera personalizada y no de la default 🥴.

Ya tengo una primera versión de los registros, ahora voy ha hacer la alu.

Termina la alu solo le falta cambiar la apariencia del circuito.

## 12-03-2023 Día 5:

Hoy he terminado el aspector custom de la ALU y he mejorador los registros personalizandolos por separado (A-B) para que se adapten mejor a la arquitectura que quiero.

He tenido que hacer un rediseño porque no sabia que los registros tenian que poder poner lo que tenian en el bus.

## 13-03-2023 Dia 6:

He añadido la RAM más el registro MAR, lo he probado y funciona correctamente

## 14-03-2023 Día 7:

He añadido el contador de programa (PC), lo he probado y puede contar, recivir una dirección en cualquier momento y puedo enviarlo al bus.

## 18-03-2023 Día 8:

Hoy solo he añadido el registro de salida.

## 19-03-2023 Día 9:

He empezado el decodificador de instrucciones, estoy entendiendo su funcionamiento y sin duda alguna es la parte más compleja.

## 20-03-2023 Día 10:

Añadido del registro de instrucciones, más las conexiones de los diferentes componentes para el futuro decodificador de instrucciones.

## 21-03-2023 Día 11:

Hoy sigo con el decodificador de instrucciones, pero por el camino he tenido que cambiar el MAR porque no habia entendido bien como decodificaba los 4bits de dirección, por lo demas, pruebas manuales para ver que todo funviona bien. Siguiendo con las mejoras he hecho que los LEDs de información sean más rapidos de con sultar cambiandolos de color, he visto que tenia un componente que cogia más bits de los que necesitaba como el MAR y el PC. Junto con un apaño (añadido de una OR al su entrada de reloj) de la RAM ya que esta no funcionaba igual que la de Ben Eater y consumia una instrucción de más.

Cambios importantes en los registros A y B, los outputs que alimentan a la ALU, estaban al reves 🤬.
He conseguido ejecutar el primer programa (manualmente (sin ID)) del procesador olé.

```
LDA 14
ADD 15
OUT
```

Tanto 14 como 15 son direciones de memoria.

He terminado la plantilla de execl para definir mis instrucciones y sus micro-códigos. Día productivo.

## 23-03-2023 Día 12:

Hoy le he dado forma al decodificador de instrucciones y conectado al mismo. Tambien he conectado todos los componentes mediante "tuneles" y le ha dado un aspecto mucho más limpio.

Siguiendo con el desarrollo del decodificador de instrucciones he creado un execl con unas instrucciones basicas para utilizarlas de referencia. Tengo que comprobar que estan bien y hacer un script para generar la ROM

## 24-03-2023 Día 13:

Hoy he empezado con la generación de la ROM y he hecho muchos progresos: generar una ROM valida vacia, generar las posibles direcciones de las instrucciones segun su step, flags, número.
