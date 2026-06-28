# 03: Tuples and Immutability

En las lecturas anteriores exploramos a fondo las listas y cómo podemos transformarlas a nuestro antojo (mutabilidad). Sin embargo, en el desarrollo de software, permitir que cualquier parte del código modifique los datos puede dar pie a errores graves de seguridad o lógica.

Aquí es donde entran las **Tuplas**, las primas inmutables de las listas.

---

## 1. ¿Qué es una Tupla?

Una tupla es una colección ordenada de elementos que, a diferencia de las listas, **no se puede modificar una vez creada**.

- **Sintaxis:** Se definen utilizando paréntesis `()` en lugar de corchetes `[]`, separando los elementos con comas.
- **Acceso:** Al igual que las listas, indexan sus elementos empezando en `0` y soportan índices negativos.

```python
# Creating a tuple
cardinal_directions = ("North", "South", "East", "West")

# Reading elements (exactly like lists)
print(cardinal_directions[0])  # Output: North
print(cardinal_directions[-1]) # Output: West

# Measuring length
print(len(cardinal_directions)) # Output: 4
```

## 2. Inmutabilidad

La característica reina de las tuplas es que son inmutables. Si intentas añadir, cambiar o eliminar un elemento, tu programa fallará inmediatamente.

```python
system_config = ("192.168.1.1", 8080)

# Attempting to modify an element
# system_config[1] = 9090
# ❌ CRASHES! TypeError: 'tuple' object does not support item assignment

# Attempting to delete an element
# del system_config[0]
# ❌ CRASHES! TypeError: 'tuple' object doesn't support item deletion
```

### 3. ¿Para qué sirve una Tupla si las listas hacen más cosas?

Es la pregunta más común al empezar. ¿Por qué querríamos una estructura que nos limita? Hay tres razones fundamentales en la ingeniería de software:

1. **Seguridad de los Datos (Data Safety):** Si tu programa maneja datos constantes que nunca deberían cambiar durante la ejecución (como las coordenadas GPS de una base, los días de la semana o configuraciones de un servidor), usar una tupla le garantiza a otros desarrolladores que esos datos son de "solo lectura" y están protegidos.

2. **Rendimiento (Performance):** Bajo el capó, Python procesa las tuplas mucho más rápido que las listas. Como las listas pueden crecer o encogerse, Python debe reservar espacio extra dinámico en la memoria RAM. Las tuplas, al tener un tamaño fijo, se guardan en bloques de memoria optimizados y ligeros.

3. **Llaves de Diccionarios:** En la próxima semana aprenderás sobre diccionarios. Debido a que las tuplas son inmutables, Python puede calcularles una firma única de seguridad (hash), lo que les permite ser usadas como llaves de acceso, algo que las listas jamás podrán hacer.

## 4. Métodos Comunes (Solo Lectura)

Como no puedes alterar una tupla, no existen métodos como .append(), .pop() o .remove(). Solo contamos con métodos de exploración y búsqueda:

- `.count(value)`: Cuenta cuántas veces aparece un valor exacto en la tupla.

- `.index(value)`: Busca un valor de izquierda a derecha y devuelve el primer índice donde lo encontró. (Arroja ValueError si el elemento no existe).

```python
responses = ("Yes", "No", "Yes", "Maybe", "Yes")

print(responses.count("Yes")) # Output: 3
print(responses.index("Maybe")) # Output: 3
```

## Retos Cortos

### 1. El Hack de la Lista Mutada

Analiza el siguiente código con atención. ¿Crees que fallará o se ejecutará con éxito?

```python
special_tuple = (10, [20, 30], 40)
special_tuple[1][0] = 99
print(special_tuple)
```

<details>
<summary>💡 Ver Solución</summary>

- **Resultado:** Se ejecuta con éxito y muestra: `(10, [99, 30], 40)`

**Explicación:** ¡Este es un caso avanzado! La tupla es inmutable y no puede cambiar qué elementos tiene guardados en sus posiciones. En la posición `1`, tiene guardada una lista. La tupla no cambió (sigue teniendo la misma lista en la misma dirección de memoria), pero la lista en su interior sí es mutable, por lo que sus sub-elementos internos sí pudieron ser alterados sin romper la regla de la tupla.

</details>

---

## Retos de Código

### Challenge 1: Rock, Paper, Scissors Simulator (vs. Computer)

**Problema:** Escribe una función llamada `play_rock_paper_scissors` que simule una partida interactiva contra la computadora.

**Reglas del juego:**

- Al ejecutar la función, el programa debe solicitar al usuario mediante `input()` que elija una opción ingresando un número entero (`1: Piedra`, `2: Papel`, `3: Tijera`).
- **Validación de errores:** Si el usuario ingresa un número fuera del rango válido (menor a 1 o mayor a 3), el programa debe mostrar un mensaje de error claro y terminar la ejecución inmediatamente.
- La computadora debe elegir su opción de forma completamente aleatoria utilizando una lista interna que guarde los tres estados posibles.
- El programa debe imprimir en pantalla la elección de ambos y declarar un ganador o si ocurrió un empate.

