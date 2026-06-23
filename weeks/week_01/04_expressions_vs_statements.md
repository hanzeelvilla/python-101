# 04: Expressions vs Statements

Para entender profundamente cómo Python ejecuta tu código, debes conocer la diferencia entre dos conceptos fundamentales: **Expressions** (Expresiones) y **Statements** (Sentencias o Instrucciones).

Dominar esta distinción te ayudará a leer código de forma más analítica y a evitar errores de sintaxis comunes en el futuro.

---

## 1. ¿Qué es una Expresión (Expression)?

Una **expresión** es cualquier bloque de código que la computadora puede evaluar para **producir o devolver un solo valor**.

Si puedes imprimirlo directamente, guardarlo en una variable, o si la computadora puede reducirlo a un único resultado, entonces es una expresión.

### Ejemplos de Expresiones

```python
# Literal values (They are already a value)
5
"Hello"
True

# Arithmetic operations (They evaluate to a single number)
10 + 5          # Evaluates to 15
20 / 2          # Evaluates to 10.0

# Comparison operations (They evaluate to a Boolean)
5 > 3           # Evaluates to True
age >= 18       # Evaluates to True or False depending on 'age'

# Function calls that return something
int("42")       # Evaluates to the integer 42
type(10.5)      # Evaluates to <class 'float'>
```

## ¿Qué es una Sentencia (Statement)?

Una sentencia es una instrucción completa que le ordena a la computadora realizar una acción. Ejecuta un comando, pero no produce un valor por sí misma.

Una sentencia está compuesta por una o más expresiones, organizadas de forma que representen una línea de ejecución completa.

### Ejemplos de Sentencias

```python
# Assignment statement (Performs the action of storing a value)
x = 5

# Output statement (Performs the action of displaying something on screen)
print("Hello, world!")

# Import statement (Performs the action of bringing an external module)
import math
```

(Más adelante en el curso verás sentencias de control como if, for y while, las cuales controlan el flujo del programa pero no generan un valor).

## 3. ¿Cómo interactúan entre sí?

La forma más fácil de entenderlos es ver cómo una sentencia suele contener expresiones dentro de ella.

Miremos con atención esta línea de código:

```python
score = 10 + 5
```

- `10 + 5` es una expresión. Python la evalúa y la reduce al valor 15.
- `score = 10 + 5` es la sentencia completa. Es una instrucción de asignación que toma el resultado de la expresión y lo guarda dentro de la caja llamada `score`.

## Retos Cortos

Determina si las siguientes líneas de código representan una Expresión o una Sentencia.

1. **El dilema del número**

```python
x * 2
```

<details>
<summary>💡 Ver Solución</summary>

- Resultado: Expresión

**Explicación:** Multiplicar el valor de `x` por `2` producirá un nuevo número como resultado. No se está guardando en ningún lado ni se está haciendo ninguna acción definitiva, solo se está calculando un valor.

</details>

---

2. **El comando de asignación**

```python
username = "coder_girl"
```

<details>
<summary>💡 Ver Solución</summary>

- Resultado: Sentencia

**Explicación:** Es una instrucción completa de asignación. Le ordena a Python crear la variable y almacenar el texto en la memoria.

</details>

---

3. **La transformación de texto**

```python
str(100)
```

<details>
<summary>💡 Ver Solución</summary>

- Resultado: Expresión

**Explicación:** La función `str(100)` toma el valor entero 100 y lo convierte en una cadena de texto. Produce un único valor como resultado.

</details>

---

4. **El combo mixto**

¿Qué es la línea completa y qué es la parte interna derecha en el siguiente código?

```python
is_adult = age >= 18
```

<details>
<summary>💡 Ver Solución</summary>

- `age >= 18` es una Expresión (se evalúa como `True` o `False`).
- `is_adult = age >= 18` es la Sentencia completa (ejecuta la acción de asignar ese booleano a la variable).

</details>
