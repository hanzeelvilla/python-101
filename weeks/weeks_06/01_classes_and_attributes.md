# Classes and Attributes — Del Diccionario al Objeto

Durante las semanas anteriores aprendiste a modelar entidades usando Diccionarios. Podíamos representar a un personaje, un usuario o un producto agrupando sus propiedades con pares clave-valor (`{"name": "Sam", "hp": 100}`).

Aunque los diccionarios son geniales para estructurar información pasiva, tienen una limitación importante: no empaquetan comportamiento de forma nativa. Si querías cambiar la vida de un personaje o curarlo, tenías que crear funciones externas que recibieran ese diccionario por parámetro.

La Programación Orientada a Objetos (POO) soluciona esto uniendo en un solo lugar los datos (Atributos) y las acciones (Métodos).

## Diccionario vs. Clase

Veamos la diferencia en código al intentar modelar a un personaje de un videojuego:

Con diccionarios:

```python
# Un diccionario solo guarda datos. No sabe hacer nada por sí mismo.
character_dict = {
    "name": "Sam Winchester",
    "hp": 100,
    "level": 1
}

# Si queremos modificar la vida, dependemos de una función externa
def heal(character, amount):
    character["hp"] += amount

heal(character_dict, 20)
```

Con clases:

```python
# La clase define qué datos tiene el objeto Y QUÉ SABE HACER
class Character:
    def __init__(self, name, hp, level=1):
        self.name = name
        self.hp = hp
        self.level = level

# Ahora el objeto es responsable de su propio estado
hero = Character("Sam Winchester", 100)
```

## Anatomía de una Clase: `__init__` y `self`

Para definir una clase en Python usamos la palabra reservada `class`, seguida del nombre en formato **PascalCase** (Mayúscula al inicio de cada palabra, como `PlayerCharacter` o `BankAccount`).

```python
class Character:
    # El Constructor: Se ejecuta automáticamente cuando 'nace' el objeto
    def __init__(self, name, hp, level=1):
        # Atributos de Instancia
        self.name = name
        self.hp = hp
        self.level = level
```

### El método constructor `___init__`

Es una función especial que Python invoca de forma automática en el momento exacto en que creas un objeto. Su trabajo es recibir los datos iniciales y configurar los valores por defecto.

### El parámetro `self`

`self` es la forma en que el objeto se refiere a sí mismo dentro de su propio código.

- Cuando escribes `self.name = name`, le estás diciendo a Python: _"En MI propia memoria (`self`), guarda el atributo `name` con el valor que me acaban de pasar por parámetro"_.
- Nunca tienes que pasar `self` manualmente al instanciar el objeto; Python lo inyecta por detrás automáticamente.

## Instanciando Objetos

Definir una clase solo crea un plano. Para **construir un objeto** necesitas realizar el proceso de **instanciación**.

Instanciar una clase significa invocar su nombre como si fuera una función, pasándole los argumentos requeridos por el método `__init__` y guardando el objeto resultante dentro de una variable.

````python
```python
# Sintaxis: variable = NombreDeLaClase(argumento1, argumento2)
hero1 = Character("Sam Winchester", 100)
````

> [!NOTE]
> El 3er parámetro `level` tiene un valor por defecto de `1`, por lo que no es obligatorio pasarlo al instanciar el objeto. Si no lo pasas, Python asumirá que es `1`.

## Atributos

Un **atributo** no es más que una **variable que pertenece a un objeto**. Sirve para almacenar el estado, las **características** o las propiedades de esa entidad en la memoria.

Para identificar los atributos de cualquier entidad del mundo real que quieras programar, hazte la pregunta: **"¿Qué datos describen a esta entidad?"**

- Si el objeto es**`User`**, sus atributos podrían ser: `name`, `email`, `password`, `is_admin`.
- Si el objeto es **`Car`**, sus atributos podrían ser: `brand`, `model`, `color`, `current_speed`.
- Si el objeto es **`Character`**, sus atributos podrían ser: `name`, `health`, `strength`, `level`.
- Etc.

### Accediendo y Modificar Propiedades

Una vez que has creado una instancia de un objeto, **las propiedades guardadas en su memoria no son privadas por defecto en Python**, puedes **leerlas** o **modificarlas** en cualquier momento utilizando el operador de punto (`.`).

#### Leer una Propiedad

Para consultar el valor de un atributo, escribes el **nombre del objeto**, un **punto** y el **nombre de la propiedad**:

````python
```python
# Sintaxis: objeto.propiedad
print(hero.name) # Imprime: Sam Winchester
print(hero.hp)   # Imprime: 100
````

