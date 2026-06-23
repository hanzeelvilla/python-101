# Week 3: Introduction to Data Collections - Lists and Tuples

¡Bienvenido al **Módulo 2**! Hasta ahora, tus programas han manejado información utilizando variables individuales (un solo string, un solo entero, un solo booleano). En el mundo real, el software maneja miles o millones de datos agrupados.

Esta semana daremos el gran salto hacia las **Colecciones de Datos**. Aprenderás a crear contenedores dinámicos en memoria, a manipularlos de forma quirúrgica y a entender la diferencia crítica entre estructuras que pueden cambiar (**mutables**) y estructuras que permanecen fijas (**inmutables**).

---

## Objetivos de la semana

- Comprender el concepto de colecciones indexadas y cómo se almacenan en memoria.
- Dominar el ciclo de vida de una lista (CRUD: Create, Read, Update, Delete).
- Manipular subconjuntos de datos de manera avanzada utilizando **Slicing**.
- Evaluar el impacto en Big O de los métodos nativos de ordenamiento (`.sort()` vs `sorted()`).
- Implementar **Tuplas** como estructuras seguras e inmutables para la protección de datos.

---

## Orden de lectura y estudio

Sigue este orden para asimilar los conceptos de forma progresiva:

1. **[01_lists_basics_and_crud.md](./01_lists_basics_and_crud.md)**
    - Aprenderás la anatomía de una lista, cómo medir su longitud y cómo agregar, modificar o eliminar elementos usando diferentes estrategias nativas.
2. **[02_slicing_and_sorting.md](./02_slicing_and_sorting.md)**
    - Descubrirás el poder del rebanado (Slicing) para extraer fragmentos de información y aprenderás a ordenar datos analizando el uso de la memoria RAM.
3. **[03_tuples_and_immutability.md](./03_tuples_and_immutability.md)**
    - Conocerás a las tuplas, las primas inmutables de las listas, y entenderás por qué la restricción de no poder modificar un dato es una ventaja de seguridad en el software.

---

## Tareas y Ejercicios

Al final de las lecturas correspondientes se desbloquearán los desafíos prácticos de esta semana, enfocados en poner a prueba tu control sobre la manipulación de colecciones:

- **Desafíos locales:** Ejercicios diseñados para implementar algoritmos modulares utilizando listas y tuplas.
- **Plataformas externas:** Problemas seleccionados de Codewars y LeetCode para evaluar tu capacidad de resolver problemas reales de la industria utilizando estructuras indexadas.

---

## Checklist de entrega

- [ ] He leído los 3 archivos de contenido de la semana.
- [ ] Puedo explicar la diferencia entre los métodos `.pop()` y `.remove()`.
- [ ] Entiendo cuándo una operación de ordenamiento es _in-place_ y cuándo consume memoria RAM adicional.
- [ ] Sé en qué escenario es preferible usar una Tupla sobre una Lista.
- [ ] He completado todos los ejercicios prácticos locales y externos asignados.

---

## Concepto clave de la semana: Data Containers

Hasta la semana pasada, tus variables eran como **cajas de zapatos individuales**: si tenías 10 objetos, necesitabas 10 cajas separadas con nombres distintos. A partir de esta semana, aprenderás a usar **mochilas de expedición** (Listas). Una sola mochila puede guardar múltiples objetos ordenados, crecer si decides meter más cosas, encogerse si las sacas, y te permite acceder a cualquier artículo simplemente recordando en qué posición lo guardaste.
