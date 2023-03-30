# Cómo hacer un procesador de 8 bits?

## 05-03-2023 Día 1:

Busco información en general para darme contexto de mi objetivo.

* [https://www.instructables.com/How-to-Build-an-8-Bit-Computer/](https://www.instructables.com/How-to-Build-an-8-Bit-Computer)
* [https://dangrie158.github.io/SAP-1/](https://dangrie158.github.io/SAP-1/)
* [https://medium.com/@karlrombauts/building-an-8-bit-computer-in-logisim-part-1-building-blocks-a4f1e5ea0d03](https://medium.com/@karlrombauts/building-an-8-bit-computer-in-logisim-part-1-building-blocks-a4f1e5ea0d03)
* [https://www.linkedin.com/pulse/design-8-bit-cpu-ross-mcgowan/](https://www.linkedin.com/pulse/design-8-bit-cpu-ross-mcgowan/)

Procesadores de referencia

* [https://github.com/eddiewastaken/logisim-discrete-CPU](https://github.com/eddiewastaken/logisim-discrete-CPU)
* [https://github.com/leonicolas/computer-8bits](https://github.com/leonicolas/computer-8bits)

Preguntando a ChatGPT sobre cuál es la secuencia que sigue el procesador ha dicho [respuesta](examples/cycle.md)

## 06-03-2023 Día 2:

Estoy atascado, he mirado otros procesadores y ya tengo un entendimiento sobre la parte física como para empezar a plantear el mío, sin embargo, no tengo idea alguna de cuál es su funcionamiento lógico a la hora de ejecutar las instrucciones de la memoria.

Empezaré por entender control Matrix:

* El Control Matrix es una técnica utilizada en el diseño y desarrollo de sistemas electrónicos digitales, que se utiliza para coordinar y controlar el flujo de señales en el sistema.
* En esencia, el Control Matrix es una tabla que describe cómo las diferentes señales en el sistema interactúan entre sí y cómo se coordinan para producir los resultados deseados. El Control Matrix describe las entradas, salidas y señales internas del sistema, y cómo se combinan para realizar operaciones específicas.

Esa es la definición de ChatGPT, pero eso no importa, al buscar información acerca del “control Matrix” me ha llevado de nuevo al canal de [Ben Eater](https://www.youtube.com/@BenEater), con la diferencia de que ahora me he fijado mejor en una serie de [videos](https://www.youtube.com/watch?v=dXdoim96v5A&list=PLowKtXNTBypGqImE405J2565dvjafglHU&index=37) que explican justamente lo que me habría dejado atascado, olé.

## 10-03-2023 Día 3:

Estoy trasteando un poco con los componentes (j-k flip flop) para crear mis propios registros de 8bits

## 11-03-2023 Día 4:

Al final sustituí los j-k por registers (que se puede utilizar más de 1 bit). He tenido problemas para editar la apariencia de mis circuitos custom, pero como no... era que había que habilitar que se vieran de la manera personalizada y no de la default 🥴.

Ya tengo una primera versión de los registros, ahora voy a hacer la alu.

Termina la alu solo le falta cambiar la apariencia del circuito.

## 12-03-2023 Día 5:

Hoy he terminado el aspecto custom de la ALU y he mejorador los registros personalizándolos por separado (A-B) para que se adapten mejor a la arquitectura que quiero.

He tenido que hacer un rediseño porque no sabía que los registros tenían que poder poner lo que tenían en el bus.

## 13-03-2023 Dia 6:

He añadido la RAM más el registro MAR, lo he probado y funciona correctamente

## 14-03-2023 Día 7:

He añadido el contador de programa (PC), lo he probado y puede contar, recibir una dirección en cualquier momento y puedo enviarlo al bus.

## 18-03-2023 Día 8:

Hoy solo he añadido el registro de salida.

## 19-03-2023 Día 9:

He empezado el decodificador de instrucciones, estoy entendiendo su funcionamiento y sin duda alguna es la parte más compleja.

## 20-03-2023 Día 10:

Añadido del registro de instrucciones, más las conexiones de los diferentes componentes para el futuro decodificador de instrucciones.

## 21-03-2023 Día 11:

Hoy sigo con el decodificador de instrucciones, pero por el camino he tenido que cambiar el MAR porque no había entendido bien como decodificaba los 4bits de dirección, por lo demás, pruebas manuales para ver que todo funviona bien. Siguiendo con las mejoras he hecho que los LEDs de información sean más rápidos de consultar cambiándolos de color, he visto que tenía un componente que cogía más bits de los que necesitaba como el MAR y el PC. Junto con un apaño (añadido de una OR al su entrada de reloj) de la RAM, ya que esta no funcionaba igual que la de Ben Eater y consumía una instrucción de más.

Cambios importantes en los registros A y B, los outputs que alimentan a la ALU, estaban al revés 🤬.
He conseguido ejecutar el primer programa (manualmente (sin ID)) del procesador olé.

```
LDA 14
ADD 15
OUT
```

Tanto 14 como 15 son direcciones de memoria.

He terminado la plantilla de Excel para definir mis instrucciones y sus microcódigos. Día productivo.

## 23-03-2023 Día 12:

Hoy le he dado forma al decodificador de instrucciones y conectado al mismo. También he conectado todos los componentes mediante "túneles" y le ha dado un aspecto mucho más limpio.

Siguiendo con el desarrollo del decodificador de instrucciones, he creado un Excel con unas instrucciones básicas para utilizarlas de referencia. Tengo que comprobar que están bien y hacer un script para generar la ROM

## 24-03-2023 Día 13:

Hoy he empezado con la generación de la ROM y he hecho muchos progresos: generar una ROM válida vacía, generar las posibles direcciones de las instrucciones, según su step, flags, número.

## 25-03-2023 Día 14:

Al final he tenido que crear yo mismo un módulo que trabaja con la ROM, pero ya lo he conseguido, ya puedo generar la ROM, leerla, escribirla como yo quiera… uf.

Me he encontrado muchos bugs en el código que genera la ROM, muchos bugs en el circuito real, problemas con los microcódigos de las instrucciones. He estado todo el día con encontrándome un problema tras otro… PERO AL FINAL LO HE CONSEGUIDO, HE LOGRADO EJECUTAR EL PROGRAMA DE SUMA BÁSICA OLEEEEEEEEEEEEEEEE JODEEEEEEEEEEEEEEEEEEEEEEEEER.

He empezado a pasar los circuitos en sucio a un nuevo proyecto en limpio, también he decidió el nombre del ordenador, Marina.

## 26-03-2023 Día 15:

Hoy he terminado de pasar los circuitos a limpio en un proyecto nuevo y también le he dado a Marina la complejidad de Turing al añadir los saltos condicionales. Ahora Marina no solo puede actuar con base en lo que lee en su memoria, sino que también a las condicionales que nosotros queramos.

También me he tirado 1 hora rallado por un problema con las direcciones de memoria, el cual era que las había escrito mal en el papel…🙂.

Ahora lo que queda es hacer el display decimal para el registro de salida, documentar y subirlo al repo.

## 27-03-2023 Día 16:

Hoy he terminado el generador de ROM para el decodificador de 8bits a un display de 7 segmentos, más el circuito para el display. Ahora el registro de salida muestra la salida en decimal.

He cambiado el diseño del circuito principal de Marina, ahora el registro de salida está arriba, junto con los pines de programación manual y los pines manuales del bus. Para separar la parte de “usuario” de la parte que no requiere la interacción directa.

## 28-03-2023 Día 17:

Hoy he empezado la documentación de Marina, junto con el compilador. La documentación es bastante exigente porque estoy tocando mucho la máquina de Turing, pero me está ayudando a mi propio entendimiento. El compilador no está siendo muy complicado, pero todavía no lo he acabado, así que me callo.

He añadido un marco de cables para el label del nombre y ha quedado de locos.

## 29-03-2023 Día 18:

He terminado el compilador, no es muy cómodo de usar, pero el proyecto se está alargando demasiado.

## 30-03-2023 Día 19:

Proyecto terminado
