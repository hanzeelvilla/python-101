# 02: Methods and State

En la lectura anterior aprendiste a definir atributos para darle propiedades a tus objetos (`self.name`, `self.hp`). Sin embargo, una entidad del mundo real no es solo una lista de datos estáticos, también realiza **acciones**.

En Programación Orientada a Objetos, las **acciones** que un objeto puede realizar se llaman **Métodos**.

## Métodos

Un método es una función que vive dentro de una clase. La diferencia clave entre una función común y un método es que **el método tiene acceso directo a la memoria interna del objeto a través de `self`.**

Si los atributos son los sustantivos y adjetivos de tu objeto, los métodos son los verbos:

| **Objeto**  |            **Atributos**            |                **Métodos**                 |
| :---------: | :---------------------------------: | :----------------------------------------: |
|   `User`    | `email`, `password`, `is_logged_in` | `login()`, `logout()`, `change_password()` |
|    `Car`    |   `brand`, `speed`, `fuel_level`    |   `accelerate()`, `brake()`, `refuel()`    |
| `Character` |        `name`, `hp`, `level`        |   `attack()`, `heal()`, `change_level()`   |

### Definiendo y llamando métodos

Para escribir un método, simplemente defines una función dentro del bloque de la clase

> [!NOTE]
> El primer parámetro de cualquier método de instancia debe ser siempre `self`.

```python
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    # Método 1: Acción simple que lee atributos
    def speak(self):
        print(f"{self.name}: ¡Hola! Estoy listo para la batalla.")

    # Método 2: Acción que recibe parámetros externos
    def attack(self, target_name):
        print(f"{self.name} ataca a {target_name} provocando daño!")

# --- INSTANCIACIÓN Y USO ---
hero = Character("Sam Winchester", 100)

# Llamamos a los métodos usando la notación de punto (.)
hero.speak()                 # Output: Sam Winchester: ¡Hola! Estoy listo para la batalla.
hero.attack("Demonio")       # Output: Sam Winchester ataca a Demonio provocando daño!
```

> [!NOTE]
> Cuando llamas a un método, **no necesitas pasar `self` manualmente**. Python lo hace automáticamente por ti. Por eso, cuando llamamos a `hero.speak()`, Python traduce internamente la llamada a `Character.speak(hero)`.

### Modificando el Estado Interno

El verdadero valor de los métodos es que nos permiten alterar el estado interno (los atributos) del objeto **de forma controlada y segura.**

En lugar de cambiar la vida de un personaje directamente desde fuera con `hero.hp = 0`, creamos un método que aplique las reglas de nuestro negocio o juego (**por ejemplo, evitar que la vida baje de 0**):

```python
class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.is_alive = True

    # Método que modifica el estado interno con validaciones
    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} recibió {amount} de daño. HP restante: {self.hp}")

        # Regla de negocio: Si el HP llega a 0 o menos, el personaje muere
        if self.hp <= 0:
            self.hp = 0
            self.is_alive = False
            print(f"{self.name} ha sido derrotado.")

    def heal(self, amount):
        if self.is_alive:
            self.hp += amount
            print(f"{self.name} se curó {amount} de HP. HP actual: {self.hp}")
        else:
            print(f"{self.name} está derrotado y no puede ser curado.")

# --- PROBANDO EL MANEJO DE ESTADO ---
hero = Character("Dean Winchester", 100)

hero.take_damage(40)  # HP baja a 60
hero.heal(20)         # HP sube a 80
hero.take_damage(90)  # HP baja a 0, is_alive pasa a False
hero.heal(50)         # Intento de curación rechazado
```

## El Método `__str__`

Si intentas imprimir un objeto directamente en la consola con `print(hero)`, Python mostrará algo bastante feo e ilegible en memoria:

```python
print(hero)
# Output misterioso: <__main__.Character object at 0x000001D4E3A82F10>
```

Para solucionar esto, Python incluye un método especial llamado `__str__`. Si defines `__str__` dentro de tu clase, puedes especificar qué texto en formato string debe retornarse cuando alguien imprima el objeto o lo convierta a texto.

```python
class Character:
    def __init__(self, name, hp, level=1):
        self.name = name
        self.hp = hp
        self.level = level

    # Definimos la representación en texto del objeto
    def __str__(self):
        return f"Hero Profile {self.name} | Nivel {self.level} | HP: {self.hp}"

hero = Character("Sam", 100)

# ¡Ahora print() utiliza automáticamente tu método __str__!
print(hero)
# Output: Hero Profile Sam | Nivel 1 | HP: 100
```

