# Access Modifiers & Encapsulation

En la semana anterior aprendiste a crear atributos dentro del constructor `__init__` y a leerlos o modificarlos usando la notación de punto (`objeto.atributo = nuevo_valor`).

Aunque esto es sencillo, en el desarrollo de software profesional puede ser peligroso. Si permites que cualquier parte del código modifique las variables de tu objeto sin control, puedes terminar con datos corruptos (por ejemplo, asignar `-5 vidas` a un gato o un saldo de dinero negativo sin autorización).

Para evitar esto existe el primer pilar de la Programación Orientada a Objetos: El Encapsulamiento, soportado por los Modificadores de Acceso.

## Modificadores de Acceso en Python

En lenguajes como Java o C++, existen palabras reservadas estrictas (`public`, `private`, `protected`) que el compilador exige. Python, bajo la filosofía de "todos somos adultos responsables aquí", maneja estos niveles de privacidad mediante convenciones de nombres con guiones bajos (`_` y `__`):

| **Tipo de Acceso** |  **Sintaxis**  | **Nivel de Privacidad** | **¿Dónde se debe acceder?**                     |
| :----------------: | :------------: | :---------------------: | ----------------------------------------------- |
|      `public`      |  `self.name`   |     Sin restricción     | Cualquier parte del código                      |
|    `protected`     |  `self._age`   |   Convención de aviso   | Solo dentro de la clase y sus subclases (hijos) |
|     `private`      | `self.__money` |   Restricción fuerte    | Únicamente dentro de la propia clase            |

### Public

Es el comportamiento por defecto que usaste la semana pasada. Todo el mundo puede leerlo y modificarlo desde fuera de la clase.

```python
class Human:
    def __init__(self, name):
        self.name = name # Atributo público

person = Human("Hanzeel")
print(person.name)   # Lectura pública: Hanzeel
person.name = "Abraham" # Modificación pública directa
```

### Protected

Al agregar un solo guion bajo (`_`) antes del nombre de la propiedad, le indicas a otros desarrolladores: "Este atributo es de uso interno o para clases heredadas; por favor no lo modifiques directamente desde fuera".

```python
class Human:
    def __init__(self, name, age):
        self.name = name
        self._age = age # Atributo protegido (Un guion bajo)
```

> [!WARNING]
> Python NO bloquea técnicamente el acceso a atributos protegidos. Es una convención de caballeros que debes respetar.

### Private

Al agregar dos guiones bajos (`__`), Python activa un mecanismo llamado **Name Mangling** (deformación de nombres). Esto altera internamente el nombre del atributo en la memoria RAM para que no pueda ser accedido o modificado directamente por accidente usando la notación de punto estándar.

```python
class Human:
    def __init__(self, name, money):
        self.name = name
        self.__money = money # Atributo privado (Dos guiones bajos)

person = Human("Hanzeel", 1000)

# Intentar acceder directamente causará un error
print(person.__money)
# AttributeError: 'Human' object has no attribute '__money'
```

## Encapsulamiento

El Encapsulamiento consiste en ocultar el estado interno de un objeto y exigir que toda interacción con él se realice a través de métodos públicos seguros (**Getters y Setters**).

Piensa en un cajero automático: tú no abres la caja fuerte del banco con un destornillador para cambiar tu saldo manualmente. Interactúas con la pantalla del cajero (interfaz/método), el cual valida tu NIP y entrega o descuenta el dinero de forma segura.

### Getters y Setters

Para implementar Getters (métodos para leer) y Setters (métodos para escribir/validar) de forma elegante, Python ofrece el decorador `@property`.

```python
class Human:
    def __init__(self, name, initial_money):
        self.name = name
        self.__money = initial_money  # Atributo privado

    # 1. GETTER: Permite LEER el valor privado como si fuera un atributo normal
    @property
    def money(self):
        return self.__money

    # 2. SETTER: Permite MODIFICAR y VALIDAR el valor antes de guardarlo
    @money.setter
    def money(self, new_amount):
        if new_amount < 0:
            print("ERROR: El saldo de dinero no puede ser negativo.")
        else:
            self.__money = new_amount
            print(f"Saldo actualizado correctamente: ${self.__money}")

# --- PRUEBA DE ENCAPSULAMIENTO ---
person = Human("Hanzeel", 500)

# Leemos el saldo a través del @property (Getter)
print(f"Saldo de {person.name}: ${person.money}") # Output: 500

# Intentamos asignar un valor inválido (Pasa por el @money.setter)
person.money = -200 # Output: ERROR: El saldo de dinero no puede ser negativo.

# Asignamos un valor válido
person.money = 1200 # Output: Saldo actualizado correctamente: $1200
```

## Lectura complementaria

Para profundizar más sobre cómo funciona el Name Mangling por detrás y ver ejemplos detallados de cada nivel de acceso, revisa esta guía extra:

- [Geek Python — Access Modifiers in Python](https://geekpython.in/access-modifiers-in-python)

## Retos cortos

Es momento de retomar las clases de la semana pasada y aplicarles blindaje de encapsulamiento.

Crea un script en tu entorno local y modifica las clases `Cat` y `Human` siguiendo estas reglas:

### Clase Cat

1. Convierte su atributo `lives_left` en un atributo privado (`__lives_left`), inicializándolo en `7`.
2. Crea su Getter `@property` para permitir consultar las vidas restantes.
3. Crea su Setter `@lives_left.setter` con la siguiente regla de negocio: si se intenta asignar un valor menor a `0` o mayor a `7`, debe mostrar un mensaje de error y no cambiar el valor actual.

<details>
<summary> Ver Solución</summary>

```python
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.__lives_left = 7  # Atributo privado

    @property
    def lives_left(self):
        return self.__lives_left

    @lives_left.setter
    def lives_left(self, value):
        if value < 0 or value > 7:
            print(f"Valor inválido ({value}). Las vidas de un gato deben estar entre 0 y 7.")
        else:
            self.__lives_left = value
            print(f"Vidas de {self.name} actualizadas a: {self.__lives_left}")
```

</details>

### Clase Human

1. Haz privado su atributo `age` (`__age`).
2. Crea un Getter y un Setter para `age`.
3. Validación en Setter: Un humano solo puede cumplir años o aumentar su edad. Si el nuevo valor de edad es menor a la edad actual, muestra un mensaje prohibiendo la "máquina del tiempo".

<details>
<summary> Ver Solución</summary>

```python
class Human:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Atributo privado

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < self.__age:
            print(f"Error: No puedes reducir la edad de {self.name} de {self.__age} a {new_age} años.")
        else:
            self.__age = new_age
            print(f"La nueva edad de {self.name} es {self.__age} años.")
```

</details>
