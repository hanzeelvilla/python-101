# 01: Mastering Dictionaries in Python

Hasta ahora, para acceder a un elemento en una lista o tupla, dependías obligatoriamente de su posición numérica (`0, 1, 2...`). Esto funciona bien para secuencias simples, pero si quieres guardar la información de un perfil de usuario, recordar que el nombre está en el índice `0`, el rol en el `1` y el correo en el `2` se vuelve insostenible a gran escala.

Los **Diccionarios** solucionan este problema de raíz. Son colecciones mutables y no indexadas que nos permiten almacenar datos emparejados mediante una estructura de **Clave-Valor (Key-Value)**. En lugar de buscar por números, buscas por etiquetas descriptivas.

---

## 1. Anatomía de un Diccionario

En Python, los diccionarios se escriben entre llaves `{}`. Cada elemento es un par compuesto por una **llave (Key)** y un **valor (Value)**, separados por dos puntos `:`. Las parejas se separan entre sí por comas.

```python
# Creating an empty dictionary
user_profile = {}

# Creating a dictionary with data
user = {
    "username": "hanzeel",
    "role": "Fullstack Engineer",
    "level": 4,
    "is_active": True
}
```

Las llaves de un diccionario deben ser únicas (**no puede haber dos llaves con el mismo nombre**) y deben ser inmutables (pueden ser strings, enteros o tuplas). Las listas jamás pueden ser llaves de un diccionario porque son mutables y su contenido puede cambiar. Los valores, por otro lado, pueden ser lo que tú quieras (listas, otros diccionarios, etc.).

## 2. El Ciclo CRUD en Diccionarios

Aprenderemos a manipular quirúrgicamente un diccionario a través de sus operaciones esenciales:

### Create & Update (Agregar y Modificar)

Para añadir una nueva pareja clave-valor, o para modificar una existente, utilizamos la sintaxis `diccionario[llave] = valor`. **Si la llave no existe, Python la crea** si ya existe, reemplaza su valor viejo por el nuevo.

```python
developer = {"name": "Alex", "language": "Python"}

# 1. Create: Adding a new key
developer["experience_years"] = 3

# 2. Update: Modifying an existing key
developer["language"] = "TypeScript"

print(developer)
# Output: {'name': 'Alex', 'language': 'TypeScript', 'experience_years': 3}
```

### Read (Lectura Segura)

Para leer un valor, la forma intuitiva es usar diccionario[llave]. Sin embargo, esto es peligroso: si buscas una llave que no existe, tu programa colapsará inmediatamente con un `KeyError`.

Para evitar caídas del sistema, la forma profesional es usar el método `diccionario.get(llave, valor_por_defecto)`. Si la llave existe, te da el valor; si no existe, te devuelve un valor seguro que tú elijas sin romper el código.

> [!NOTE]
> Aunque si es más común usar `diccioario[llave]`

```python
server_config = {"ip": "192.168.1.1", "port": 8080}

# Danger Read: Works if the key exists
print(server_config["ip"]) # Output: 192.168.1.1

# print(server_config["status"])
# CRASHES! KeyError: 'status'

# Safe Read: Avoids crashes entirely
print(server_config.get("port", 3000))   # Output: 8080 (Found)
print(server_config.get("status", "off")) # Output: off (Not found, safe default)
```

### Delete (Eliminar)

Podemos remover elementos usando la instrucción `del` o el método `.pop()`. Al igual que en las listas, `.pop(llave)` elimina la pareja y te retorna el valor eliminado.

```python
product = {"id": 101, "name": "Mechanical Keyboard", "stock": 15}

# Using del (No return value)
del product["stock"]

# Using .pop() (Returns the value before destroying it)
deleted_name = product.pop("name")

print(product)      # Output: {'id': 101}
print(deleted_name) # Output: Mechanical Keyboard
```

## 3. Iteración (Recorrer Diccionarios)

Para pasar un bucle `for` a través de un diccionario, Python nos provee de tres métodos esenciales para extraer la información de forma limpia:

```python
stats = {"kills": 12, "deaths": 2, "assists": 8}

# 1. Iterating only over KEYS (.keys())
for key in stats.keys():
    print(f"Stat Category: {key}")

# 2. Iterating only over VALUES (.values())
for val in stats.values():
    print(f"Score Value: {val}")

# 3. Iterating over BOTH simultaneously (.items())
# Returns pairs as temporary tuples that we can unpack on the fly
for key, val in stats.items():
    print(f"-> {key}: {val}")
```

## Retos de Código

### Challenge 1: The Hunter Profile (Diccionario Simple)

**Problema:** Para entender cómo mapear las propiedades de un objeto del mundo real, vas a crear el perfil digital de un personaje de televisión.

Crea un diccionario llamado `hunter_profile` que almacene la información de **Sam Winchester** de la serie _Supernatural_. El diccionario debe tener exactamente las siguientes llaves (keys) con sus respectivos valores:

- `first_name`: "Sam"
- `last_name`: "Winchester"
- `occupation`: "Hunter"
- `brother`: "Dean Winchester"
- `vehicle`: "Chevrolet Impala 1967"
- `status`: "Active"

