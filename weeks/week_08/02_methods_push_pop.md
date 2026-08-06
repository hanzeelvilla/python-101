# Métodos `push` y `pop`

En el archivo anterior construimos las clases base `Node` y `SinglyLinkedList`. Ahora es momento de agregarles métodos para insertar y remover elementos desde el final de la lista.

## Método `push`

El método `push` se encarga de recibir un valor, envolverlo dentro de un nuevo `Node` y colocarlo al final de la lista enlazada.

1. Crea un método `push` dentro de la clase `SinglyLinkedList` que reciba un parámetro `value`.
2. Crear una nueva instancia de `Node` con ese valor (`new_node`).
3. Caso 1 (Lista vacía): Si la lista está vacía (`self.head` es `None` o `self.tail` es `None` o `self.length` es `0`), entonces:
   - El nuevo nodo se convierte en la cabeza y la cola de la lista (`self.head = new_node` y `self.tail = new_node`).
4. Caso 2 (Lista con nodos): Si la lista no está vacía, entonces:
   - Cambiar el puntero next de la cola actual (`self.tail.next`) para que apunte a `new_node`.
   - Actualiza la cola de la lista para que sea el nuevo nodo (`self.tail = new_node`).
5. Incrementa la longitud de la lista (`self.length += 1`).

<details>
<summary>Ver Solución</summary>

```python
def push(self, val):
    new_node = Node(val)

    if not self.head:
        self.head = new_node
        self.tail = self.head
    else:
        self.tail.next = new_node
        self.tail = new_node

    self.length += 1
    return self
```

</details>

## Método `pop`

El método pop remueve el último nodo de la lista y lo retorna. A diferencia de un array convencional, en una Lista Enlazada Simple no podemos retroceder desde la cola (`tail`) directamente al nodo anterior, ya que los punteros solo van hacia adelante.

Por ello, debemos recorrer la lista desde `head` usando un bucle hasta encontrar el penúltimo nodo.

1. Caso 1 (Lista vacía): Si no hay elementos en la lista (`self.length == 0` o `self.head is None` o `self.tail is None`), retornar `None`.
2. Caso 2 (Un solo nodo): Si solo hay un elemento (`self.head == self.tail` o `self.length == 1`), entonces:
   - Guardar el nodo actual para devolverlo.
   - Resetear `self.head = None` y `self.tail = None`.
   - Decrementar `self.length = 0`.
   - Retornar el nodo guardado.
3. Caso 3 (Más de un nodo): Si hay más de un nodo, entonces:
   - Crear dos variables de rastreo: `prev = self.head` y `current = prev.next`.
   - Hacer un bucle `while current.next`: para avanzar por la lista. En cada iteración:
     - Asignar `prev = current`.
     - Avanzar `current = current.next`.
   - Al terminar el bucle, `current` estará en el último nodo y `prev` en el penúltimo.
   - Cortar la conexión `prev.next = None`
   - Actualizar la cola `self.tail = prev`.
   - Decrementar la longitud `self.length -= 1`.
   - Retornar el nodo eliminado (`current`).

<details>
<summary>Ver Solución</summary>

```python
def pop(self):
    if not self.head:
        return None

    if self.length == 1:
        removed_node = self.head
        self.head = None
        self.tail = None
        self.length -= 1
        return removed_node

    prev = self.head
    current = prev.next

    while current.next:
        prev = current
        current = current.next

    self.tail = prev
    self.tail.next = None
    self.length -= 1

    return current
```

</details>
