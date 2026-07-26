# Inheritance & Polymorphism

En la lección anterior aprendiste a proteger los datos internos de tus clases usando Encapsulamiento. Ahora exploraremos dos pilares que te permitirán reutilizar código masivamente y diseñar sistemas flexibles: la Herencia y el Polimorfismo.

## Herencia

Imagina que estás programando un sistema de transporte. Tienes que crear las clases `Car` (Auto) y `Motorbike` (Motocicleta).

Ambas entidades comparten un montón de características y acciones en común: tienen marca, modelo, velocidad actual, y ambas se pueden acelerar o frenar. Escribir esas mismas propiedades en ambas clases por separado sería duplicar código (violando el principio **DRY**: _Don't Repeat Yourself_).

La **Herencia** nos permite definir una **Clase Padre** (o Base) con las características generales, y hacer que las **Clases Hijas** (o Subclases) hereden automáticamente todos sus atributos y métodos.

```text
               ┌───────────────────────┐
               │    CLASE PADRE:       │
               │        Vehicle        │
               │ - brand, model, speed │
               │ - accelerate(), stop()│
               └───────────┬───────────┘
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
  ┌─────────────────────┐     ┌─────────────────────┐
  │    CLASE HIJA:      │     │    CLASE HIJA:      │
  │        Car          │     │      Motorbike      │
  │ + doors: int        │     │ + has_sidecar: bool │
  │ + open_trunk()      │     │ + wheelie()         │
  └─────────────────────┘     └─────────────────────┘
```

### Implementando Herencia y la función `super()`

Para indicar que una clase hereda de otra en Python, pasamos el nombre de la clase padre entre paréntesis al definir la clase hija: `class Car(Vehicle):`.

Además, utilizamos la función `super().__init__()` dentro del constructor de la clase hija para invocar el constructor del padre y delegarle la inicialización de los atributos compartidos.

```python
# 1. CLASE PADRE (BASE)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0

    def accelerate(self, increment):
        self.speed += increment
        print(f"[{self.brand} {self.model}] Aceleró a {self.speed} km/h.")

    def stop(self):
        self.speed = 0
        print(f"[{self.brand} {self.model}] Se ha detenido por completo.")


# 2. CLASE HIJA 1: Car (Hereda de Vehicle)
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        # super() invoca el __init__ de Vehicle para guardar brand y model
        super().__init__(brand, model)
        self.doors = doors  # Atributo exclusivo de Car

    def open_trunk(self):
        print(f"Abriendo la cajuela del {self.brand} {self.model}.")


# 3. CLASE HIJA 2: Motorbike (Hereda de Vehicle)
class Motorbike(Vehicle):
    def __init__(self, brand, model, has_sidecar=False):
        super().__init__(brand, model)
        self.has_sidecar = has_sidecar  # Atributo exclusivo de Motorbike

    def wheelie(self):
        print(f"¡El conductor de la {self.brand} {self.model} está haciendo un caballito!")


# --- PRUEBA DE HERENCIA ---
my_car = Car("Toyota", "Corolla", doors=4)
my_bike = Motorbike("Yamaha", "MT-07")

# Ambos objetos heredan los métodos de Vehicle
my_car.accelerate(50)  # Output: [Toyota Corolla] Aceleró a 50 km/h.
my_bike.accelerate(80) # Output: [Yamaha MT-07] Aceleró a 80 km/h.

# Cada objeto tiene sus propios métodos exclusivos
my_car.open_trunk()    # Output: Abriendo la cajuela del Toyota Corolla.
my_bike.wheelie()      # Output: ¡El conductor de la Yamaha MT-07 está haciendo un caballito!
```

## Polimorfismo

La palabra Polimorfismo proviene del griego y significa _"muchas formas"_. En POO, el polimorfismo se refiere a la capacidad de diferentes clases hijas de implementar un mismo método con un **comportamiento totalmente distinto.**

Esto se logra mediante la **Sobrescritura de Métodos (Method Overriding)**: la clase hija vuelve a definir un método que ya existía en la clase padre para personalizar su ejecución.

### Ejemplo de Polimorfismo con Vehículos

Imagina que agregamos un método `honk()` (tocar el claxon) en la clase `Vehicle`, pero cada tipo de vehículo suena diferente:

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def honk(self):
        print("¡Sonido genérico de vehículo!")


class Car(Vehicle):
    # Sobrescribimos el método honk() para el auto
    def honk(self):
        print(f"[{self.brand}]: ¡Beep! ¡Beep!")


class Motorbike(Vehicle):
    # Sobrescribimos el método honk() para la moto
    def honk(self):
        print(f"[{self.brand}]: ¡Meeep! ¡Meeep!")


# --- POLIMORFISMO EN ACCIÓN ---
# Creamos un garaje con distintos tipos de vehículos
garage = [Car("Ford"), Motorbike("Honda"), Car("Chevrolet")]

# Podemos iterar la lista y llamar a .honk() sin preocuparnos de qué tipo específico es cada uno
print("=== PROBANDO CLAXONS EN EL GARAJE ===")
for vehicle in garage:
    vehicle.honk() # Cada objeto responde según su propia implementación
```

## Retos cortos

Es momento de aplicar estos conceptos heredando y personalizando las clases con las que trabajamos la semana pasada.

Crea un script en tu entorno local y construye la jerarquía de animales siguiendo estos pasos:

1. Crea la Clase Padre `Animal`:
   - Su constructor `__init__` debe recibir: `name` (str) y `age` (int).
   - Debe tener un atributo protegido `_energy` inicializado en `100`.
   - Método `eat(amount)`: Incrementa `_energy` en la cantidad indicada y muestra un mensaje informando que el animal comió.
   - Método `make_sound()`: Debe imprimir un mensaje genérico como: `"[Nombre] emite un sonido genérico."`.

    <details>
    <summary>Ver Solución</summary>

   ```python
   class Animal:
           def __init__(self, name, age):
               self.name = name
               self.age = age
               self._energy = 100  # Atributo protegido

           def eat(self, amount):
               self._energy += amount
               print(f"{self.name} comió y recuperó energía. Energía actual: {self._energy}")

           def make_sound(self):
               print(f"{self.name} hace un sonido genérico de animal.")
   ```

    </details>

2. Crea la Clase Hija `Dog` (Hereda de `Animal`):
   - Su constructor `__init__` recibe `name`, `age` y `breed` (raza). Usa `super().__init__()` para pasar los datos al padre.
   - Sobrescribe `make_sound()` para que imprima: `"[Nombre] dice: ¡Woof! ¡Woof!"`.
   - Agrega un método exclusivo `fetch_ball()` que reduzca `_energy` en `20` e imprima que el perro fue a buscar la pelota. Si `_energy` es menor a `20`, imprime que el perro está demasiado cansado para buscar la pelota.

    <details>
    <summary>Ver Solución</summary>

   ```python
   class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # Hereda atributos de Animal
        self.breed = breed

    # Sobrescritura Polimórfica de Método
    def make_sound(self):
        print(f"[{self.name} ({self.breed})]: ¡Woof! ¡Woof!")

    def fetch_ball(self):
        if self._energy >= 20:
            self._energy -= 20
            print(f"{self.name} corrió tras la pelota. Energía restante: {self._energy}")
        else:
            print(f"{self.name} está demasiado cansado para jugar.")
   ```

    </details>

3. Crea la Clase Hija `Cat` (Hereda de `Animal`):
   - Su constructor `__init__` recibe `name`, `age` y `color`. Usa `super().__init__()`.
   - Incluye el atributo privado `__lives_left` (inicializado en `7`) con su respectivo `@property`.
   - Sobrescribe `make_sound()` para que imprima: `"[Nombre] dice: ¡Miau!"`.

   <details>
   <summary>Ver Solución</summary>

   ```python
   class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        self.__lives_left = 7  # Atributo privado

    @property
    def lives_left(self):
        return self.__lives_left

    # Sobrescritura Polimórfica de Método
    def make_sound(self):
        print(f"[{self.name}]: ¡Miau!")
   ```

    </details>
