# Métodos `insert` y `remove`

Con los métodos `push`, `pop`, `shift`, `unshift`, `get` y `set` listos, hemos llegado al punto culminante de la Singly Linked List: insertar y eliminar nodos en cualquier posición intermedia de la lista.

La clave de estos dos métodos reside en la reutilización de código: aprovecharemos los métodos de los extremos (`push`, `unshift`, `pop`, `shift`) cuando los índices correspondan a las puntas, y usaremos `get` cuando el objetivo esté en medio.

## Método `insert`

El método `insert` agrega un nuevo nodo en el índice exacto indicado, desplazando las referencias de los nodos vecinos.

1. Recibir un `index` y un valor `val`.
2. Validación de Límites:
   - Si `index < 0` o `index > self.length`, está fuera de rango; retornar `False`.
3. Casos Extremos (Reutilización de métodos):
   - Si `index == self.length`: El elemento va al final de la lista. Llamar a `self.push(val)` y retornar `True`.
   - Si `index == 0`: El elemento va al inicio de la lista. Llamar a `self.unshift(val)` y retornar `True`.
4. Inserción en Medio:
   - Obtener el nodo anterior a la posición deseada llamando a `self.get(index - 1)` y guardarlo en `prev_node`.
   - Crear el nuevo nodo: `new_node = Node(val)`.
   - Guardar la referencia al nodo que le sigue actualmente: `temp = prev_node.next`.
   - Reconectar punteros:
     - Apuntar el `next` del anterior al nuevo nodo: `prev_node.next = new_node`.
     - Apuntar el `next` del nuevo nodo al nodo temporal: `new_node.next = temp`.
5. Incrementar la longitud de la lista (`self.length += 1`).
6. Retornar `True`.

```text
INSERTAR EN ÍNDICE 2 (insert(2, "X")):
             Index 0          Index 1 (prev)                   Index 2 (temp)
             [ "A" ]  ──►     [ "B" ]        ────────►        [ "C" ]  ──► None
                                 │                               ▲
                                 │ 1. prev.next = [ "X" ]        │ 2. [ "X" ].next = temp
                                 ▼                               │
                              [ "X" ] ───────────────────────────┘
```

<details>
<summary>Ver Solución</summary>

```python
def insert(self, index, val):
    # 1. Validación de límites
    if index < 0 or index > self.length:
        return False

    # 2. Casos extremos con métodos auxiliares
    if index == self.length:
        self.push(val)
        return True
    if index == 0:
        self.unshift(val)
        return True

    # 3. Inserción intermedia
    prev_node = self.get(index - 1)
    new_node = Node(val)
    temp = prev_node.next

    prev_node.next = new_node
    new_node.next = temp

    self.length += 1
    return True
```

</details>

## Método `remove`

El método `remove` busca el nodo en la posición indicada, lo remueve de la secuencia reajustando los enlaces de sus vecinos y lo retorna.

1. Recibir un `index`.
2. Validación de Límites:
   - Si `index < 0` o `index >= self.length`, está fuera de rango; retornar `None`.
3. Casos Extremos (Reutilización de métodos):
   - Si `index == 0`: Eliminar al inicio. Llamar y retornar `self.shift()`.
   - Si `index == self.length - 1`: Eliminar al final. Llamar y retornar `self.pop()`.
4. Eliminación en Medio:
   - Obtener el nodo anterior a la posición a eliminar llamando a `self.get(index - 1)` y guardarlo en `prev_node`.
   - Guardar el nodo que va a ser eliminado: `removed_node = prev_node.next`.
   - Saltar el nodo eliminado en la cadena de punteros:
     - `prev_node.next = removed_node.next`
5. Decrementar la longitud de la lista (`self.length -= 1`).
6. Desconectar el nodo removido (`removed_node.next = None`) por seguridad y retornarlo.

<details>
<summary>Ver Solución</summary>

```python
def remove(self, index):
    # 1. Validación de límites
    if index < 0 or index >= self.length:
        return None

    # 2. Casos extremos con métodos auxiliares
    if index == 0:
        return self.shift()
    if index == self.length - 1:
        return self.pop()

    # 3. Eliminación intermedia
    prev_node = self.get(index - 1)
    removed_node = prev_node.next

    # Bypassear el nodo eliminado
    prev_node.next = removed_node.next

    self.length -= 1
    removed_node.next = None
    return removed_node
```

</details>
