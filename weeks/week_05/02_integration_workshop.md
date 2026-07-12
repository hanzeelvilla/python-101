# 02: Integration Workshop

¡Bienvenido al taller central de la semana! Ha llegado el momento de poner a prueba tu lógica de programación. En este archivo encontrarás **2 problemas prácticos que simulan situaciones específicas** del desarrollo de software en el mundo real, diseñados para que integres todas las herramientas y estructuras de datos que hemos visto hasta ahora.

## Proyecto 1: The Randomized Trivia Engine

### Contexto del Problema

Vas a construir el motor de un juego de preguntas y respuestas de opción múltiple (A, B, C, D). Para evitar que los usuarios hagan trampa memorizando el orden, el sistema debe **desordenar aleatoriamente las preguntas** cada vez que se inicie el juego.

### Requerimientos Técnicos

1. Copia la base de datos de preguntas provista abajo (una lista con diccionarios anidados).
2. Utiliza la librería nativa `random` de Python y su método `random.shuffle(tu_lista)` para desordenar las preguntas antes de iniciar el ciclo.
3. Crea un bucle que muestre una a una las preguntas y sus opciones en la pantalla.
4. Solicita la respuesta del usuario usando `input()`. Convierte la entrada a mayúsculas automáticamente para evitar fallas si escriben en minúscula.
5. Lleva un contador de puntos. Si la respuesta es correcta, felicita al usuario y suma 1 punto, si falla, muestra cuál era la respuesta correcta.

### Datos Iniciales (Copy-Paste)

```python
questions_db = [
    {
        "question": "¿Cuál de las siguientes colecciones es inmutable en Python?",
        "options": {
            "A": "Listas",
            "B": "Tuplas",
            "C": "Diccionarios",
            "D": "Sets"
        },
        "correct": "B"
    },
    {
        "question": "¿Qué método se utiliza para agregar un elemento al final de una lista?",
        "options": {
            "A": " .add()",
            "B": " .insert()",
            "C": " .append()",
            "D": " .push()"
        },
        "correct": "C"
    },
    {
        "question": "¿Cuál es la complejidad en el tiempo (Big O) para buscar una llave en un Diccionario?",
        "options": {
            "A": "O(1)",
            "B": "O(n)",
            "C": "O(log n)",
            "D": "O(n^2)"
        },
        "correct": "A"
    }
]
```

### Ejemplo de Entrada y Salida

```text
=== ¡BIENVENIDO A THE RANDOMIZED TRIVIA ENGINE! ===

Pregunta 1: ¿Qué método se utiliza para agregar un elemento al final de una lista?
A) .add()
B) .insert()
C) .append()
D) .push()
Tu respuesta (A, B, C o D): c
Tu respuesta es correcta. (+1 punto)

Pregunta 2: ¿Cuál es la complejidad en el tiempo (Big O) para buscar una llave en un Diccionario?
A) O(1)
B) O(n)
C) O(log n)
D) O(n^2)
Tu respuesta (A, B, C o D): a
Tu respuesta es correcta. (+1 punto)

Pregunta 3: ¿Cuál de las siguientes colecciones es inmutable en Python?
A) Listas
B) Tuplas
C) Diccionarios
D) Sets
Tu respuesta (A, B, C o D): b
Tu respuesta es correcta. (+1 punto)

=== JUEGO TERMINADO ===
Tu puntuación final es: 3 / 3 puntos.
```

<details>
<summary>Ver Código de Solución</summary>

```python
import random

def run_trivia():
    score = 0

    random.shuffle(questions_db)

    print("=== ¡BIENVENIDO A THE RANDOMIZED TRIVIA ENGINE! ===\n")

    for index, item in enumerate(questions_db, start=1):
        print(f"Pregunta {index}: {item['question']}")

        for letter, option_text in item["options"].items():
            print(f"{letter}) {option_text.strip()}")

        user_ans = input("Tu respuesta (A, B, C o D): ").strip().upper()

        if user_ans == item['correct']:
            print("Tu respuesta es correcta. (+1 punto)\n")
            score += 1
        else:
            print(f"Fallaste. La respuesta correcta era la opción {item['correct']}.\n")

    print("=== JUEGO TERMINADO ===")
    print(f"Tu puntuación final es: {score} / {len(questions_db)} puntos.")

run_trivia()
```

</details>

## Proyecto 2: The Fighter Stats Matcher

### Contexto del Problema

En un gimnasio de artes marciales mixtas, organizar combates de práctica (sparring) desequilibrados puede causar lesiones. Vas a crear un algoritmo de matchmaking automático que empareje peleadores basándose en perfiles altamente anidados.

### Requerimientos Técnicos

1. Escribe una función llamada `match_fighters` que reciba la lista de competidores y el nombre de un peleador específico que busca rival.
2. La función debe buscar el perfil del peleador solicitado y extraer sus estadísticas (`level` y `weight`).
3. El algoritmo debe escanear el resto de la lista y retornar una lista con los nombres de todos los rivales elegibles que cumplan simultáneamente con estas dos condiciones de seguridad:
   - Su peso (`weight`) debe ser exactamente igual (misma categoría de peso).
   - Su nivel (`level`) no debe tener una diferencia mayor a 1 nivel hacia arriba o hacia abajo respecto al peleador original.

### Datos Iniciales (Copy-Paste)

```python
fighters_db = [
    {
        "name": "Sam 'The Warrior'",
        "stats": {
            "level": 4,
            "weight": 70
        }
    },
    {
        "name": "Dean 'The Iron'",
        "stats": {
            "level": 5,
            "weight": 85
        }
    },
    {
        "name": "Cas 'The Angel'",
        "stats": {
            "level": 2,
            "weight": 70}
        },
    {
        "name": "Crowley 'The Demon'",
        "stats": {
            "level": 5,
            "weight": 70
        }
    }
]
```

### Ejemplo de Entrada y Salida

```text
Rivales seguros para Sam:
Salida: ["Cas 'The Angel'", "Crowley 'The Demon'"]

Rivales seguros para Dean:
Salida: []
```

<details>
<summary>Ver Código de Solución</summary>

```python
def match_fighters(fighters_list, target_name):
    target_fighter = None

    # Paso 1: Localizar al peleador objetivo
    for fighter in fighters_list:
        if fighter["name"] == target_name:
            target_fighter = fighter
            break

    if not target_fighter:
        return f"Error: El peleador '{target_name}' no existe en la base de datos."

    # Extraer variables de referencia
    target_lvl = target_fighter["stats"]["level"]
    target_wgt = target_fighter["stats"]["weight"]

    # Paso 2: Buscar rivales ideales que cumplan con los filtros de seguridad
    valid_opponents = []
    for fighter in fighters_list:
        if fighter["name"] == target_name:
            continue # No puede pelear contra sí mismo

        current_lvl = fighter["stats"]["level"]
        current_wgt = fighter["stats"]["weight"]

        # Calcular la diferencia absoluta de niveles usando la función nativa abs()
        lvl_diff = abs(target_lvl - current_lvl)

        if current_wgt == target_wgt and lvl_diff <= 1:
            valid_opponents.append(fighter["name"])

    return valid_opponents
```

</details>