> [!WARNING]
> El método `__str__` debe retornar un string (`str`) usando la palabra reservada `return`. Si usas `print()` dentro de `__str__` o retornas un entero, Python arrojará un error.

## Retos Cortos

Es momento de retomar las clases `Human`, `Cat` y `Dog` que construiste en la lección anterior. Vas a agregarles métodos para que tus objetos puedan interactuar y cambiar su estado interno.

Actualiza cada clase con los siguientes requerimientos:

1. Actualiza la clase Human:
   - Agrega un atributo `money` inicializado en `0` en el `__init__`.
   - Agrega un método `work(amount)` que incremente `self.money` con la cantidad ganada e imprima un mensaje informando el nuevo saldo.
   - Agrega un método `birthday()` que incremente `self.age` en 1 y celebre su cumpleaños en consola.
   - Agrega el método `__str__` para mostrar una ficha formateada con el `name`, `age`, `occupation` y `money`.

2. Actualiza la clase Cat:
   - Agrega un método `meow()` que imprima un mensaje de maullido.
   - Agrega un método `lose_life()` que disminuya `self.lives_left` en 1 y verifique si el gato sigue vivo. Si `lives_left` llega a 0, imprime un mensaje indicando que el gato ha muerto.
   - Agrega el método `__str__` para mostrar una ficha formateada con el `name`, `color` y `lives_left`.

3. Actualiza la clase Dog:
   - Agrega un método `bark()` que imprima un mensaje de ladrido.
   - Agrega un método `fetch(item)` que imprima un mensaje indicando que el perro ha traído el `item` especificado.
   - Agrega el método `__str__` para mostrar una ficha formateada con el `name` y `breed`.

4. Prueba en Consola:
   - Instancia un objeto de cada clase.
   - Pon a trabajar al humano y hazlo cumplir años. Imprímelo directamente con `print(humano)` para probar **str**.
   - Haz que el gato maulle, pierda una vida e imprime su ficha.
   - Haz que el perro ladre, busque una pelota e imprime su ficha.

<details>
<summary> Ver Solución</summary>

```python
# 1. Definición de la Clase Human
class Human:
    def __init__(self, name, age, occupation="Student"):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.money = 0  # Atributo inicializado en 0

    def work(self, amount):
        self.money += amount
        print(f"{self.name} trabajó como {self.occupation} y ganó ${amount}. Saldo total: ${self.money}")

    def birthday(self):
        self.age += 1
        print(f"¡Feliz cumpleaños {self.name}! Ahora tienes {self.age} años.")

    def __str__(self):
        return f"Humano: {self.name} | Edad: {self.age} | Trabajo: {self.occupation} | Dinero: ${self.money}"

# 2. Definición de la Clase Cat
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.lives_left = 9  # Atributo por defecto

    def meow(self):
        print("Meow!")

    def lose_life(self):
        if self.lives_left > 0:
            self.lives_left -= 1
            print(f"{self.name} perdió una vida! Le quedan {self.lives_left} vidas.")
            if self.lives_left == 0:
                print(f"{self.name} ha gastado todas sus vidas...")
        else:
            print(f"{self.name} ya no tiene más vidas que perder.")

    def __str__(self):
        return f"Gato: {self.name} | Color: {self.color} | Vidas restantes: {self.lives_left}"

# 3. Definición de la Clase Dog
class Dog:
    def __init__(self, name, breed, is_trained=False):
        self.name = name
        self.breed = breed
        self.is_trained = is_trained

    def bark(self):
        print("Woof!")

    def fetch(self, item):
        print(f"{self.name}: ¡Trajo la {item}!")

    def __str__(self):
        return f"Perro: {self.name} | Raza: {self.breed}"

# --- EJECUCIÓN DE PRUEBA ---

# Probar Humano
person = Human("Hanzeel", 22, "Full-Stack Engineer")
person.work(500)
person.birthday()
print(person)  # Llama a __str__
print()

# Probar Gato
my_cat = Cat("Garfield", "Naranja")
my_cat.meow()
my_cat.lose_life()
print(my_cat)  # Llama a __str__
print()

my_dog = Dog("Viejon", "Beagle")
my_dog.bark()
my_dog.fetch("pelota")
print(my_dog)  # Llama a __str__

```

</details>
