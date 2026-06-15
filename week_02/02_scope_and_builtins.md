# 02: Variable Scope and Built-in Tools

En esta lectura aprenderás dónde viven tus variables y cuánto tiempo duran en la memoria del computador (**Scope**). Además, añadiremos dos herramientas nativas muy poderosas a tu cinturón de herramientas: la función **`range()`** y la librería **`random`**.

---

## 1. Alcance de Variables (Variable Scope)

El **Scope** (alcance) se refiere a la región de un programa donde una variable es visible y puede ser utilizada. En Python existen dos alcances principales que debes dominar:

### Alcance Global (Global Scope)

Una variable declarada fuera de cualquier función es **global**. Puede ser leída desde cualquier parte de tu archivo, incluso dentro de las funciones.

```python
# Global variable
game_title = "CyberQuest"

def play_game():
    # We can read the global variable inside the function without issues
    print(f"Starting {game_title}...")

play_game() # Output: Starting CyberQuest...
```

### Alcance Local (Local Scope)

Una variable declarada dentro de una función es local. Solo existe mientras la función se esté ejecutando. Una vez que la función termina (return), esa variable es destruida y borrada de la memoria.

```python
def calculate_bonus():
    # Local variable
    bonus_points = 500
    return bonus_points

# Trying to access the local variable from the outside
# print(bonus_points)
# ❌ CRASHES! NameError: name 'bonus_points' is not defined
```

## 2. La Función range()

En la Semana 1 aprendiste a usar el bucle `for` para recorrer las letras de un texto. ¿Pero qué pasa si quieres que un bucle for se repita exactamente 5 veces? Para eso usamos `range()`, una función nativa que genera una secuencia de números.

Su sintaxis tiene tres variantes:

### Variante 1: `range(stop)`

Genera números desde el 0 hasta el número anterior al stop (el límite es exclusivo).

```python
# Loops 3 times: 0, 1, 2
for i in range(3):
    print(f"Iteration: {i}")
```

### Variante 2: `range(start, stop)`

Tú decides dónde empieza y dónde termina.

```python
# Loops from 5 to 9 (10 is excluded)
for number in range(5, 10):
    print(number)
```

### Variante 3: `range(start, stop, step)`

El tercer parámetro determina el "salto" o incremento entre cada número.

```python
# Even numbers from 2 to 8 (10 is excluded)
for even in range(2, 10, 2):
    print(even) # Output: 2, 4, 6, 8
```

### 3. La Librería `random`

Python viene con un ecosistema de módulos nativos listos para usar (la filosofía "Batteries Included"). Para utilizarlos, primero debemos importarlos al inicio de nuestro archivo usando la palabra `import`.

- La librería random nos permite generar aleatoriedad, algo indispensable para videojuegos, simulaciones o pruebas. Su función más común para principiantes es `random.randint(a, b)`.

```python
import random

# Generates a random integer between 1 and 10 (inclusive!)
secret_number = random.randint(1, 10)

print(f"The computer chose: {secret_number}")
```

> [!Note]
> En `range(1, 10)`, el 10 está excluido (llega al 9).
> En `random.randint(1, 10)`, el 10 está incluido (puede salir un 10).

## Retos Cortos

1. **El Conflicto de Nombres**

¿Qué se imprimirá en la consola al ejecutar el siguiente código?

```python
value = 10

def alter_value():
    value = 5
    return value

alter_value()
print(value)
```

<details>
<summary>💡 Ver Solución</summary>

- **En la consola se imprimirá:** `10`

**Explicación:** La variable `value = 5` creada dentro de la función es una variable local completamente nueva. Aunque comparte el mismo nombre que la variable global, vive en una "caja" diferente. La ejecución de la función no alteró el valor de la variable global externa.

</details>

---

2. **El Contador Invertido con range**

¿Qué números exactos imprimirá este bucle en la consola?

```python
for step in range(5, 1, -1):
    print(step)
```

<details>
<summary>💡 Ver Solución</summary>

- **En la consola se imprimirá:** `5, 4, 3, 2`

**Explicación:** Al usar un `step` negativo (`-1`), el rango se genera en cuenta regresiva. Comienza en el start (`5`) y se detiene justo antes del `stop` (`1`), por lo que el `1` queda excluido de la serie.

</details>

---

3. **El Rango Imposible**

¿Cuántas veces se ejecutará el bloque de código dentro de este bucle for?

