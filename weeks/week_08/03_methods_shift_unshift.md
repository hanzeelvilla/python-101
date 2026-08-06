# Métodos `shift` y `unshift`

En la lección anterior aprendiste a insertar y remover elementos desde el final de la lista con `push` y `pop`.

Hoy abordaremos los métodos `shift` y `unshift`, los cuales se encargan de manipular elementos desde el inicio de la lista (la cabeza). Una de las mayores ventajas de las Listas Enlazadas sobre los Arrays nativos es que estas operaciones ocurren en tiempo constante `O(1)`, ya que no requieren reindexar elementos en memoria.

## Método `shift`

El método `shift` se encarga de eliminar el primer nodo (`head`) de la lista y retornarlo.

1. Caso 1 (Lista vacía): Si no hay elementos (`self.head is None` o `self.tail is None` o `self.length == 0`), retornar `None`.
2. Caso 2 (Lista con elementos):
   - Guardar la cabeza actual en una variable temporal (`old_head = self.head`).
   - Mover el puntero `head` al siguiente nodo (`self.head = self.head.next`).
   - Decrementar la longitud de la lista (`self.length -= 1`).
   - Validación de lista vacía: Si tras decrementar la longitud queda en `0` (o `self.head` pasa a ser `None`), reasignar la cola a `None` (`self.tail = None`).

<details>
<summary>Ver Solución</summary>

```python
def shift(self):
    if not self.head:
        return None

    old_head = self.head

    self.head = self.head.next
    self.length -= 1

    if self.length == 0:
        self.tail = None

    return old_head
```

</details>

## Método `unshift`

El método `unshift` recibe un valor, crea un nuevo nodo con él y lo coloca en la primera posición de la lista, convirtiéndolo en la nueva cabeza (`head`).

1. Crear una función `unshift` que reciba un valor (`val`) como argumento.
2. Crear una nueva instancia de `Node` con el valor recibido (`new_node`).
3. Caso 1 (Lista vacía): Si no hay cabeza (`self.head is None`):
   - Establecer `self.head = new_node` y `self.tail = new_node`.
4. Caso 2 (Lista con elementos):
   - Apuntar el `next` del nuevo nodo a la cabeza actual (`new_node.next = self.head`).
   - Reasignar la cabeza de la lista al nuevo nodo (`self.head = new_node`).
5. Incrementar la longitud de la lista (`self.length += 1`).

<details>
<summary>Ver Solución</summary>

```python
def unshift(self, val):
    new_node = Node(val)

    if not self.head:
        self.head = new_node
        self.tail = self.head
    else:
        new_node.next = self.head
        self.head = new_node

    self.length += 1
```

</details>
