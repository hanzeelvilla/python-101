# Week 4: Advanced Data Collections - Dictionaries and Sets

¡Bienvenido a la última semana del **Módulo 2**! Hasta ahora, has manejado colecciones indexadas (Listas y Tuplas) donde la única forma de acceder a un dato era recordando su posición numérica (`0, 1, 2...`). Aunque esto es útil, no siempre es la forma más natural de modelar la realidad.

Esta semana romperemos el paradigma de los índices numéricos para explorar dos estructuras de datos sumamente poderosas: los **Diccionarios** (que nos permiten asociar información mediante etiquetas de texto) y los **Sets** (ideales para garantizar la unicidad de los datos y realizar filtros relámpago).

Terminaremos la semana con una guía analítica para aprender a elegir la estructura de datos perfecta ante cualquier problema en blanco.

## Objetivos de la semana

- Comprender la estructura Clave-Valor (`Key: Value`) para modelar datos complejos del mundo real.
- Dominar el ciclo de vida de un diccionario (CRUD) y aprender a realizar lecturas seguras para evitar caídas del sistema.
- Iterar diccionarios de forma profesional utilizando los métodos `.keys()`, `.values()` y `.items()`.
- Implementar Conjuntos (Sets) para eliminar duplicados de forma masiva en una sola línea de código.
- Comparar analíticamente las 4 colecciones de Python para desarrollar intuición arquitectónica de software.

## Orden de lectura y estudio

Organiza tu semana de estudio siguiendo este orden de archivos:

1. **[01_dictionaries.md](./01_dictionaries.md)**
   - Aprenderás la anatomía de un diccionario, cómo estructurar datos relacionales, el uso del método seguro `.get()` y cómo acumular estados dinámicos paso a paso.
2. **[02_sets_and_uniqueness.md](./02_sets_and_uniqueness.md)**
   - Descubrirás el poder de los sets para limpiar colecciones con datos repetidos y cómo realizar cruces de información utilizando lógica matemática de conjuntos.
3. **[03_collections_comparison.md](./03_collections_comparison.md)**
   - La "hoja de trucos" (Cheat Sheet) definitiva del módulo. Una guía comparativa de características, rendimiento y escenarios del mundo real para saber exactamente cuándo usar cada contenedor.

## Checklist de entrega

- [ ] He leído las lecturas de Diccionarios, Sets y la Guía de Comparación.
- [ ] Puedo explicar la diferencia entre intentar acceder a una llave con `dict[key]` y usar `dict.get(key)`.
- [ ] Entiendo por qué una lista no puede ser utilizada como llave de un diccionario.
- [ ] Sé cómo limpiar los duplicados de una lista usando un Set en una sola línea de código.
- [ ] Puedo justificar técnicamente la elección de una estructura sobre otra según el problema.
- [ ] He completado y probado todos los retos de código locales de esta semana.

## Concepto clave de la semana: No-Indexed Containers

Hasta la semana pasada, tus colecciones eran como **filas de asientos de un teatro**: para encontrar a alguien, tenías que ir a la fuerza al asiento 0, luego al 1, luego al 2. A partir de esta semana, tus contenedores serán como **agendas de contactos** (Diccionarios). No te importa en qué posición física de la libreta está guardado el número de "Mamá"; simplemente buscas la etiqueta "Mamá" y obtienes el valor de inmediato.
