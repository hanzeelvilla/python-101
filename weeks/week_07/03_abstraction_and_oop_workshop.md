# Abstraction & OOP Workshop

¡Bienvenido al taller integrador de la Semana 7! En esta lección abordaremos el último pilar de la Programación Orientada a Objetos: la **Abstracción**. Después, conectaremos todo lo aprendido durante las últimas dos semanas en un taller práctico del mundo real.

## Abstracción

La Abstracción consiste en enfocarse en **qué debe hacer un objeto sin importar cómo lo hace** internamente. Se trata de ocultar la complejidad técnica detrás de una interfaz clara y sencilla.

Piensa en el pedal del acelerador de un auto: tú no necesitas saber cómo funciona la inyección de combustible o la combustión interna para usarlo. Simplemente presionas el pedal (interfaz) y el auto acelera.

### Contratos Estrictos en Python (`abc` module)

Hasta ahora, si creábamos un método genérico como `make_sound()` en la clase `Animal`, un desarrollador podía olvidar sobrescribirlo en las clases hijas.

Para solucionar esto y crear reglas obligatorias, Python nos ofrece el módulo nativo `abc` (Abstract Base Classes):

- `ABC`: Es la clase base de la cual deben heredar nuestras clases abstractas.
- `@abstractmethod`: Es un decorador que marca un método como obligatorio. Si una clase hija no implementa este método, Python impedirá instanciarla y lanzará un error (`TypeError`).

```python
from abc import ABC, abstractmethod

# 1. Convertimos a Animal en una Clase Abstracta
class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 2. Definimos un contrato obligatorio
    @abstractmethod
    def make_sound(self):
        """Método abstracto: obliga a las clases hijas a definir cómo suena el animal."""
        pass

# INTENTO ILÍCITO: No se puede instanciar una clase abstracta directamente
# animal_generico = Animal("Desconocido", 2)
# TypeError: Can't instantiate abstract class Animal with abstract method make_sound
```

## The Pet Shelter System

Vas a diseñar un sistema de administración de refugio de animales donde coexisten las entidades que hemos trabajado: `Human` (veterinario/cuidador) y las mascotas `Dog` y `Cat`, las cuales heredan de una clase base abstracta `Animal`.

```text
                        ┌────────────────────────────────┐
                        │      CLASE ABSTRACTA (ABC)     │
                        │             Animal             │
                        ├────────────────────────────────┤
                        │ - name: str                    │
                        │ - _energy: int (Protected)     │
                        │ - @abstractmethod make_sound() │
                        └───────────────┬────────────────┘
                                        │
             ┌──────────────────────────┴──────────────────────────┐
             ▼                                                     ▼
┌──────────────────────────┐                             ┌──────────────────────────┐
│         Dog              │                             │         Cat              │
├──────────────────────────┤                             ├──────────────────────────┤
│ + breed: str             │                             │ + __lives_left: int      │
│ + make_sound() (Woof!)   │                             │ + make_sound() (Miau!)   │
└──────────────────────────┘                             └──────────────────────────┘
             ▲                                                     ▲
             └──────────────────────────┬──────────────────────────┘
                                        │ (Almacena en su lista)
                        ┌───────────────┴────────────────┐
                        │             Human              │
                        ├────────────────────────────────┤
                        │ - name: str                    │
                        │ - role: str                    │
                        │ - pets_under_care: list        │
                        │ + checkup(animal)              │
                        │ + feed_all_pets()              │
                        └────────────────────────────────┘
```

1. Clase Abstracta `Animal(ABC)`:

   Atributos:
   - `name` (str, público)
   - `age` (int, público)
   - `_energy` (int, protegido, inicializado en `100`)

   Métodos:
   - `eat(amount)`: Incrementa `_energy` con la cantidad especificada.
   - `@abstractmethod make_sound()`: Método abstracto sin código (`pass`).

    <details>
    <summary>Ver Solución</summary>

   ```python
   from abc import ABC, abstractmethod

   # 1. Clase Base Abstracta (Contrato)
   class Animal(ABC):
   def __init__(self, name, age):
   self.name = name
   self.age = age
   self._energy = 100 # Atributo protegido

       def eat(self, amount):
           self._energy += amount
           print(f"{self.name} comió y su energía subió a {self._energy}.")

       @abstractmethod
       def make_sound(self):
           """Obliga a implementar el sonido en las clases hijas."""
           pass
   ```

    </details>

2. Clases Hijas `Dog` y `Cat`:

   `Dog`:
   - Hereda de `Animal`. Recibe `name`, `age` y `breed`
   - Implementa obligatoriamente `make_sound()`: Imprime `"[Nombre] dice: ¡Woof!"`

   `Cat`:
   - Hereda de `Animal`. Recibe `name`, `age` y `color`.
   - Agrega el atributo privado `__lives_left` (inicializado en `7`) con su `@property`.
   - Implementa obligatoriamente `make_sound()`: Imprime `"[Nombre] dice: ¡Miau!"`.

    <details>
    <summary>Ver Solución</summary>

   ```python
   class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        print(f"[{self.name} - {self.breed}]: ¡Woof!")

    class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        self.__lives_left = 7  # Atributo privado

    @property
    def lives_left(self):
        return self.__lives_left

    def make_sound(self):
        print(f"[{self.name} - {self.color}]: ¡Miau!")
   ```

    </details>

3. Clase Contenedora `Human`:

   Atributos:
   - `name` (str, público)
   - `role` (str, ej. `"Veterinario"` o `"Cuidador"`)
   - `pets_under_care` (lista vacía por defecto)

   Métodos:
   - `adopt_pet(animal)`: Recibe una instancia de `Animal` (o sus hijas) y la añade a `pets_under_care`.
   - `checkup_pets()`: Recorre la lista `pets_under_care` y para cada animal:
     1. Imprime su nombre y edad.
     2. Ejecuta su método polimórfico `make_sound()`.
   - `feed_all_pets(food_amount)`: Recorre la lista de animales e invoca el método `.eat(food_amount)` en cada uno de ellos.

    <details>
    <summary>Ver Solución</summary>

   ```python
   class Human:
    def __init__(self, name, role="Cuidador"):
        self.name = name
        self.role = role
        self.pets_under_care = []

    def adopt_pet(self, animal):
        # Validamos que el objeto sea una instancia derivada de Animal
        if isinstance(animal, Animal):
            self.pets_under_care.append(animal)
            print(f"{self.name} ({self.role}) ahora cuida a {animal.name}.")
        else:
            print("Solo se pueden registrar objetos derivados de la clase Animal.")

    def checkup_pets(self):
        print(f"\n === CHEQUEO MÉDICO CON {self.name.upper()} ({self.role}) ===")
        if not self.pets_under_care:
            print("No hay mascotas bajo cuidado actualmente.")
            return

        for pet in self.pets_under_care:
            print(f"Paciente: {pet.name} | Edad: {pet.age} años")
            # Invocación polimórfica del método abstracto implementado
            pet.make_sound()

    def feed_all_pets(self, food_amount):
        print(f"\n=== ALIMENTANDO A LAS MASCOTAS EN EL REFUGIO ===")
        for pet in self.pets_under_care:
            pet.eat(food_amount)
   ```

    </details>
