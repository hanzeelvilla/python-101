# 03: Input, Output, and Operators

En esta lectura aprenderás a hacer que tus programas interactúen con el mundo exterior (recibiendo y mostrando datos) y a transformar esos datos utilizando diferentes tipos de operadores lógicos y matemáticos.

---

## 1. Entrada y Salida de Datos (Input & Output)

Hasta ahora, hemos escrito datos fijos en nuestras variables (valores _hardcoded_). Para hacer programas dinámicos, necesitamos comunicarnos con el usuario.

### Salida: `print()` y f-strings

Ya conoces `print()`, pero la forma más eficiente y moderna de mostrar variables junto con texto en Python es usando **f-strings** (formatted string literals). Solo debes agregar una `f` antes de las comillas y colocar las variables entre llaves `{}`.

```python
name = "Sam"
age = 22

# Using f-strings
print(f"Hello, {name}! Next year you will be {age + 1} years old.")
# Output: Hello, Sam! Next year you will be 23 years old.
```

### Entrada: input()

La función `input()` detiene la ejecución del programa y espera a que el usuario escriba algo en la consola y presione Enter.

> [!NOTE]
> La función `input()` siempre devuelve una cadena de texto (`string`), incluso si el usuario ingresa un número. Si necesitas un número, debes convertirlo usando `int()` o `float()`.

```python
# Receiving text
favorite_color = input("What is your favorite color? ")
print(f"Cool! I like {favorite_color} too.")

# Receiving numbers (Requires casting!)
user_age = input("Enter your age: ")
age_number = int(user_age) # Converting str to int
print(f"In 10 years you will be {age_number + 10}.")
```

## 2. Operadores Aritméticos

Son los símbolos que utilizas para realizar operaciones matemáticas básicas.

| **Operador** |           **Operación**            | **Ejemplo** | **Resultado** |
| :----------: | :--------------------------------: | :---------: | :-----------: |
|     `+`      |                Suma                |   10 + 5    |      15       |
|     `-`      |               Resta                |   10 - 5    |       5       |
|     `\*`     |           Multiplicación           |   10 \ 5    |      50       |
|     `/`      |              División              |   10 / 4    |      2.5      |
|     `//`     | División entera (ignora decimales) |   10 // 4   |       2       |
|     `%`      |  Módulo (residuo de la división)   |   10 % 3    |       1       |
|     `**`     |        Exponente (potencia)        |  2 \*\* 3   |       8       |

## 3. Operadores de Comparación

Se utilizan para comparar dos valores. El resultado de cualquier comparación siempre es un Booleano (`True` o `False`).

| **Operador** |     **Significado**     | **Ejemplo** | **Resultado** |
| :----------: | :---------------------: | :---------: | :-----------: |
|     `==`     |         Igual a         |   5 == 5    |     True      |
|     `!=`     | Diferente de/No igual a |   5 != 3    |     True      |
|     `>`      |        Mayor que        |   10 > 20   |     False     |
|     `<`      |        Menor que        |   10 < 20   |     True      |
|     `>=`     |    Mayor o igual que    |   5 >= 5    |     True      |
|     `<=`     |    Menor o igual que    |   8 <= 4    |     False     |

## 4. Operadores Lógicos

Permiten combinar múltiples comparaciones o booleanos. Python utiliza palabras en inglés muy intuitivas:

| **Operador** |                        **Descripción**                         |      **Ejemplo**      | **Resultado** |
| :----------: | :------------------------------------------------------------: | :-------------------: | :-----------: |
|    `and`     |     Devuelve True solo si ambas condiciones son verdaderas     | (5 > 3) and (10 < 20) |     True      |
|     `or`     | Devuelve True si al menos una de las condiciones es verdadera  | (5 > 3) or (10 < 20)  |     True      |
|    `not`     | Invierte el valor booleano actual (Si es True lo vuelve False) |     not (5 == 5)      |     False     |

## Retos cortos

1. **La Trampa del Input** ¿Qué pasará si ejecutas este código, ingresas el número 5 en la consola y presionas Enter?

```python
user_number = input("Enter a number: ")
result = user_number * 3
print(result)
```

<details>
<summary>💡 Ver Solución</summary>

- Resulltado: `555`

**Explicación:** Como `input()` devuelve un texto (`str`), la variable `user_number` vale `"5"`. En Python, multiplicar un string por un entero lo repite esa cantidad de veces. Para que diera `15`, tendrías que haber usado `int(user_number) \* 3`.

</details>

---

2. **Evaluación de Operadores** Determina si el resultado final de la variable final_check es `True` o `False`

```python
a = 10
b = 3

condition_1 = (a // b) == 3
condition_2 = (a % b) > 2

final_check = condition_1 and not condition_2
```

<details>
<summary>💡 Ver Solución</summary>

- Resulltado: `True`

**Explicación:**

1. `a // b` (División entera de 10 entre 3) es `3`. Por lo tanto, `3 == 3` es `True`. (`condition_1 = True`).
2. `a % b` (Residuo de 10 entre 3) es `1`. Por lo tanto, `1 > 2` es `False`. (`condition_2 = False`).
3. `not condition_2` invierte `False` a `True`.
4. `final_check = True and True`, lo cual da como resultado final `True`.

