# 02: Variables and Data Types

En este archivo aprenderás cómo almacena información una computadora, cómo comunicarte con el código usando comentarios y cómo transformar un tipo de dato en otro. Estos son los bloques de construcción fundamentales de cualquier programa.

---

## 1. Comentarios (Comments)

Un comentario es una nota para ti mismo o para otros desarrolladores. El intérprete de Python ignora por completo los comentarios; no se ejecutan como código.

En Python, los comentarios se crean usando el símbolo `#`.

```python
# This is a single-line comment
# The computer will ignore this completely

score = 100  # You can also write comments at the end of a line

# Use comments to explain WHY you wrote the code,
# not WHAT the code does if it is already obvious.
```

---

## 2. Variables

Imagina una variable como una caja con una etiqueta en la memoria de la computadora. Puedes guardar un valor dentro de esa caja y usar la etiqueta (el nombre de la variable) para hacer referencia a ese valor más tarde.

En Python, creas una variable simplemente asignándole un valor con el operador `=`.

```python
# Creating variables
player_name = "Alex"
player_health = 100
gold_coins = 45.5

# Using variables
print(player_name)
print(player_health)
```

### Reglas para nombrar variables (Naming Rules)

- Deben empezar con una letra o un guion bajo (\_).
- Solo pueden contener caracteres alfanuméricos y guiones bajos (a-z, A-Z, 0-9, y \_).
- Son sensibles a mayúsculas y minúsculas (age, Age y AGE son tres variables diferentes).
- Por convención en Python, se usa el estilo [snake_case](https://en.wikipedia.org/wiki/Snake_case) (letras minúsculas separadas por guiones bajos, por ejemplo: user_serial_number).

## 3. Tipos de Datos Nativos (Data Types)

Python es un lenguaje de tipado dinámico. Esto significa que no tienes que declarar explícitamente qué tipo de dato va a guardar una variable; Python lo deduce automáticamente por el valor que le asignas.

Los cuatro tipos de datos más básicos y esenciales son:

### Integers (int)

Números enteros, tanto positivos como negativos, sin decimales.

```python
items_count = 5
temperature = -12
year = 2026
```

### Floats (float)

Números reales que contienen uno o más decimales.

```python
price = 19.99
pi_value = 3.14159
negative_float = -0.5
```

### Strings (str)

Cadenas de texto. Deben ir encerradas entre comillas simples (`'`) o dobles (`"`).

```python
greeting = "Hello, world!"
username = 'coder_123'
empty_string = ""
```

### Booleans (bool)

Solo pueden tener dos valores: True (Verdadero) o False (Falso). Nota que la primera letra debe ser mayúscula.

```python
is_game_over = False
has_permission = True
```

> [!NOTE]
> Si alguna vez quieres saber qué tipo de dato tiene una variable en tiempo de ejecución, puedes usar la función nativa `type()`.

## 4. Conversión de Tipos (Type Casting)

Habrá situaciones en las que necesites transformar una variable de un tipo de dato a otro. A esto se le conoce como Type Casting. Python nos provee de funciones nativas para lograrlo de forma explícita:

- `int()` - Convierte a entero.
- `float()` - Convierte a decimal.
- `str()` - Convierte a texto.
- `bool()` - Convierte a booleano.

## Retos Cortos

Intenta resolver estos pequeños retos directamente en un archivo de pruebas local o anotando tus respuestas antes de pasar a la siguiente lectura:

1. **¿Válido o Inválido?** Identifica cuáles de los siguientes nombres de variables son válidos en Python:

- `1st_player`
- `player_1`
- `player-1`
- `_secret_key`
- `print`

<details>
<summary>💡 Ver Solución</summary>

- `1st_player`: **Inválido** (No puede empezar con un número).
- `player_1`: **Válido**.
- `player-1`: **Inválido** (No puede contener guiones medios `-`).
- `_secret_key`: **Válido**.
- `print`: **Válido técnicamente, pero NO recomendado** (Es una palabra reservada de Python y "romperías" la función original de imprimir).

</details>

---

2. **Compilador Mental**¿Qué tipo de dato y qué valor exacto tendrá la variable result después de ejecutar el siguiente bloque?

```python
value_a = "10"
value_b = 5
result = int(value_a) + float(value_b)
```

<details>
<summary>💡 Ver Solución</summary>

La variable `result` tendrá el tipo de dato `float` y el valor exacto `15.0`.
**Explicación:** Al sumar un entero (`10`) con un flotante (`5.0`), Python convierte automáticamente el resultado a float para no perder precisión decimal.

</details>

---

3. **El juego de las cajas (Variable Swapping Trap)** ¿Qué valores tendrán las variables `x` e `y` al final de la ejecución de este bloque de código?

```python
x = 5
y = 10

x = y
y = x
```

<details>
<summary>💡 Ver Solución</summary>

- Valor de `x`: `10`
- Valor de `y`: `10`

Este es un clásico error de lógica para principiantes. En la línea `x = y`, el valor de `x` cambia a `10` (perdiendo el `5` original para siempre). Por lo tanto, cuando se ejecuta `y = x`, le estás asignando a `y` el nuevo valor de `x`, que ya era 10. Para intercambiar valores correctamente en programación, se suele necesitar una tercera variable temporal o usar el truco nativo de Python: `x, y = y, x`.

</details>

---

4. **El detector de mentiras (Truthy vs Falsy Strings)** ¿Cuál será el valor booleano final de la variable is_valid?

```python
status_text = "False"
is_valid = bool(status_text)
```

<details>
<summary>💡 Ver Solución</summary>

- Resultado: `True`

**Explicación:** ¡Cuidado con la trampa! Aunque el texto dice `"False"` en Python cualquier cadena de texto que no esté vacía se evalúa como `True` en un contexto booleano. Aunque la cadena `"False"` contiene la palabra "False", es una cadena no vacía, por lo tanto, se considera truthy.

</details>

---

5. **La mutación (Dynamic Typing)** ¿Qué tipo de dato (`type`) y qué valor tendrá la variable `data` al final del script?

```python
data = 10
data = "Python"
data = data + " 3"
```

<details>
<summary>💡 Ver Solución</summary>

- Tipo de dato: `str`
- Valor: `"Python 3"`

**Explicación:** Esto demuestra el tipado dinámico de Python. La variable `data` comenzó siendo un entero (`int`), luego mutó a un texto (`str`) al reasignarle `"Python"`, y finalmente se le concatenó el texto `" 3"`. Python no se queja por cambiar el tipo de dato de la variable sobre la marcha.

</details>

---

6. **La suma prohibida (TypeError)** ¿Qué ocurrirá cuando la computadora intente ejecutar la tercera línea de este código?

```python
score = 99
message = "Your score is: "
final_output = message + score
```

<details>
<summary>💡 Ver Solución</summary>

- **Resultado:** El programa fallará y lanzará un error de tipo: `TypeError: can only concatenate str (not "int") to str`.

**Explicación:** Aunque Python es flexible, también es un lenguaje de tipado fuerte. Esto significa que no te dejará realizar operaciones entre tipos incompatibles de forma automática (como intentar "sumar" un texto con un número entero). Para arreglar este código y que funcione, tendrías que hacer un casting explícito: `final_output = message + str(score)`.

</details>
