# 01: What is Python?

Antes de sumergirnos en la sintaxis y escribir líneas de código, es vital entender qué es Python, de dónde viene y por qué se ha convertido en uno de los lenguajes más populares del planeta.

---

## ¿Qué es Python?

Python es un lenguaje de programación creado por **Guido van Rossum** a finales de los años 80 y lanzado oficialmente en **1991**. Guido buscaba un lenguaje que fuera fácil de leer, potente y que permitiera a los desarrolladores escribir código claro y lógico para proyectos de cualquier escala.

> 🎭 **¿De dónde viene el nombre?**
> Al contrario de lo que muchos piensan por el logotipo, el nombre no se eligió por la serpiente pitón. Guido van Rossum era un gran fanático de un grupo de comediantes británicos de los años 70 llamado **Monty Python** (famosos por su programa _Monty Python's Flying Circus_). Al buscar un nombre que fuera corto, único y un poco misterioso, decidió llamarlo Python.

---

## Características principales

Python destaca en la industria tecnológica gracias a una combinación de características que lo hacen único:

### 1. Código Abierto (Open Source)

Python es gratuito y mantenido por una enorme comunidad global (la _Python Software Foundation_). Cualquiera puede descargar su código fuente, sugerir mejoras, crear herramientas y usarlo para proyectos comerciales sin pagar licencias.

### 2. Lenguaje Interpretado

A diferencia de lenguajes como C++ o Rust, que necesitan un proceso de "compilación" (traducir todo el archivo a código máquina antes de ejecutarse), Python es **interpretado**. Un programa llamado _intérprete_ lee y ejecuta el código línea por línea, en tiempo real. Esto facilita y agiliza el proceso de prueba y corrección de errores durante el desarrollo.

### 3. Lenguaje de Alto Nivel

Está diseñado para ser lo más cercano posible al lenguaje humano (específicamente al inglés). Python abstrae detalles complejos de bajo nivel, como la gestión manual de la memoria del computador o la interacción directa con el procesador. Esto te permite enfocarte en resolver el problema lógico, no en cómo funciona el hardware.

### 4. Lenguaje de Propósito General

No fue creado para una sola tarea específica. Con Python puedes construir prácticamente lo que sea:

- **Desarrollo Web:** Creación del backend de aplicaciones (usando frameworks como Django, FastAPI o Flask).
- **Ciencia de Datos e Inteligencia Artificial:** Análisis de datos, Machine Learning y Deep Learning (con librerías como Pandas, NumPy y TensorFlow).
- **Scripting y Automatización:** Pequeños programas para automatizar tareas repetitivas en tu computadora (renombrar archivos, descargar imágenes de internet, etc.).
- **Videojuegos:** Prototipos rápidos y juegos independientes (usando librerías como Pygame).
- **Aplicaciones de Escritorio:** Programas con interfaz gráfica para Windows, Mac o Linux (usando Tkinter o PyQt).

### 5. Multiparadigma

Un "paradigma" es un estilo o enfoque para organizar tu código. Python no te obliga a programar de una sola forma; soporta:

- **Programación Orientada a Objetos (POO):** Centrada en modelar datos y comportamientos del mundo real.
- **Programación Imperativa/Procedural:** Centrada en dar instrucciones paso a paso.
- **Programación Funcional:** Centrada en el uso y combinación de funciones matemáticas puras.

### 6. Multiplataforma

El código que escribes en Python funciona exactamente igual si lo ejecutas en **Windows, macOS o Linux**, siempre y cuando la computadora tenga instalado el intérprete de Python.

### 7. Gran variedad de módulos nativos ("Batteries Included")

La filosofía de Python es que viene con "baterías incluidas". Esto significa que su librería estándar cuenta con muchísimos módulos nativos listos para usar sin instalar nada extra.

```python
# Un ejemplo de cómo usar módulos nativos de Python
import os
import math

# Usar el módulo matemático nativo
result = math.sqrt(16)
print(f"The square root is: {result}") # Output: 4.0

# Usar el módulo del sistema operativo para ver la ruta actual
current_path = os.getcwd()
print(f"Current working directory: {current_path}")
```

## Desventajas de Python

Aunque Python es una herramienta increíble, no existe el "lenguaje perfecto". Es importante conocer sus debilidades:

- **Velocidad de ejecución:** Al ser un lenguaje interpretado y de tipado dinámico, Python suele ser más lento en ejecución que lenguajes compilados como C, C++ o Go. No es la mejor opción para software donde cada milisegundo cuenta (como motores gráficos de videojuegos AAA o sistemas embebidos de alta frecuencia).
- **Consumo de memoria:** Las estructuras de datos de Python requieren más espacio en la memoria RAM que en otros lenguajes de bajo nivel, lo que puede ser un problema en sistemas con recursos muy limitados.