#### Modificar una Propiedad

Si el estado del objeto cambia durante la ejecución del programa (por ejemplo, el personaje recibe un ataque o sube de nivel), puedes reasignar el valor de esa propiedad directamente con el operador de asignación `=`:

```python
# El personaje recibe daño
hero.hp = 75

# El personaje sube de nivel
hero.level = 2

print(f"{hero.name} ahora es nivel {hero.level} con {hero.hp} HP.")
# Output: Sam Winchester ahora es nivel 2 con 75 HP.
```

Si intentas acceder a una propiedad que no fue definida dentro del método `__init__` o en la clase, Python romperá la ejecución arrojando un `AttributeError`.

```python
# Intentamos acceder a 'mana', pero nuestro personaje solo tiene 'name', 'hp' y 'level'
print(hero.mana)
# CRASH: AttributeError: 'Character' object has no attribute 'mana'
```

## Retos Cortos

Es hora de poner a prueba tus manos en el teclado. Vas a crear los moldes para tres entidades del mundo real: un ser humano, un gato y un perro.

Define tres clases distintas siguiendo estos requerimientos:

1. **Clase `Human`**:
   - Su constructor `__init__` debe recibir: `name` (string) y `age` (entero).
   - Debe incluir un tercer atributo `occupation` con un valor por defecto (por ejemplo, `"Student"`).

2. **Clase `Cat`**:
   - Su constructor `__init__` debe recibir: `name` (string) y `color` (string).
   - Debe incluir un tercer atributo **fijo** `lives_left` inicializado por defecto en `9`.

3. **Clase `Dog`**:
   - Su constructor `__init__` debe recibir: `name` (string) y `breed` (raza, string).
   - Debe incluir un atributo `is_trained` (booleano) con valor por defecto `False`.

4. **Instanciación e Impresión**:
   - Instancia un objeto para cada clase (un humano, un gato y un perro) con datos reales o ficticios.
   - Utiliza la **notación de punto (`.`)** e impresiones formateadas (`f-strings`) para mostrar en consola las propiedades de cada uno.

<details>
<summary> Ver Solución</summary>

```python
# 1. Definición de la Clase Human
class Human:
    def __init__(self, name, age, occupation="Student"):
        self.name = name
        self.age = age
        self.occupation = occupation

# 2. Definición de la Clase Cat
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.lives_left = 9  # Atributo por defecto

# 3. Definición de la Clase Dog
class Dog:
    def __init__(self, name, breed, is_trained=False):
        self.name = name
        self.breed = breed
        self.is_trained = is_trained

# --- INSTANCIACIÓN DE OBJETOS ---

person = Human("Hanzeel", 22, "Full-Stack Engineer")
my_cat = Cat("Garfield", "Naranja")
my_dog = Dog("Viejon", "Beagle")

# --- LECTURA DE ATRIBUTOS (NOTACIÓN DE PUNTO) ---

print("=== REGISTRO DE ENTIDADES ===")
print(f"Humano: {person.name} | Edad: {person.age} años | Ocupación: {person.occupation}")
print(f"Gato: {my_cat.name} | Color: {my_cat.color} | Vidas restantes: {my_cat.lives_left}")
print(f"Perro: {my_dog.name} | Raza: {my_dog.breed} | ¿Entrenado?: {my_dog.is_trained}")
```

</details>
