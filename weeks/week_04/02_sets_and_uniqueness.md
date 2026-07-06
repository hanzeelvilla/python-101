# 02: Sets

En la lectura anterior vimos cómo los diccionarios nos permiten guardar información usando etiquetas personalizadas. Ahora exploraremos la última colección fundamental de Python: los **Conjuntos (Sets)**.

Un Set es una colección **no ordenada** de elementos donde **está estrictamente prohibido tener duplicados**. Imagínalo como una bolsa donde echas objetos: no importa en qué orden cayeron ni en qué posición están, lo único que importa es si un objeto está dentro de la bolsa o no.

---

## 1. Creación y Reglas de un Set

Los conjuntos se escriben utilizando llaves `{}` (igual que los diccionarios, pero **sin** usar los dos puntos `:` de clave-valor).

```python
# Creating a set with data
lucky_numbers = {4, 8, 15, 16, 23, 42}

# What happens if we force duplicates?
programming_languages = {"Python", "JavaScript", "Python", "TypeScript", "JavaScript"}

print(programming_languages)
# Output: {'TypeScript', 'JavaScript', 'Python'}
# Notice that duplicates were automatically destroyed and the order changed!
```

Si escribes `my_set = {}`, Python pensará que estás creando un diccionario vacío (**porque los diccionarios son más comunes**). Para crear un conjunto totalmente vacío, debes usar obligatoriamente la función `set()`:

```python
fake_set = {}      # Type: dict (Dictionary)
real_set = set()   # Type: set (True Empty Set)
```

---

## 2. Operaciones Básicas: Verificar, Agregar y Eliminar

Como los conjuntos no tienen un orden fijo, no puedes usar índices para modificar o buscar datos (escribir `my_set[0]` arrojará un error de inmediato). En su lugar, Python nos da herramientas para interactuar con los elementos:

### Verificar si un elemento existe (`in`)

Para saber si un objeto está dentro de un conjunto, utilizamos la palabra clave **`in`**. Gracias a la naturaleza de los conjuntos, esta búsqueda es **instantánea ($O(1)$)**. A diferencia de una lista, donde Python tiene que revisar elemento por elemento de izquierda a derecha ($O(n)$), en un set la respuesta es inmediata, sin importar si la colección tiene 5 elementos o 1 millón.

```python
verified_users = {"hanzeel", "alex99", "sam_hunter"}

# Checking membership
print("hanzeel" in verified_users)   # Output: True
print("dean_win" in verified_users)  # Output: False
```

### Agregar elementos (.add())

Para meter un nuevo dato al conjunto, utilizamos el método .add(elemento). Si el elemento que intentas agregar ya se encuentra dentro del set, Python simplemente lo ignorará de forma silenciosa sin duplicarlo ni arrojar errores.

```python
tools = {"Hammer", "Wrench"}

tools.add("Screwdriver") # Successfully added
tools.add("Hammer")      # Already exists! It is completely ignored

print(tools) # Output: {'Screwdriver', 'Hammer', 'Wrench'}
```

### Eliminar elementos (`.remove()` vs `.discard()`)

Python nos ofrece dos métodos para sacar elementos de un conjunto. Elegir el correcto es fundamental para garantizar que tu servidor no se caiga por un error inesperado:

1. `.remove(valor) (Peligroso)`: Busca el elemento y lo elimina. Si el valor no existe dentro del conjunto, el programa colapsa inmediatamente lanzando un `KeyError`.
2. `.discard(valor)` (Seguro / Recomendado): Busca el elemento y lo elimina. Si el valor no existe, el método no hace nada, no arroja ningún error y permite que tu código siga corriendo felizmente.

```python
inventory = {"Sword", "Shield", "Potion"}

# 1. Safe Deletion using .discard()
inventory.discard("Potion") # Removes "Potion"
inventory.discard("Gold")   # "Gold" is not there, but nothing breaks!

# 2. Risky Deletion using .remove()
inventory.remove("Shield")  # Removes "Shield"
# inventory.remove("Gold")  # CRASHES the program! KeyError: 'Gold'

print(inventory) # Output: {'Sword'}
```

## 3. Limpiar Listas

En el mundo real, los sistemas suelen llenarse de datos repetidos por errores de los usuarios o registros duplicados en las bases de datos.