- **Ejemplo de Flujo:**
  - Elige una opción (1: Piedra, 2: Papel, 3: Tijera): `2`
  - Tú elegiste: Papel
  - La computadora eligió: Piedra
  - **Resultado:** ¡Ganaste! Papel envuelve a Piedra.

<details>
<summary>💻 Ver Código de Solución</summary>

```python
import random

def play_rock_paper_scissors():
    # We use a tuple to map numbers to string values via indices
    options = ("Rock", "Paper", "Scissors")

    # 1. Get user input
    user_input = int(input("Choose an option (1: Rock, 2: Paper, 3: Scissors): "))

    # 2. Validate input boundaries
    if user_input < 1 or user_input > 3:
        print("Error: Invalid choice. You must enter 1, 2, or 3.")
        return # Early exit

    # Get the string based on user index choice (adjusting for 0-based indexing)
    user_choice = options[user_input - 1]

    # 3. Computer makes a random choice from the tuple
    computer_choice = random.choice(options)

    print(f"\nYour choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")

    # 4. Evaluate game conditions
    if user_choice == computer_choice:
        print("Result: It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        print(f"Result: You win! {user_choice} beats {computer_choice}.")
    else:
        print(f"Result: You lose! {computer_choice} beats {user_choice}.")

# Running the game
play_rock_paper_scissors()
```

</details>

### Challenge 2: Boxing Combination Creator I

**Problema:** En los entrenamientos de boxeo, los entrenadores diseñan combinaciones de golpes al azar para poner a prueba los reflejos de los atletas. Escribe una función llamada `generate_boxing_combo` que automatice este proceso.

**Reglas:**

- La función debe recibir un parámetro opcional llamado `max_punches` que determine cuántos golpes tendrá la combinación final. Por defecto, su valor debe ser 4.
- Internamente, debes tener una tupla que contenga los cuatro golpes básicos del boxeo: `"Jab", "Cross", "Hook" y "Uppercut"`.
- La función debe construir una nueva tupla con la secuencia ordenada de golpes aleatorios.
- Finalmente, la función debe **devolver** la combinación final.
- **Ejemplo de ejecución:** `generate_boxing_combo(3)`
- **Retorno esperada:** `["Jab", "Hook", "Cross"]`

<details>
<summary>💻 Ver Código de Solución</summary>

```python
import random

def generate_boxing_combo(max_punches = 4):
    basic_punches = ("Jab", "Cross", "Hook", "Uppercut")
    final_combination = []

    # Loop exactly the amount of times requested by parameters
    for _ in range(max_punches):
        random_punch = random.choice(basic_punches)
        # We accumulate the choices inside our list container
        final_combination.append(random_punch)

    return final_combination

# Testing standard and custom sizes
print(generate_boxing_combo())  # Generates 4 punches
print(generate_boxing_combo(6)) # Generates 6 punches
```

</details>

### Challenge 3: Boxing Combination Creator II (Avanzado)

Problema: Una combinación de boxeo estática no es realista; un verdadero peleador necesita moverse. Vamos a evolucionar la función anterior creando `generate_advanced_boxing_combo`.

**Reglas:**

- La función ahora debe aceptar dos parámetros opcionales con valores predeterminados:
- `max_punches`: Cantidad de golpes totales (por defecto `4`).
- `footwork_moves`: Cantidad de desplazamientos de pies a integrar (por defecto `1`).
- Debes contar con dos tuplas de referencia en el código local: una para los golpes básicos y otra para los tipos de desplazamientos (por ejemplo: `"Paso adelante"`, `"Paso atrás"`, `"Pivote izquierdo"`, `"Paso lateral derecho"`).
- **El reto de inserción:** Primero, construye la lista final con los golpes aleatorios solicitados. Después, agrega la cantidad de desplazamientos indicada por `footwork_moves`, finalmente mezcla la lista para que los golpes y desplazamientos estén distribuidos aleatoriamente.
  > [!NOTE]
  > Para mezclar la lista, puedes usar el método `random.shuffle()` que reordena los elementos de una lista de manera aleatoria.
- Devuelve la combinación final.
- **Ejemplo de ejecución:** `generate_advanced_boxing_combo(3, 2)`
- **Retorno esperado:** `["Jab", "Paso atrás", "Hook", "Pivote izquierdo", "Cross"]`

<details>
<summary>💻 Ver Código de Solución</summary>

```python
import random

def generate_advanced_boxing_combo(max_punches = 4, footwork_moves = 1):
    basic_punches = ["Jab", "Cross", "Hook", "Uppercut"]
    movements = ["Step Forward", "Step Backward", "Left Pivot", "Right Side-Step"]

    combination = []

    # Step 1: Generate and append the initial punches
    for _ in range(max_punches):
        random_punch = random.choice(basic_punches)
        combination.append(random_punch)

    # Step 2: Generate and append the footwork
    for _ in range(footwork_moves):
        random_move = random.choice(movements)
        combination.append(random_move)

    # Step 3: Shuffle the combination to mix punches and movements
    random.shuffle(combination)


    return combination

# Testing advanced integration
print(generate_advanced_boxing_combo())        # 4 punches, 1 movement mixed in
print(generate_advanced_boxing_combo(3, 2))     # 3 punches, 2 movements mixed in
```

</details>
