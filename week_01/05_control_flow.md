# 05: Control Flow (Conditionals and Loops)

Por defecto, la computadora ejecuta tu código de forma secuencial: de arriba a abajo, línea por línea. El **Control de Flujo** (Control Flow) es lo que nos permite romper esa estructura lineal para que el programa tome decisiones o repita bloques de código según ciertas condiciones.

---

## 1. La Regla de Oro: Indentación (Indentation)

A diferencia de otros lenguajes de programación que usan llaves `{}` para agrupar bloques de código, Python utiliza espacios en blanco conocidos como **indentación**.

- Cada vez que inicias una estructura de control (como un `if` o ciclo), debes terminar la línea con dos puntos (`:`).
- La siguiente línea y todas las que pertenezcan a ese bloque **deben tener exactamente 4 espacios de sangría**.

```python
# Correct indentation
if True:
    print("This is inside the block")
    print("This is also inside the block")

print("This is outside the block (back to the main flow)")
```

> [!WARNING]
> Si mezclas espacios o no indentas correctamente, Python lanzará un error llamado `IndentationError` y el programa no correrá.

## 2. Condicionales (if, elif, else)

Los condicionales le permiten a tu programa tomar caminos diferentes según si una expresión se evalúa como `True` o `False`.

- `if`: Es el punto de partida. Se ejecuta solo si la condición es verdadera.
- `elif` (abreviatura de else if): Te permite evaluar una nueva condición si las anteriores fueron falsas. Puedes usar tantos como necesites.
- `else`: Es el camino por defecto. Se ejecuta si absolutamente todas las condiciones anteriores resultaron falsas.

### Ejemplo Práctico

```python
age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
```

## 3. Ciclos (Loops)

Los ciclos te permiten repetir un bloque de código múltiples veces sin tener que reescribirlo.

### while Loop

Repite el bloque de código mientras una condición lógica se mantenga como `True`. Es vital asegurarte de que la condición cambie en algún momento dentro del ciclo; de lo contrario, crearás un ciclo infinito que congelará tu programa.

```python
# Printing numbers from 1 to 5
counter = 1

while counter <= 5:
    print(f"Number: {counter}")
    counter += 1  # Increment counter to prevent an infinite loop

print("Loop finished!")
```

### For Loop

Se utiliza para iterar sobre una secuencia (como los caracteres de una cadena de texto o elementos de una colección). En lugar de depender de una condición abierta, se ejecuta una cantidad fija de veces basada en la secuencia.

```python
# Iterating over a string
message = "CODE"

for letter in message:
    print(f"Current letter: {letter}")
```

### ¿Cómo saber qué ciclo utilizar?

Elegir el ciclo correcto hará que tu código sea más limpio, legible y eficiente. Aquí tienes una guía rápida para tomar la decisión:

| **Tipo de Ciclo** |                                                      **¿Cuándo usarlo?**                                                       |                                            **Ejemplo**                                            |
| :---------------: | :----------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------: |
|       `for`       |         Cuando sabes de antemano cuántas veces se debe repetir el código (un número fijo o el tamaño de la colección)          |                                 Imprimir los números del 1 al 100                                 |
|      `while`      | Cuando no sabes cúantas veces se repetirá. Depende enteramente de una condición externa que puede cambiar en cualquier momento | El ciclo principal de un videojuego: Mientras el jugador tenga vidas suficientes que siga jugando |
|                   |                                                                                                                                |                                                                                                   |

## Retos de Código

### Challenge 1: FizzBuzz

**Problema:** Escribe un programa usando un bucle que evalúe los números del 1 al 15 uno por uno.

- Si el número es divisible por `3`, debe imprimir `"Fizz"`.
- Si el número es divisible por `5`, debe imprimir `"Buzz"`.
- Si es divisible por ambos (`3` y `5`), debe imprimir `"FizzBuzz"`.
- Si no es divisible por ninguno, debe imprimir el número normal.

<details>
<summary>💡 Ver Solución</summary>

```python
number = 1

while number <= 15:
    # Check the combined condition first!
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

    number += 1
```

> [!NOTE]
> También es posible hacerlo con un ciclo `for`

</details>

---

### Challenge 2: Calculadora de Promedios

**Problema:** Un profesor necesita calcular el promedio final de calificaciones de su grupo, pero nunca sabe cuántos alumnos asistieron al examen. Escribe un programa que pida de forma continua las calificaciones (números flotantes) de los alumnos.

- El programa debe detenerse inmediatamente cuando el profesor introduzca una calificación de `-1`.
- Al detenerse, el programa debe calcular y mostrar el promedio exacto del grupo.
- _Validación extra:_ Si el profesor introduce `-1` al primer intento, el programa debe avisar que no se ingresaron calificaciones en lugar de intentar dividir por cero.

- **Ejemplo de Flujo:**
  - Enter student grade (or -1 to stop): `8.5`
  - Enter student grade (or -1 to stop): `9.0`
  - Enter student grade (or -1 to stop): `7.5`
  - Enter student grade (or -1 to stop): `-1`
  - **Salida:** `The class average is: 8.333333333333334`

<details>
<summary>💡 Ver Solución</summary>

