# The Two Pointers Pattern

El patrón de Two Pointers (Dos Punteros) es una de las técnicas de optimización más famosas y utilizadas en las entrevistas técnicas. Consiste en utilizar dos variables que guardan índices (punteros) para recorrer una estructura lineal como un string o una lista de forma simultánea.

En lugar de usar bucles anidados que ralentizan el programa, este patrón nos permite resolver problemas complejos en un solo recorrido, reduciendo el tiempo de ejecución drásticamente.

Existen dos formas principales de aplicar este patrón: Desde los extremos (**Left/Right**) y A diferente velocidad (**Slow/Fast**).

## Variante 1: Punteros desde los extremos (Left / Right)

Esta estrategia coloca un puntero al inicio de la estructura (índice 0) y otro al final (último índice). En cada paso del bucle, los punteros realizan una acción o comparación y luego se mueven el uno hacia el otro hasta cruzarse en el centro.

```python
def two_pointers_left_right(nums):
    left = 0
    right = len(nums) - 1

    # we want to keep moving the pointers until they meet in the middle
    while left < right:
        left += 1
        right -= 1

```

### Cuándo usarlo

- Para comparar elementos simétricos (como en palíndromos).
- Para invertir el orden de un conjunto de datos.
- Para buscar pares de elementos en estructuras ordenadas.

## Variante 2: Punteros a diferente velocidad (Slow / Fast)

También conocido como el algoritmo de la liebre y la tortuga (_Hare and Tortoise_). En esta estrategia, ambos punteros arrancan en la misma posición inicial y se mueven en la misma dirección, pero uno avanza más rápido que el otro (por ejemplo, el puntero `fast` avanza 2 pasos por cada paso que da el puntero `slow`).

```python
def two_pointers_fast_slow(nums):
    slow = 0
    fast = 2 # fast could be any number greater than 0, but it should be greater than slow

    # we want to keep moving the fast pointer until it reaches the end of the array
    while fast < len(nums):
        slow += 1
        fast += 2

```

### Cuándo usarlo

- Para encontrar el punto medio de una estructura sin medir su longitud total de antemano.
- Para detectar ciclos infinitos o bucles repetitivos en caminos de datos.
- Para eliminar duplicados o filtrar elementos mientras se avanza.

## Big O

|  **Variante**  | **Time Complexity** | **Space Complexity** |
| :------------: | :-----------------: | :------------------: |
| **left/right** |       `O(n)`        |        `O(1)`        |
| **slow/fast**  |       `O(n)`        |        `O(1)`        |

## ¿Cómo saber cuándo activar este patrón en tu mente?

Considera usar Two Pointers si tu problema cumple las siguientes condiciones:

1. Estás trabajando con datos lineales y ordenados (strings, arrays/listas).
2. Tu solución inicial o intuitiva requiere usar bucles anidados (`O(n²)`), y necesitas reducirla a un rendimiento lineal (`O(n)`).
3. El problema te pide analizar relaciones entre dos elementos diferentes de la misma estructura.

## Ecosistema: Conexiones con otras Estructuras, Algoritmos y Patrones

El patrón de Two Pointers no vive aislado; es la base fundacional de muchas de las estructuras de datos y algoritmos más eficientes en la computación. A medida que avances en el curso, verás este patrón transformado en los siguientes conceptos:

### 1. Estructuras de Datos Relacionadas

- **Arrays / Listas (`O(n)`):** Es el terreno más común para este patrón. Se utiliza para resolver problemas clásicos como _Two Sum_ (encontrar dos números en una lista ordenada que sumen un objetivo) o para invertir un arreglo sobre su propio espacio (_in-place_), intercambiando los elementos de los extremos hacia el centro.
- **Linked Lists / Listas Enlazadas (`O(n)`):** Aquí la variante _Slow / Fast_ (la liebre y la tortuga) es el rey absoluto. Como no puedes acceder a un elemento por su índice directamente (no existe el `lista[5]`), usas dos punteros para encontrar la mitad de la lista en un solo recorrido o para detectar si la lista está corrupta y tiene un ciclo infinito.

### 2. Algoritmos Matemáticos y de Búsqueda

- **Binary Search / Búsqueda Binaria (`O(log n)`):** La búsqueda binaria es, en su esencia, un algoritmo de dos punteros (`low` y `high`). En lugar de moverse de uno en uno, calculan un punto medio (`mid`) para ir partiendo el espacio de búsqueda a la mitad en cada paso.
- **Algoritmos de Ordenamiento Avanzado (`O(n log n)`):** Algoritmos como _Merge Sort_ (ordenamiento por mezcla) y _Quick Sort_ (ordenamiento rápido) utilizan punteros para comparar y fusionar sublistas, o para mover elementos menores y mayores alrededor de un pivote.

### 3. Patrones de Diseño Derivados

- **Sliding Window / Ventana Deslizante:** Este patrón es una evolución directa de Two Pointers. En lugar de que los punteros se muevan en direcciones opuestas o a velocidades fijas, los dos punteros se mueven en la misma dirección definiendo los límites (inicio y fin) de una "ventana" o subconjunto de datos. Se usa para resolver problemas de sub-arreglos o sub-strings (por ejemplo: _"encuentra la sub-cadena más larga sin caracteres repetidos"_).
