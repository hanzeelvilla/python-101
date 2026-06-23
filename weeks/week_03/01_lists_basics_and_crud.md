# 01: Lists Basics and CRUD Operations

Hasta ahora, has trabajado con variables que guardan un único valor. Si necesitabas almacenar los nombres de 5 usuarios, tenías que crear `user1`, `user2`, etc. Las **Listas** resuelven esto permitiéndonos agrupar múltiples elementos en una sola estructura ordenada y dinámica.

En Python, una lista es una colección ordenada de elementos (que pueden ser de cualquier tipo: enteros, strings, booleanos o incluso otras listas) separados por comas y encerrados entre corchetes `[]`.

---

## 1. Creación y Anatomía de una Lista (Create & Read)

Para crear una lista, simplemente encerramos los elementos entre `[]`. Podemos medir cuántos elementos tiene una lista utilizando la función nativa **`len()`**.

```python
# Creating an empty list
shopping_list = []

# Creating a list with initial data
player_scores = [100, 85, 92, 78]
languages = ["Python", "JavaScript", "TypeScript"]

# Measuring the length of a list
total_languages = len(languages)
print(f"I am learning {total_languages} languages.") # Output: 3
```

## 2. El Sistema de Direcciones: Indexación

Para acceder a un elemento específico dentro de la lista (Read), utilizamos su índice (su posición en la fila) encerrado entre corchetes justo después del nombre de la lista.

Python utiliza un sistema de indexación dual:

- Índices Positivos: Comienzan en `0` desde la izquierda (primer elemento) hasta `len(lista) - 1`.
- Índices Negativos: Comienzan en `-1` desde la derecha (último elemento) hacia atrás.

```python
videogames = ["Zelda", "Metroid", "Halo", "Minecraft"]

# Reading using positive indices
print(videogames[0])  # Output: Zelda (First item)
print(videogames[2])  # Output: Halo

# Reading using negative indices (from right to left)
print(videogames[-1]) # Output: Minecraft (Last item)
print(videogames[-3]) # Output: Metroid
```

> [!WARNING]
> Si intentas acceder a un índice que no existe (por ejemplo, `videogames[10]`), Python detendrá tu programa inmediatamente con un `IndexError: list index out of range`. Siempre el índice más alto posible es `len(lista) - 1`.

## 3. Modificar Elementos (Update)

A diferencia de los strings (que son inmutables y no puedes cambiarles una sola letra a la fuerza), las listas son mutables. Esto significa que puedes alterar, reemplazar o actualizar cualquier elemento directamente usando su índice.

```python
hardware_tools = ["Hammer", "Screwdriver", "Wrench"]

# Updating the second element (index 1)
hardware_tools[1] = "Electric Drill"

print(hardware_tools)
# Output: ['Hammer', 'Electric Drill', 'Wrench']
```

## 4. Eliminar Elementos (Delete)

Python nos da tres herramientas nativas para sacar elementos de una lista. Elegir la correcta depende de qué necesitas hacer con el dato eliminado:

### A. El método `.pop(index)`

Elimina el elemento en el índice indicado y te lo entrega (lo retorna) para que lo guardes en una variable si lo necesitas. **Si no le pasas ningún índice, elimina automáticamente el último elemento de la lista.**

```python
tasks = ["Email client", "Fix bug", "Code review"]

# Remove the last item and save it
completed_task = tasks.pop()
print(f"Done with: {completed_task}") # Output: Code review
print(tasks)                          # Output: ['Email client', 'Fix bug']

# Remove by specific index
first_task = tasks.pop(0)
print(tasks)                          # Output: ['Fix bug']
```

### B. El método `.remove(value)`

Busca el elemento por su valor exacto y lo elimina. A diferencia de `.pop()`, este método no te devuelve el elemento y **solo elimina la primera coincidencia que encuentre de izquierda a derecha.**

```python
inventory = ["Sword", "Shield", "Potion", "Sword"]

inventory.remove("Sword") # Removes the FIRST sword
print(inventory)          # Output: ['Shield', 'Potion', 'Sword']
```

> [!WARNING]
> Si intentas usar `.remove()` con un valor que no existe en la lista, el programa arrojará un `ValueError`.

### C. La palabra clave `del`

Es una instrucción directa del sistema para borrar un elemento en una posición específica de la memoria sin retornar nada.

```python
cart = ["Bread", "Milk", "Eggs"]
del cart[1]  # Deletes "Milk"
print(cart)  # Output: ['Bread', 'Eggs']
```
