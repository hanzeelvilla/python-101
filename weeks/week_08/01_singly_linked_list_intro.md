# Singly Linked List

Durante las semanas anteriores trabajaste con estructuras de datos que Python nos ofrece de forma nativa (`list`, `dict`, `set`, `tuple`).

A partir de esta semana entraremos en el terreno de las Estructuras de Datos Clásicas. Comenzaremos construyendo desde cero una de las estructuras lineales más emblemáticas de la informática: la **Lista Enlazada Simple (Singly Linked List).**

## ¿Qué es una Lista Enlazada Simple?

Una Lista Enlazada es una colección lineal de elementos llamados **nodos**.

A diferencia de las listas nativas de Python (arrays dinámicos), donde los elementos se guardan en bloques continuos de la memoria RAM, los nodos de una lista enlazada pueden estar dispersos en cualquier lugar de la memoria.

Cada nodo funciona como una cápsula que guarda dos cosas:

1. **El Valor (`val` / `data`)**: La información real que queremos almacenar (un número, texto, u objeto).
2. **El Puntero (next)**: Una referencia o enlace que apunta hacia la dirección de memoria del siguiente nodo en la secuencia. Si no hay más nodos, apunta a `None`.

```text
HEAD (Cabeza)                                           TAIL (Cola)
┌─────────────┐        ┌─────────────┐        ┌─────────────┐
│ val:  "A"   │        │ val:  "B"   │        │ val:  "C"   │
│ next: ──────┼───────►│ next: ──────┼───────►│ next: None  │
└─────────────┘        └─────────────┘        └─────────────┘
LENGTH = 3
```

## Componentes de una Lista Enlazada Simple

Para administrar una Lista Enlazada Simple, mantenemos tres propiedades principales en la estructura:

1. **`head` (Cabeza)**: Puntero que señala al primer nodo de la lista. Es el punto de entrada para recorrerla.
2. **`tail` (Cola)**: Puntero que señala al último nodo de la lista (aquel cuyo next es `None`).
3. **`length` (Longitud)**: Un contador entero que lleva el registro del número total de nodos activos en la lista.

## Lista Enlazada vs Lista Nativa de Python

¿Por qué quisiéramos usar una lista enlazada si ya existen las listas nativas de Python? Todo se reduce al rendimiento en memoria y la complejidad algorítmica (**Big O**):

|         **Operación**         |                    **Array/Lista Bativa**                     |                                        **Lista Enlazada Simple**                                         |
| :---------------------------: | :-----------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
|   Almacenamiento en memoria   |                  Bloque contiguo de memoria                   |                                 Nodos dispersos conectados por punteros                                  |
| Acceso aleatorio (por índice) |        `O(1)`. Salta directo a la dirreción en memoria        | `O(n)`. Tiene que empezar desde el `head` e ir saltando de `next` en `next` hasta llegar al nodo deseado |
|      Insertar al inicio       | `O(n)`. Requiere reindexar todos los elementos de la derecha  |                  `O(1)`. Solo reajusta los punteros del nuevo nodo a la cabeza antigua                   |
|      Eliminar al inicio       | `O(n)`. Requiere desplazar todos los elementos a la izquierda |                               `O(1)`. Se mueve la cabeza al siguiente nodo                               |
|           Busqueda            |                            `O(n)`                             |                                                   O(n)                                                   |

> [!NOTE]
> Las listas enlazadas son superiores cuando se necesita realizar inserciones o eliminaciones constantes al inicio o final de una colección sin el costo de reindexar memoria.

## Retos cortos

Vas a construir las dos clases fundamentales que servirán como plantilla para los métodos que desarrollaremos durante el resto de la semana.

### Instrucciones

Crea un script en tu entorno local con las siguientes especificaciones:

1. Crea la clase `Node`:
   - Su constructor **init** debe recibir un parámetro `value`.
   - Debe inicializar el atributo `self.val = value`.
   - Debe inicializar el atributo `self.next = None` (por defecto no apunta a nadie).

<details>
<summary>Ver Solución</summary>

```python
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
```

</details>

2. Crea la clase `SinglyLinkedList`:
   - Su constructor `__init__` no requiere parámetros externos.
   - Debe inicializar `self.head = None`.
   - Debe inicializar `self.tail = None`.
   - Debe inicializar `self.length = 0`.

<details>
<summary>Ver Solución</summary>

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
```

</details>
