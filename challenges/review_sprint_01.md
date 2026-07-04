# Python Coding Sprint 1

Primera dinámica de repaso. Este archivo contiene una serie de problemas con diferentes niveles de complejidad. Tienes exactamente **30 minutos** para resolver la mayor cantidad de retos posible, acumular puntos y canjearlos por recompensas.

---

## Reglas del Juego

1. **Compra de Pistas:** Si te quedas completamente estancado en un problema, puedes recibir una pista a cambio de **3 puntos**.
2. **Validación:** Para que los puntos de un reto cuenten, el código debe correr sin errores en la consola y cumplir exactamente con el ejemplo de entrada y salida proporcionado.

---

## Sistema de Puntuación

- **Nivel Fácil (10 Puntos):** Ejercicios de una sola herramienta. Se resuelven en 3 a 5 líneas de código.
- **Nivel Intermedio (25 Puntos):** Requieren combinar dos conceptos (bucles + listas, o funciones + condicionales).
- **Nivel Difícil (50 Puntos):** Requieren manipulación de índices o control de flujo.

---

## Lista de Problemas

### NIVEL FÁCIL (10 Puntos c/u)

#### Reto F1: El Limpiador de Negativos

Escribe una función llamada `clean_list` que reciba una lista de números enteros. La función debe modificar la lista original para que cualquier número que sea negativo se convierta automáticamente en `0`.

**Entrada de ejemplo:**

```python
numbers = [10, -5, 20, -1, 5]
clean_list(numbers)
print(numbers)
```

**Salida esperada:**

```bash
[10, 0, 20, 0, 5]
```

#### Reto F2: El Validador de Esquinas

Escribe una función llamada `check_extremes` que reciba una cadena de texto (string). La función debe devolver `True` si la primera letra y la última letra son exactamente iguales, o `False` si son diferentes.

Asegúrate de que no afecte si una es mayúscula y la otra minúscula.

- Ejemplo de uso 1: `check_extremes("Radar")` Retorna: `True`
- Ejemplo de uso 2: `check_extremes("Python")` Retorna: `False`

### NIVEL INTERMEDIO (25 Puntos c/u)

#### Reto I1: El Clonador Invertido

Escribe una función llamada `secure_reverse` que reciba una lista de elementos. La función debe devolver una nueva lista con los mismos elementos pero en orden inverso, **garantizando que la lista original quede intacta**.

**Entrada de ejemplo:**

```python
original_tasks = ["Task 1", "Task 2", "Task 3"]
reversed_tasks = secure_reverse(original_tasks)

print("Nueva:", reversed_tasks)
print("Original:", original_tasks)
```

**Salida esperada:**

```text
Nueva: ['Task 3', 'Task 2', 'Task 1']
Original: ['Task 1', 'Task 2', 'Task 3']
```

#### Reto I2: Contador de Golpes

Un boxeador está entrenando ráfagas de combinaciones sobre el costal. Escribe una función llamada `count_jabs` que reciba una lista de strings con los nombres de los golpes lanzados. La función debe contar y retornar (return) el número total de veces que se ejecutó el golpe `"Jab"`.

**Entrada de ejemplo:**

```python
training_round = ["Jab", "Cross", "Hook", "Jab", "Uppercut", "Jab"]
total_jabs = count_jabs(training_round)
print(f"Total Jabs: {total_jabs}")
```

**Salida esperada:**

```text
Total Jabs: 3
```

### NIVEL DIFÍCIL (50 Puntos)

#### Reto D1: El Filtro de Admisión (Fila del Club)

Crea una función llamada `manage_queue` que reciba dos parámetros: una lista con nombres de invitados actuales y un string con el nombre de un nuevo invitado que desea ingresar.

1. Si el nuevo invitado **ya se encuentra en la lista**, significa que ya ingresó al lugar; por lo tanto, la función debe **eliminarlo de la lista**.
2. Si el nuevo invitado **no está en la lista**, se le permite el acceso y se le debe **agregar al puro inicio de la lista** (índice 0).

La función debe **modificar la lista original** y **retornar la longitud final de la lista.**

**Ejemplo de uso 1 (No estaba en lista):**

```python
queue = ["Alice", "Bob"]
length = manage_queue(queue, "Charlie")
print(queue, length) # Salida: ['Charlie', 'Alice', 'Bob'] 3
```

**Ejemplo de uso 2 (Ya estaba en lista):**

```python
queue = ["Alice", "Bob", "Charlie"]
length = manage_queue(queue, "Bob")
print(queue, length) # Salida: ['Alice', 'Charlie'] 2
```
