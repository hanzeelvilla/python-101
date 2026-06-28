# 02: Advanced Slicing and Sorting Techniques

Ahora que dominas las operaciones básicas de las listas (CRUD), es momento de aprender a manipularlas a gran escala. En esta lectura descubrirás cómo extraer fragmentos quirúrgicos de información (**Slicing**) y cómo ordenar conjuntos de datos analizando el impacto que esto tiene en la memoria RAM de tu servidor (**Big O**).

---

## 1. El Arte del Slicing (Rebanado)

El **Slicing** es una técnica en python que te permite extraer una sub-lista completa de una lista original sin modificarla. Su sintaxis utiliza tres parámetros dentro de los corchetes, separados por dos puntos:

$$\text{lista}[\text{start}:\text{stop}:\text{step}]$$

- **`start`:** El índice donde inicia la extracción (inclusive). Por defecto es `0`.
- **`stop`:** El índice donde se detiene la extracción (**exclusivo**, no incluye este elemento). Por defecto es el final de la lista.
- **`step`:** El tamaño del salto entre elementos. Por defecto es `1`.

```python
letters = ["a", "b", "c", "d", "e", "f", "g"]

# Example 1: Extract from index 1 up to 4 (5 is excluded)
fragment_1 = letters[1:5]
print(fragment_1) # Output: ['b', 'c', 'd', 'e']

# Example 2: Omitting parameters (takes defaults)
from_start_to_3 = letters[:4]  # From start up to index 3
from_3_to_end = letters[3:]    # From index 3 up to the very end
print(from_start_to_3)         # Output: ['a', 'b', 'c', 'd']
print(from_3_to_end)           # Output: ['d', 'e', 'f', 'g']

# Example 3: Using a custom step
every_second_letter = letters[::2]
print(every_second_letter)     # Output: ['a', 'c', 'e', 'g']
```

## Slicing Tricks de Nivel Profesional

### A. Invertir una lista instantáneamente: `[::-1]`

Al configurar un `step` negativo de `-1` y omitir el inicio y el fin, Python entiende automáticamente que debe recorrer la lista al revés, desde el final hasta el principio.

```python
numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1]
print(reversed_numbers) # Output: ['5', '4', '3', '2', '1']
```

### B. Clonar una lista de forma segura: `[:]`

En Python, si haces `lista_b = lista_a`, no estás duplicando los datos; solo estás creando dos nombres que apuntan a la misma lista en memoria. Si modificas `lista_b`, `lista_a` también cambiará. Para duplicar de verdad, usamos slicing vacío:

```python
original = [10, 20, 30]

# Danger: This is NOT a copy, it's a reference shortcut
fake_copy = original

# Safe: This extracts ALL elements into a completely distinct new list
real_copy = original[:]

fake_copy[0] = 99
print(original)  # Output: [99, 20, 30] ❌ The original was corrupted!

real_copy[1] = 88
print(original)  # Output: [99, 20, 30]  The original stays safe!
```

## 2. Ordenamiento de Listas: `.sort()` vs `sorted()`

Python tiene dos formas nativas de ordenar elementos. Aunque ambas logran el mismo resultado visual, operan de formas totalmente distintas bajo el capó de la memoria RAM.

### Método `.sort()`(In-Place)

Modifica la lista original directamente en su lugar de memoria. No crea estructuras nuevas.

- Time Complexity: `O(n log n)`
- Space Complexity: `O(1)` — Excelente uso de memoria, es constante.

### Función `sorted()` (Any Iterable)

Deja la lista original intacta y retorna una nueva lista completamente limpia y ordenada.

- Time Complexity: `O(n log n)`
- Space Complexity: `O(n)` — Consume memoria RAM adicional proporcional al tamaño de la lista.

```python
# --- Scenario A: Using .sort() ---
prices = [45.0, 12.5, 99.9, 5.0]
prices.sort() # Modifies the original list directly
print(prices) # Output: [5.0, 12.5, 45.0, 99.9]

# --- Scenario B: Using sorted() ---
ages = [25, 18, 40, 31]
ordered_ages = sorted(ages) # Returns a completely separate new list

print(ages)         # Output: [25, 18, 40, 31] (Original is intact!)
print(ordered_ages) # Output: [18, 25, 31, 40] (New ordered container)
```

## Retos Cortos

### 1. El Rebanado Avanzado

Dada la siguiente lista, ¿cuál será el resultado exacto de la operación de slicing mostrada abajo?

```python
data = [10, 20, 30, 40, 50, 60, 70, 80]
result = data[1:6:2]
print(result)
```

<details>
<summary>💡 Ver Solución</summary>

- **En la consola se imprimirá:** `[20, 40, 60]`

**Explicación:** El corte inicia en el índice 1 (`20`) y llega de forma exclusiva antes del índice 6 (el índice 5 es `60`). Al aplicar un `step` de `2`, avanza saltando de dos en dos posiciones: toma el `20` (índice 1), se salta el `30`, toma el `40` (índice 3), se salta el `50`, y toma el `60` (índice 5).

</details>

---

### 2. El Engaño del Retorno

Analiza el siguiente código. ¿Qué se imprimirá en la consola en la última línea? ¿Funcionó el ordenamiento?

```python
scores = [100, 50, 80]
ordered_scores = scores.sort()
print(ordered_scores)
```

<details>
<summary>💡 Ver Solución</summary>

- **En la consola se imprimirá:** `None`

**Explicación:** Este es uno de los errores más frustrantes para los principiantes. El método `.sort()` modifica la lista in-place, pero su valor de retorno es `None`. Al asignarlo a la variable `ordered_scores`, destruiste el acceso al resultado de esa línea. La forma correcta de imprimir los puntajes ordenados era imprimiendo directamente la variable original: `print(scores)`.

</details>