</details>

---

3. **El examen del validador** Imagina que ejecutas el siguiente código, el usuario ingresa primero el número `20` y luego el número `5`. ¿Cuál será el valor booleano final de la variable `result`?

```python
# Assume the user inputs "20" first, and then "5"
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

val1 = num1 + num2
val2 = int(num1) // int(num2)

result = (val1 == "205") and (val2 > 3)
```

<details>
<summary>💡 Ver Solución</summary>

- Resulltado: `True`

**Explicación:**

1. **La trampa del texto:** Como `input()` siempre recibe texto, `num1` almacena el string `"20"` y `num2` almacena el string `"5"`.
2. **Operación con texto (`val1`):** Al usar el operador `+` entre dos strings, Python los concatena (los une). Por lo tanto, `"20"` + `"5"` da como resultado el string `"205"`.
3. **Operación matemática (`val2`):** Aquí sí se hace un casting explícito a enteros con `int()`. La operación se transforma en `20 // 5` (división entera). El resultado es `4`.
4. **Evaluación final (`result`):**
   - **Primera condición:** `val1 == "205"` evaluará si `"205" == "205"`, lo cual es `True`.
   - **Segunda condición:** `val2 > 3` evaluará si `4 > 3`, lo cual es `True`.
   - **Combinación lógica:** `True and True` da como resultado final `True`.

</details>

## Retos de código

¡Es hora de escribir tus primeros scripts reales! Crea un archivo `.py` en tu entorno local para cada reto. Recuerda la regla de oro: **está prohibido usar herramientas que no hayamos visto todavía** (como condicionales `if/else`). Todo debe resolverse de forma lineal usando operaciones y lógica pura.

### Challenge 1: Calculadora de Propinas

**Problema:** Escribe un programa que ayude a las personas a calcular cuánta propina deben dejar en un restaurante y cuál es el total final a pagar. El script debe solicitar:

1. El total de la cuenta en la mesa.
2. El porcentaje de propina que desean dejar (por ejemplo: `10`, `15`, `20`, etc.).

Al final, debe mostrar en la consola el monto exacto de la propina y el total absoluto (cuenta + propina) usando f-strings.

- **Ejemplo de Entrada (Consola):** Enter the total bill: `80.0`
  - Enter the tip percentage: `15`
- **Ejemplo de Salida Esperada:** Tip amount: $12.0
  - Total to pay: $92.0

<details>
<summary>💡 Ver Solución</summary>

```python
# 1. Receive input from user and convert to float
bill_total = float(input("Enter the total bill: "))
tip_percentage = float(input("Enter the tip percentage (e.g., 10, 15, 20): "))

# 2. Calculate the tip amount (percentage / 100 * total)
tip_amount = bill_total * (tip_percentage / 100)

# 3. Calculate the grand total
final_total = bill_total + tip_amount

# 4. Output both results clearly
print(f"Tip amount: ${tip_amount}")
print(f"Total to pay: ${final_total}")
```

</details>

---

### Challenge 2: Conversor de Temperatura

**Problema:** Escribe un programa que le pida al usuario una temperatura en grados Celsius, la transforme a grados Fahrenheit y muestre el resultado en la consola usando f-strings.

- **Fórmula:** $F = (C \times 9/5) + 32$
- **Ejemplo de Entrada (Consola):** `25`
- **Ejemplo de Salida Esperada:** `25.0°C is equal to 77.0°F`

<details>
<summary>💡 Ver Solución</summary>

```python
# 1. Receive input from user and convert to float immediately
celsius_input = input("Enter temperature in Celsius: ")
celsius = float(celsius_input)

# 2. Apply the conversion formula
fahrenheit = (celsius * 9 / 5) + 32

# 3. Output the result using f-strings
print(f"{celsius}°C is equal to {fahrenheit}°F")
```

</details>

---

### Challenge 3: Generador de historias graciosas

**Problema:** Crea un juego de palabras donde el usuario introduzca diferentes tipos de palabras y el programa las use para rellenar los espacios en blanco de una historia corta y divertida. El script debe solicitar al usuario:

1. Un animal (plural).
2. Un adjetivo (una cualidad).
3. Un verbo (una acción en infinitivo).
4. Un lugar.

Al final, el programa debe mostrar la historia completa usando una sola f-string. ¡Asegúrate de que las respuestas del usuario encajen bien en el texto!

- **Ejemplo de Entrada (Consola):**
  - Enter an animal (plural): `monkeys`
  - Enter an adjective: `shiny`
  - Enter a verb: `code`
  - Enter a place: `the kitchen`
- **Ejemplo de Salida Esperada:**
  - `Story: Yesterday, 3 shiny monkeys decided to code inside the kitchen!`

<details>
<summary>💡 Ver Solución</summary>

```python
# 1. Receive text inputs from the user (No casting needed since input() returns a string!)
animals = input("Enter an animal (plural): ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")
place = input("Enter a place: ")

# 2. Construct and print the story using a single f-string
print("\n--- Your Story ---")
print(f"Yesterday, 3 {adjective} {animals} decided to {verb} inside {place}!")
```

</details>