Imprime en la consola el nombre completo del cazador y su ocupación accediendo directamente a las llaves del diccionario.

<details>
<summary>💻 Ver Código de Solución</summary>

```python
# Creating the character dictionary
hunter_profile = {
    "first_name": "Sam",
    "last_name": "Winchester",
    "occupation": "Hunter",
    "brother": "Dean Winchester",
    "vehicle": "Chevrolet Impala 1967",
    "status": "Active"
}

# Reading and formatting the output
fullname = hunter_profile["first_name"] + " " + hunter_profile["last_name"]
print(f"Character: {fullname}")
print(f"Occupation: {hunter_profile['occupation']}")
```

</details>

### Challenge 2: The Pokédex Simulator (Diccionarios dentro de una Lista)

Las APIs modernas de internet (como la famosa [PokéAPI](https://pokeapi.co/)) devuelven la información de los servidores utilizando un formato idéntico a los diccionarios y listas de Python. Vamos a simular una Pokédex interactiva.

Crea una lista llamada `pokedex`. Esta lista debe contener 3 diccionarios, donde cada diccionario represente a un Pokémon (puedes usar a Bulbasaur, Charmander y Squirtle).

Cada Pokémon (diccionario) debe estructurarse con la siguiente información:

1. `name` (String)
2. `pokedex_number` (Entero)
3. `types` (Lista de Strings): Se usa una lista porque un Pokémon puede tener uno o más tipos simultáneamente.
4. `attacks` (Lista de Strings): Se usa una lista porque un Pokémon conoce múltiples movimientos de combate.

Información de ejemplo para cada Pokémon:

|     `name`     | `pokedex_number` |       `types`       |                `attacks`                |
| :------------: | :--------------: | :-----------------: | :-------------------------------------: |
| `"Bulbasaur"`  |       `1`        | `["Grass, Posion"]` | `["Tackle, "Vine Whip", "Razor Leaf"]`  |
| `"Charmander"` |       `4`        |     `["Fire"]`      | `["Scratch", "Ember", "Flamethrower"]`  |
|  `"Squirtle"`  |       `7`        |     `["Water"]`     | `["Tackle", "Water Gun", "Hydro Pump"]` |

<details>
<summary>💻 Ver Código de Solución</summary>

```python
# A list containing dictionaries, which contain lists inside!
pokedex = [
    {
        "name": "Bulbasaur",
        "pokedex_number": 1,
        "types": ["Grass", "Poison"],
        "attacks": ["Tackle", "Vine Whip", "Razor Leaf"]
    },
    {
        "name": "Charmander",
        "pokedex_number": 4,
        "types": ["Fire"],
        "attacks": ["Scratch", "Ember", "Flamethrower"]
    },
    {
        "name": "Squirtle",
        "pokedex_number": 7,
        "types": ["Water"],
        "attacks": ["Tackle", "Water Gun", "Hydro Pump"]
    }
]
```

</details>

### Challenge 3: The Series Database (Catálogo Complejo)

Problema: Las plataformas de streaming como Netflix o HBO guardan sus catálogos usando colecciones altamente anidadas. Vas a diseñar una base de datos miniatura para tres series de televisión específicas: Supernatural, Fallout y El Mentalista.

Crea una lista llamada `series_database`. Adentro, cada serie debe ser un diccionario con la siguiente estructura:

1. `title` (String)
2. `categories` (Lista de Strings con géneros como "Drama", "Sci-Fi", "Mystery")
3. `rating` (Flotante o Entero que represente su calificación de 1 a 5 estrellas)
4. `main_characters` (Lista de Strings con los nombres de los personajes principales)

Información de ejemplo para cada serie:

|      `title`      |            `categories`             | `rating` |               `main_characters`                |
| :---------------: | :---------------------------------: | :------: | :--------------------------------------------: |
| `"Supernatural"`  |  `["Drama", "Fantasy", "Horror"]`   |  `4.8`   | `["Sam Winchester, Dean Winchester, Castiel"]` |
|    `"Fallout"`    | `["Sci-Fi", "Action", "Adventure"]` |  `4.7`   |   `["Lucy MacLean", "The Ghoul", "Maximus"]`   |
| `"El Mentalista"` |   `["Mystery", "Drama", "Crime"]`   |  `4.6`   |      `["Patrick Jane", "Teresa Lisbon"]`       |

<details>
<summary>💻 Ver Código de Solución</summary>

```python
# Complex catalog simulation
series_database = [
    {
        "title": "Supernatural",
        "categories": ["Drama", "Fantasy", "Horror"],
        "rating": 4.8,
        "main_characters": ["Sam Winchester", "Dean Winchester", "Castiel"]
    },
    {
        "title": "Fallout",
        "categories": ["Sci-Fi", "Action", "Adventure"],
        "rating": 4.7,
        "main_characters": ["Lucy MacLean", "The Ghoul", "Maximus"]
    },
    {
        "title": "The Mentalist",
        "categories": ["Mystery", "Drama", "Crime"],
        "rating": 4.6,
        "main_characters": ["Patrick Jane", "Teresa Lisbon"]
    }
]
```

</details>
