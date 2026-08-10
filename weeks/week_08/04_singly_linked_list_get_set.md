# Métodos `get` y `set`

En los archivos anteriores aprendiste a insertar y remover nodos al inicio y al final de la lista en tiempo constante `O(1)`.

Hoy exploraremos cómo buscar un nodo en una posición específica usando el método `get` y cómo modificar su valor mediante el método `set`. A diferencia de los arrays nativos de Python donde el acceso por índice es directo (`O(1)`), en una Lista Enlazada Simple debemos recorrer la lista nodo por nodo a través de sus punteros hasta llegar a la posición deseada, lo que toma un tiempo de `O(n)`.

## Método `get`

El método `get` recibe un índice basado en cero (index) y retorna el objeto `Node` que se encuentra en esa posición.

1. Recibir un parámetro `index`.
2. Validación de Límites: Si el `index` es menor a `0` o mayor o igual a `self.length`, el índice está fuera de rango; retornar `None`.
3. Recorrido:
   - Crear una variable contador `counter = 0`.
   - Crear una variable de rastreo inicializada en el `head`: `current = self.head`.
   - Realizar un bucle `while counter != index`:
     - Avanzar al siguiente nodo: `current = current.next`.
     - Incrementar el contador: `counter += 1`.
4. Retornar el nodo encontrado (`current`).

```text
BUSCANDO ÍNDICE 2 (get(2)):
Index:      0             1             2
          Head
         [ "A" ]  ──►   [ "B" ]  ──►   [ "C" ]  ──►   [ "D" ]  ──► None
                                        ▲
                                   current (retornar)
```

<details>
<summary>Ver Solución</summary>

```python
def get(self, index):
    # 1. Validación de límites del índice
    if index < 0 or index >= self.length:
        return None

    # 2. Recorrido hasta la posición requerida
    counter = 0
    current = self.head
    while counter != index:
        current = current.next
        counter += 1

    # 3. Retornamos el nodo encontrado
    return current
```

</details>

## Método `set`

El método set recibe un `index` y un nuevo valor `val`, busca el nodo correspondiente en esa posición y actualiza su propiedad `val`.

1. Recibir un `index` y el nuevo `val`.
2. Reutilizar el método `get(index)` para encontrar el nodo objetivo y guardarlo en una variable (`found_node = self.get(index)`).
3. Caso 1 (Nodo encontrado):
   - Actualizar la propiedad del nodo: `found_node.val = val`.
   - Retornar `True` para confirmar que la actualización fue exitosa.
4. Caso 2 (Nodo no encontrado):
   - Retornar `False` para indicar que la actualización falló.

<details>
<summary>Ver Solución</summary>

```python
def get(self, index):
    # 1. Buscamos el nodo reutilizando el método get
    found_node = self.get(index)

    # 2. Si el nodo existe, actualizamos su valor y retornamos True
    if found_node:
        found_node.val = val
        return True

    # 3. Si no existe, retornamos False
    return False
```

</details>
