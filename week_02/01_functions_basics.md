# 01: Functions Basics

En la primera semana escribiste scripts que se ejecutaban de principio a fin. Sin embargo, a medida que tus programas crecen, repetir el mismo bloque de código una y otra vez se vuelve insostenible. Aquí es donde entran las **Funciones**.

Una función es un bloque de código organizado y reutilizable que está diseñado para realizar una sola tarea específica.

---

## 1. Sintaxis de una Función

Para crear (declarar) una función en Python, utilizamos la palabra reservada **`def`** (short for _define_), seguida del nombre de la función, paréntesis `()` y dos puntos `:`.

Al igual que con las estructuras de control de la semana pasada, todo el código dentro de la función **debe estar indentado con 4 espacios**.

```python
# 1. Defining the function
def say_hello():
    # Inside the function body
    print("Welcome to Week 2!")
    print("Let's learn functions.")

# 2. Calling (executing) the function
say_hello()
say_hello()  # We can reuse it as many times as we want
```

> [!NOTE]
> Si ejecutas ese código, el texto se imprimirá dos veces. Si defines la función pero nunca la llamas (usando su nombre con paréntesis), el código dentro de ella nunca se ejecutará.

## 2. Parámetros vs Argumentos

Para que una función sea verdaderamente útil, debe ser capaz de recibir datos dinámicos para procesarlos. Aquí es donde entran estos dos conceptos que suelen confundirse, pero que representan momentos diferentes:

- **Parámetro (Parameter):** Es la variable de la plantilla. Se escribe dentro de los paréntesis al definir la función. Funciona como un "espacio reservado".
- **Argumento (Argument):** Es el valor real que le pasas a la función cuando la llamas.

```python
# 'name' is the PARAMETER (the placeholder)
def greet_user(name):
    print(f"Hello, {name}!")

# "Alice" and "Bob" are the ARGUMENTS (the actual data)
greet_user("Alice")
greet_user("Bob")
```

## 3. El Gran Debate: print() vs return

Este es el obstáculo más grande para los principiantes. Es muy común pensar que `print()` y `return` hacen lo mismo porque ambos pueden mostrar resultados en la consola durante las pruebas, pero operan de formas completamente distintas en la memoria.

|                        |                              **print**                               |                                **return**                                |
| :--------------------: | :------------------------------------------------------------------: | :----------------------------------------------------------------------: |
|      **Objetivo**      |                  Mostrar información al ojo humano                   |              Enviar un valor de vuelta al programa/sistema               |
| **Impacto en Memoria** |   No guarda nada. El valor se imprime y desaparece para el código    |   Detiene la función y "transforma" la llamada en el valor resultante    |
|   **Reutilizacion**    | El resultado no se puede guardar en una variable para usarlo después | El resultado si se puede almacenar en una variable o pasar a una función |

### Ejemplo de error clásico

Imagina que quieres una función que sume dos números y luego quieres multiplicar ese resultado por 2 de manera externa.

```python
# APPROACH A: Using print()
def add_with_print(a, b):
    print(a + b)

# APPROACH B: Using return
def add_with_return(a, b):
    return a + b

# Testing Approach A
result_a = add_with_print(5, 5)  # Console shows: 10
# final_a = result_a * 2          # ❌ CRASHES! TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'

# Testing Approach B
result_b = add_with_return(5, 5) # Console shows: nothing (it's silent)
final_b = result_b * 2           #  WORKS! final_b now holds 20
print(f"The final math is: {final_b}")
```

## Retos Cortos

Pon a prueba tu comprensión de los flujos de datos antes de ver las respuestas.

1. **El Retorno Invisible**

¿Qué valor se guardará en la variable output y qué se mostrará en la consola al ejecutar este código?

```python
def multiply(a, b):
    result = a * b

output = multiply(3, 4)
print(output)
```

<details>
<summary>💡 Ver Solución</summary>

- **En la consola se imprimirá:** `None`

**Explicación:** En Python, si una función no tiene una sentencia `return` explícita, la función siempre devuelve `None` de forma automática al terminar. Aunque la multiplicación se calculó internamente en la variable `result`, ese valor se quedó encerrado dentro y nunca salió de la función.

</details>

---

2. **La Línea Fantasma**

¿Qué se imprimirá en la consola al ejecutar la función `check_status`?

```python
def check_status():
    print("Step 1")
    return "Status OK"
    print("Step 2")

final_status = check_status()
```

<details>
<summary>💡 Ver Solución</summary>

- **En la consola se imprimirá:** `Step 1`

**Explicación:** La palabra reservada `return` tiene un superpoder: detiene inmediatamente la ejecución de la función. En cuanto Python lee `return "Status OK"`, sale de la función y regresa al flujo principal del programa. La línea `print("Step 2")` es código muerto; nunca se ejecutará.

</details>

---

3. **Identificador de Componentes**

Mira el siguiente código. Identifica cuáles son los parámetros y cuáles son los argumentos.

```python
def calculate_area(width, height):
    return width * height

x = 10
y = 5
area = calculate_area(x, y)
```

<details>
<summary>💡 Ver Solución</summary>

- **Parámetros:** `width` y `height` (Son las variables molde definidas en la firma de la función en la línea 1).
- **Argumentos:** `x` y `y` (Son las variables reales con valores `10` y `5` que se le envían a la función al llamarla en la línea 6).

</details>

## Retos de Código

### Challenge 1: Calculadora de multas por exceso de velocidad

**Problema:** Escribe una función llamada `calculate_fine` que determine el costo de una multa por exceso de velocidad. La función debe recibir tres parámetros:

1. `speed`: La velocidad actual del conductor (entero).
2. `speed_limit`: El límite de velocidad de la zona (entero).
3. `is_school_zone`: Un booleano (`True`/`False`) que indica si es una zona escolar.

**Reglas de cálculo:**

- Si la velocidad es menor o igual al límite, la multa es `0`.
- Si excede el límite por 20 km/h o menos, la multa base es `50`.
- Si excede el límite por más de 20 km/h, la multa base es `150`.
- **Factor crítico:** Si `is_school_zone` es `True`, el valor total de la multa se debe duplicar.

La función **debe retornar (return)** el valor numérico de la multa final. Fuera de la función, llama a la función con diferentes datos e imprime el resultado.

- **Ejemplo de ejecución:** `calculate_fine(85, 60, True)` debería retornar `300` (excede por 25 km/h, multa base de 150, duplicada por zona escolar).

<details>
<summary>💡 Ver Solución</summary>

```python
def calculate_fine(speed, speed_limit, is_school_zone):
    fine = 0

    # Calculate base fine
    if speed <= speed_limit:
        fine = 0
    elif (speed - speed_limit) <= 20:
        fine = 50
    else:
        fine = 150

    # Apply school zone multiplier
    if is_school_zone:
        fine = fine * 2

    return fine
```

</details>
