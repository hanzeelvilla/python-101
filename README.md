# Python 101

<div align="center">
  <img src="./images/python-logo.svg" alt="Python Logo" width="200">
</div>

¡Bienvenido al curso! Este repositorio contiene todo el material, lecturas, ejercicios y pruebas que utilizaremos a lo largo de las próximas 10 semanas. El objetivo es que pases de entender los fundamentos de la lógica de programación a ser capaz de diseñar tus propias estructuras de datos y algoritmos desde cero.

## Contenido

- [Python 101](#python-101)
  - [Contenido](#contenido)
  - [Introducción](#introducción)
  - [Cómo funciona el curso](#cómo-funciona-el-curso)
  - [Instalaciones necesarias](#instalaciones-necesarias)
    - [Extensiones recomendada para Visual Studio Code](#extensiones-recomendada-para-visual-studio-code)
  - [Tips de estudio](#tips-de-estudio)
  - [Cómo resolver un problema de código](#cómo-resolver-un-problema-de-código)
  - [Material recomendado](#material-recomendado)

## Introducción

Programar no se trata de memorizar sintaxis, sino de resolver problemas. Python es uno de los lenguajes más amigables para empezar, pero a la vez es sumamente poderoso y utilizado en la industria (Desarrollo Web, Inteligencia Artificial, Data Science, etc.). En este curso usaremos Python como la herramienta para aprender a pensar como programadores.

## Cómo funciona el curso

El curso está dividido en semanas. La estructura general del repositorio se ve de la siguiente manera:

```text
.
├── README.md                 # Archivo con una guía general (DEBE SER EL PRIMERO QUE DEBES LEER)
├── week_01/                  # Directorio de la Semana 1
│   ├── README.md             # Guía temática de la semana y orden de lectura
│   ├── 01_variables.md       # Tema específico
│   ├── 02_data_types.md      # Tema específico
│   └── tests/                # Pruebas automatizadas para tus ejercicios
└── week_02/                  # Directorio de la Semana 2
```

En cada semana deberás:

- Leer el `README.md` principal de esa semana para conocer el orden de los temas.
- Estudiar cada archivo de tema y resolver los ejercicios propuestos al final.
- Escribir código a mano cuando se te indique.
- Resolver los problemas de plataformas externas (Codewars / LeetCode).
- Validar tus soluciones locales ejecutando las pruebas automatizadas (tests).

## Instalaciones necesarias

- [Python 3.10 o superior](https://www.python.org/downloads/)
- [git](https://git-scm.com/)
- [Visual Studio Code](https://code.visualstudio.com/)

### Extensiones recomendada para Visual Studio Code

- **Python** (Microsoft) - Soporte para Python, incluyendo linting, debugging y ejecución de pruebas.
- **Error Lens** (Alexander) - Resalta errores y advertencias directamente en el código.

## Tips de estudio

- **Escribe código a mano:** Aunque parezca obsoleto, escribir lógica en papel te obliga a procesar cada línea de código en tu cerebro antes de que la computadora lo evalúe. Previene el "adivinar por prueba y error".
- **No te satures:** Es mejor programar 45 minutos concentrado todos los días, que intentar hacer 6 horas seguidas el fin de semana.
- **Explicar para entender:** Intenta explicarle un concepto o tu solución a un compañero, a un familiar o incluso a un objeto en tu escritorio (técnica del patito de goma). Si puedes explicarlo simple, lo entiendes.

## Cómo resolver un problema de código

Cuando te enfrentes a un ejercicio o problema de LeetCode/Codewars, nunca empieces a escribir código de inmediato. Sigue estos pasos:

- **Entiende el problema:** Lee las instrucciones dos o tres veces. Identifica claramente cuáles son las entradas (inputs) y cuáles deben ser las salidas (outputs).
- **Haz un ejemplo manual:** Escribe en papel un caso de uso con datos inventados y resuelve el problema paso a paso como si fueras la computadora.
- **Escribe pseudocódigo:** Traduce tus pasos manuales a un lenguaje intermedio (español/inglés simple con estructura de código), sin preocuparte por la sintaxis exacta de Python.
- **Pasa a código:** Ahora sí, traduce tu pseudocódigo a código real en Python.
- **Refactoriza:** Si tus pruebas pasan, revisa tu código. ¿Se puede leer más fácil? ¿Hay nombres de variables que se puedan mejorar?

## Material recomendado

- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) - Un libro excelente para principiantes.
- [Python desde cero por Midudev](https://youtu.be/TkN2i-_4N4g?si=vdWBH0BfG5XpaDRO)
