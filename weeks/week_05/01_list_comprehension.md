# 01: List Comprehension

Hasta ahora, cada vez que querías crear una lista modificada o filtrar elementos de un contenedor, tenías que seguir 4 pasos:

1. Crear una lista vacía de soporte (`acumulador = []`).
2. Escribir un bucle `for` para recorrer la lista original.
3. Evaluar una condición con un `if` (opcional).
4. Usar `.append()` para meter el elemento transformado a la lista nueva.

Aunque esto funciona perfectamente, Python ofrece una herramienta elegante llamada **List Comprehension** (comprensión de listas). No es un concepto nuevo de lógica; es simplemente un atajo de sintaxis que te permite fusionar esos 4 pasos en una sola línea de código limpia y legible.

## 1. El Antes y el Después

Imagina que tenemos una lista de números y queremos crear una nueva lista que contenga el doble de cada número.

Enfoque de 4 pasos (tradicional)

```python
numbers = [1, 2, 3, 4, 5]
doubled_numbers = []

for n in numbers:
    doubled_numbers.append(n * 2)

print(doubled_numbers) # Output: [2, 4, 6, 8, 10]
```

Enfoque con List Comprehension

```python
numbers = [1, 2, 3, 4, 5]
doubled_numbers = [n * 2 for n in numbers]
print(doubled_numbers) # Output: [2, 4, 6, 8, 10]
```

**¿Cómo se lee esto?**
Al leer `[n * 2 for n in numbers]`, piensa: "Quiero guardar el doble de `n`, por cada `n` que se encuentre dentro de `numbers`". Todo encerrado entre corchetes `[]` porque el resultado final sigue siendo una lista.

## 2. Sintaxis List Comprehension

Para construir cualquier List Comprehension sin equivocarte, apréndete este mapa de posiciones:

```text
nueva_lista = [ expresión_final  for elemento in coleccion_original ]
                     │                 │                 │
                     │                 │                 └─ La lista vieja a recorrer
                     │                 └─ El nombre de la variable temporal
                     └─ Qué le vas a hacer al elemento antes de guardarlo
```

## 3. Filtros

¿Qué pasa si no queremos transformar todos los elementos, sino únicamente los que cumplan con una regla? En la sintaxis tradicional, metías un `if` dentro del bucle. En List Comprehension, el `if` se coloca al puro final de la línea.

Enfoque de 4 pasos (tradicional)

```python
all_numbers = [10, 15, 20, 25, 30, 35]
only_evens = []

for n in all_numbers:
    if n % 2 == 0:
        only_evens.append(n)
```

Enfoque con List Comprehension

```python
all_numbers = [10, 15, 20, 25, 30, 35]

only_evens = [n for n in all_numbers if n % 2 == 0]

print(only_evens) # Output: [10, 20, 30]
```

## Retos de Código

### Filtro de Spam

Dada una lista de correos electrónicos, crea una nueva lista que contenga únicamente los correos que pertenezcan al dominio `"@gmail.com"`.

- **Dato inicial:** `emails = ["user1@gmail.com", "user2@yahoo.com", "admin@gmail.com", "test@outlook.com"]`
- **Salida esperada:** `["user1@gmail.com", "admin@gmail.com"]`

<details>
<summary>Ver Código de Solución</summary>

```python
emails = ["user1@gmail.com", "user2@yahoo.com", "admin@gmail.com", "test@outlook.com"]
gmail_only = [email for email in emails if email.endswith("@gmail.com")]
print(gmail_only)
```

</details>

### Buscador de palabras largas

Dada una lista de palabras, quédate únicamente con aquellas que tengan más de 5 caracteres de longitud.

**Dato inicial:** `words = ["apple", "banana", "kiwi", "strawberry", "grape", "watermelon"]`
**Salida esperada:** `["banana", "strawberry", "watermelon"]`

<details>
<summary>Ver Código de Solución</summary>

```python
words = ["apple", "banana", "kiwi", "strawberry", "grape", "watermelon"]
long_words = [w for w in words if len(w) > 5]
print(long_words)
```

</details>