```python
total_score = 0.0
student_count = 0

while True:
    score_input = float(input("Enter student grade (or -1 to stop): "))

    # Check for the exit condition
    if score_input == -1:
        break

    # Accumulate the total score and increment the student counter
    total_score += score_input
    student_count += 1

# Prevent division by zero if no grades were entered
if student_count > 0:
    average = total_score / student_count
    print(f"The class average is: {average}")
else:
    print("No grades were entered.")
```

</details>

---

### Challenge 5: Simulador de Cajero Automático

**Problema:** Escribe un programa que simule un cajero automático básico. El usuario comenzará con un saldo inicial fijo de $100.0 dólares. Utilizando un bucle `while True`, el programa debe solicitar continuamente al usuario qué acción desea realizar: `"deposit"`, `"withdraw"` o `"exit"`.

- Si elige `"deposit"`, el programa debe pedir la cantidad a depositar y sumarla al saldo actual.
- Si elige `"withdraw"`, el programa debe pedir la cantidad a retirar. _Validación importante_: Si la cantidad a retirar es mayor que el saldo actual, debe mostrar un mensaje de `"Insufficient funds!"` y no restar nada. Si tiene suficiente dinero, realiza el retiro.
- Si elige `"exit"`, el programa debe despedirse, mostrar el saldo final y romper el bucle para terminar.
- Si introduce cualquier otra palabra, debe avisar que es una opción inválida y volver a mostrar el menú.

**Ejemplo de Flujo:**

1. Current Balance: $100.0
2. Choose action (deposit/withdraw/exit): withdraw
3. Enter amount to withdraw: 150.0
4. -> Output: Insufficient funds!
5. Choose action (deposit/withdraw/exit): deposit
6. Enter amount to deposit: 50.0
7. Choose action (deposit/withdraw/exit): exit
8. -> Output: Thank you! Your final balance is: $150.0

<details>
<summary>💡 Ver Solución</summary>

```python
balance = 100.0

print("--- Welcome to the Pocket ATM ---")

while True:
    print(f"\nYour current balance is: ${balance}")
    action = input("Choose an action (deposit/withdraw/exit): ").lower()

    if action == "deposit":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Successfully deposited ${amount}")

    elif action == "withdraw":
        amount = float(input("Enter amount to withdraw: "))
        # Validation to prevent negative balance
        if amount > balance:
            print("Error: Insufficient funds!")
        else:
            balance -= amount
            print(f"Successfully withdrew ${amount}")

    elif action == "exit":
        print(f"Thank you for using Pocket ATM. Your final balance is: ${balance}")
        break  # Exit the loop

    else:
        print("Invalid action. Please type 'deposit', 'withdraw', or 'exit'.")
```

</details>

## Retos en Plataformas Externas (Codewars & LeetCode)

Para terminar la semana, medirás tus habilidades en plataformas reales utilizadas en la industria para entrevistas técnicas.

> [!WARNING]
> En estas plataformas no usarás `input()` ni `print()`. Las plataformas te entregarán los datos automáticamente dentro de los paréntesis de una función (`def`) y esperarán que tu programa devuelva el resultado usando la palabra reservada **`return`** en lugar de mostrarlo en pantalla.

---

### 1. Codewars: Even or Odd (8 kyu)

- **Enlace:** [Even or Odd on Codewars](https://www.codewars.com/kata/53da3dbb4a5168369a0000fe)
- **Problema:** Crea una función que tome un número entero como argumento y devuelva `"Even"` para los números pares o `"Odd"` para los números impares.

<details>
<summary>💡 Ver Pista</summary>

Usa el operador módulo (`% 2`) dentro de una estructura `if/else` elemental.

</details>

<details>
<summary>💻 Ver Código de Solución</summary>

```python
def even_or_odd(number):
    # Check if the number is divisible by 2
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
```

</details>

---

### 2. Codewars: Quarter of the Year (8 kyu)

- **Enlace:** [Quarter of the year on Codewars](https://www.codewars.com/kata/5ce9c1000bab0b001134f5af)
- **Problema:** Dado un mes del 1 al 12 (como entero), devuelve a qué trimestre (quarter) del año pertenece como un número entero del 1 al 4.

<details>
<summary>💻 Ver Código de Solución</summary>

```python
def quarter_of(month):
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    else:
        return 4

# Alternative mathematical solution:
# def quarter_of(month):
#     return (month + 2) // 3   return 4
```

</details>

---

### 3. LeetCode 9: Palindrome Number (Easy)

- **Enlace:** 9. [Palindrome Number on LeetCode](https://leetcode.com/problems/palindrome-number/)
- **Problema:** Dado un número entero x, devuelve True si x es un palíndromo (se lee igual al derecho y al revés) y False en caso contrario. Ejemplo: 121 es True, -121 es False.

<details>
<summary>💻 Ver Código de Solución</summary>

```python
def isPalindrome(x):
    # Convert integer to string
    text_number = str(x)
    reversed_text = ""

    # Reverse the string manually using a loop
    for character in text_number:
        reversed_text = character + reversed_text

    # Compare original string with reversed string
    return text_number == reversed_text
```

</details>