Gracias a que los conjuntos destruyen los duplicados de forma nativa, podemos combinarlos con una lista para limpiar miles de datos corruptos en una sola línea de código:

```python
# A list with heavily duplicated data
corrupted_emails = ["alex@test.com", "sam@test.com", "alex@test.com", "dean@test.com", "sam@test.com"]

# Step 1: Convert list to set to destroy duplicates
clean_set = set(corrupted_emails) # {'dean@test.com', 'alex@test.com', 'sam@test.com'}

# Step 2: Convert it back to a list so it can be indexed again
fixed_emails = list(clean_set)

print(fixed_emails)
# Output: ['dean@test.com', 'alex@test.com', 'sam@test.com']

# Short Version:
# fixed_emails = list(set(corrupted_emails))
```

## 4 . Operaciones de Conjuntos (Operaciones Lógicas)

Los conjuntos se vuelven herramientas brutales cuando necesitamos comparar dos colecciones diferentes. Python nos permite realizar operaciones matemáticas de conjuntos usando símbolos muy sencillos:

Imaginemos que tenemos dos desarrolladores con diferentes habilidades tecnológicas:

```python
dev_a_skills = {"Python", "JavaScript", "HTML", "Git"}
dev_b_skills = {"TypeScript", "NodeJS", "JavaScript", "Git"}
```

### Unión (|): Combinar todo

Une todos los elementos de ambos conjuntos, eliminando los que se repitan entre ellos. Sirve para saber el catálogo total de opciones.

```python
all_skills = dev_a_skills | dev_b_skills
print(all_skills)
# Output: {'HTML', 'Python', 'NodeJS', 'TypeScript', 'JavaScript', 'Git'}
```

### Intersección (&): Lo que tienen en común

Devuelve únicamente los elementos que existen en ambos conjuntos al mismo tiempo. Ideal para encontrar similitudes o compatibilidades.

```python
shared_skills = dev_a_skills & dev_b_skills
print(shared_skills)
# Output: {'JavaScript', 'Git'}
```

### Diferencia (-): Lo que es exclusivo de uno

Devuelve los elementos que están en el primer conjunto pero no en el segundo. El orden aquí sí importa. Sirve para ver qué le falta a uno respecto al otro.

```python
# What skills does Dev A have that Dev B DOES NOT have?
exclusive_a = dev_a_skills - dev_b_skills
print(exclusive_a) # Output: {'HTML', 'Python'}

# What skills does Dev B have that Dev A DOES NOT have?
exclusive_b = dev_b_skills - dev_a_skills
print(exclusive_b) # Output: {'NodeJS', 'TypeScript'}
```

## Retos Cortos

### 1. El Filtro de Etiquetas

Analiza el siguiente bloque de código. ¿Qué número exacto se imprimirá en la consola al ejecutarlo?

```python
tags = ["python", "javascript", "python", "html", "css", "html"]
unique_tags_count = len(set(tags))
print(unique_tags_count)
```

<details>
<summary>💡 Ver Solución</summary>

**En la consola se imprimirá:** `4`

**Explicación:** Al pasar la lista tags por la función `set()`, Python elimina automáticamente los elementos duplicados. Los strings `"python"` y `"html"`, que aparecían dos veces cada uno, se reducen a una sola aparición. El conjunto resultante internamente se reduce a `{'python', 'javascript', 'html', 'css'}`. Al medirlo con `len()`, el conteo final de elementos únicos es `4`.

</details>

### 2. El Intruso Mutable

Mira con atención el siguiente intento de agregar datos a un conjunto. ¿El código se ejecutará con éxito o provocará una falla en el sistema? ¿Por qué?

```python
lucky_numbers = {10, 20, 30}
lucky_numbers.add([40, 50])
print(lucky_numbers)
```

<details>
<summary>💡 Ver Solución</summary>

**Resultado:** El programa colapsará inmediatamente arrojando un `TypeError: unhashable type: 'list'`.

**Explicación:** Esta es una de las reglas de seguridad más estrictas de los Conjuntos. **Todos los elementos dentro de un Set deben ser inmutables** (no modificables, como enteros, strings o tuplas) para que Python pueda garantizar que no cambiarán de valor de forma secreta. Como las listas son mutables (puedes alterar sus elementos internos en cualquier momento), Python bloquea la operación por completo para proteger la integridad del conjunto.

</details>
