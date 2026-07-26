# Advanced OOP & The 4 Pillars of Software Design

¡Bienvenido a la Semana 7! Durante la semana pasada aprendiste los cimientos de la Programación Orientada a Objetos: la creación de clases, atributos, métodos y la instanciación de objetos.

Esta semana daremos el paso definitivo hacia el diseño de arquitectura de software profesional. Aprenderás a proteger tu código, reutilizar lógica masivamente y crear contratos estrictos para tus aplicaciones utilizando los Modificadores de Acceso y Los 4 Pilares de la POO (**Encapsulamiento, Herencia, Polimorfismo y Abstracción**).

Para que la curva de aprendizaje sea totalmente fluida, reutilizaremos la familia de clases que ya conoces (`Human`, `Cat` y `Dog`), llevándolas desde estructuras simples hasta un sistema completo interconectado.

## Objetivos de la semana

- Dominar la sintaxis y convenciones de los Modificadores de Acceso en Python (Público, Protegido `_` y Privado `__`).
- Implementar el 1er Pilar (**Encapsulamiento**) utilizando decoradores `@property` para la lectura (Getters) y modificación validada (Setters) de atributos.
- Aplicar el 2do Pilar (**Herencia**) para reutilizar código definiendo clases padre y extendiendo funcionalidades en subclases mediante `super()`.
- Utilizar el 3er Pilar (**Polimorfismo**) para redefinir comportamientos mediante la sobrescritura de métodos (Method Overriding).
- Comprender el 4to Pilar (**Abstracción**) mediante el uso del módulo `abc` (`ABC`, `@abstractmethod`) para definir contratos de diseño obligatorios en clases abstractas.

## Ruta para esta Semana

Sigue el orden de lectura y práctica sugerido para construir el conocimiento paso a paso:

1. [01_access_modifiers_and_encapsulation.md](01_access_modifiers_and_encapsulation.md)
   - Privacidad en Python: Convención de guiones bajos (`_` protegido, `__` privado) y el mecanismo _Name Mangling_.
   - 1er Pilar — **Encapsulamiento**: Proteger el estado interno de un objeto para evitar datos corruptos.
   - Getters y Setters: Uso elegante del decorador `@property` para aplicar reglas de negocio.
   - Retos Cortos: Blindaje de vida y edad en las clases `Cat` y `Human`.
2. [02_inheritance_and_polymorphism.md](02_inheritance_and_polymorphism.md)
   - 2do Pilar — **Herencia**: Reutilización de código usando clases base y la función `super().__init__()`.
   - Explicación con Vehículos: La jerarquía de `Vehicle` -> `Car` y `Motorbike`.
   - 3er Pilar — Polimorfismo: Misma interfaz, distinto comportamiento mediante sobrescritura de métodos.
   - Retos Cortos: Construyendo la jerarquía de la familia `Animal`, `Dog` y `Cat`.
3. [03_abstraction_and_oop_workshop.md](03_abstraction_and_oop_workshop.md)
   - 4to Pilar — **Abstracción**: Ocultar la complejidad y definir contratos con el módulo `abc` (`ABC` y `@abstractmethod`).
   - El Proyecto Pet Shelter System: Un taller práctico integrador donde un `Human` (Veterinario/Cuidador) administra el refugio e interactúa con mascotas (`Dog` y `Cat`) bajo el contrato de la clase abstracta `Animal`.