```python
for item in range(10, 5):
    print("Running...")
```

<details>
<summary>💡 Ver Solución</summary>

- **Resultado:** `0` veces (no imprimirá nada).

**Explicación:** Por defecto, `range()` asume un incremento positivo de `+1`. Como el inicio (`10`) ya es mayor que el límite de parada (`5`), Python detecta que la secuencia está vacía desde el primer segundo y salta el ciclo por completo.

</details>

## Retos de Código

### Challenge 1: The Custom Dice Roller

**Problema:** Escribe una función llamada `roll_dice` que simule el lanzamiento de un dado de múltiples caras.

- Debe recibir un parámetro llamado `sides` que represente el número de caras del dado.
- **Configuración por defecto:** Si no se le pasa ningún argumento al llamar a la función, `sides` debe valer `6` por defecto.
- La función debe **retornar (return)** un número aleatorio entero entre `1` y el valor de `sides` (inclusive).

- **Ejemplo de ejecución:**

  ```python
  print(roll_dice())    # Rolls a 6-sided dice (returns between 1 and 6)
  print(roll_dice(20))  # Rolls a 20-sided dice (returns between 1 and 20)
  ```

<details>
<summary>💡 Ver Solución</summary>

```python
import random

def roll_dice(sides=6):
    # random.randint includes both limits
    return random.randint(1, sides)

# Testing the function
default_roll = roll_dice()
rpg_roll = roll_dice(20)

print(f"Standard dice: {default_roll}")
print(f"D&D 20-sided dice: {rpg_roll}")
```

</details>

---

### Challenge 2: The Star Pyramid Builder

**Problema:** Escribe una función llamada `print_pyramid` que dibuje una media pirámide de asteriscos en la consola utilizando bucles.

- Debe recibir un parámetro opcional llamado `height` para definir la altura (número de filas) de la pirámide.
- **Configuración por defecto:** Si no se pasa un valor, la altura debe ser `5`.
- _Pista_: En Python puedes multiplicar un string por un número entero para repetirlo (por ejemplo: `"*" * 3` da como resultado `"***"`). Combina esto con un bucle for y range().

Ejemplo de ejecución: `print_pyramid(4)`

Salida esperada:

```python
*
**
***
****
```

<details>
<summary>💡 Ver Solución</summary>

```python
def print_pyramid(height=5):
    # We use height + 1 because the stop value in range() is exclusive
    for i in range(1, height + 1):
        print("*" * i)

# Testing the function
print("--- Pyramid 1 (Default) ---")
print_pyramid()

print("\n--- Pyramid 2 (Custom Height 3) ---")
print_pyramid(3)
```

</details>

---

### Challenge 3: The Customizable Guessing Game

**Problema:** ¡Vamos a construir el juego de adivinar el número con máxima flexibilidad! Escribe una función llamada `play_guessing_game` que reciba dos parámetros opcionales:

1. `max_attempts`: El número de oportunidades que tiene el usuario (entero, por defecto `5`).
2. `max_num`: El número límite superior para el rango del número secreto (entero, por defecto `100`).

Reglas del juego:

- La función debe generar un número secreto aleatorio entre 1 y `max_num`.
- Usando un bucle interactivo, solicitará números al usuario mediante `input()`.
- Si el usuario adivina, el juego imprime `"Correct! You win!"` y termina.
- Si el usuario falla, el programa debe responder únicamente si el número secreto es mayor (`Higher`) o menor (`Lower`) que el intento del usuario, restar un intento y continuar.
- El juego termina de forma definitiva cuando el usuario adivina el número o se queda completamente sin intentos.

<details>
<summary>💡 Ver Solución</summary>

```python
import random

def play_guessing_game(max_attempts = 5, max_num = 100):
    SECRET_NUMBER = random.randint(1, max_num)
    user_attempts = max_attempts

    print(f"I'm thinking of a number between 1 and {max_num}. You have {user_attempts} attempts remaining!")

    while(user_attempts > 0):
        guess = int(input("Enter your guess: "))

        if guess == SECRET_NUMBER:
            print("Correct! You win!")
            return True;
        elif guess < SECRET_NUMBER:
            print("HIGHER")
        else:
            print("LOWER")

        user_attempts -= 1
        print(f"Attempts left: {user_attempts}")

    print(f"GAME OVER, the secret number was: {SECRET_NUMBER}")
    return False;
```

</details>
