# 03: Data Collections Comparison Guide

¡Felicidades! Has completado el estudio de las cuatro estructuras de datos fundamentales de Python: **Listas, Tuplas, Diccionarios y Sets**. Cada una de ellas fue diseñada por los ingenieros de software con un propósito específico, sacrificando ciertas capacidades a cambio de ganar otras (por ejemplo, sacrificar la velocidad de búsqueda por mantener un orden estricto, o sacrificar la capacidad de modificar los datos para ganar seguridad inmutable).

Esta guía sirve como tu "hoja de trucos" (Cheat Sheet) definitiva del módulo. Aquí analizaremos sus características para ayudarte a desarrollar la intuición necesaria para elegir **la estructura correcta ante cualquier problema en blanco**.

---

## 1. Tabla Maestra Comparación

| Colección                |     Sintaxis     | ¿Es Mutable? |     ¿Tiene Orden / Índice?      |        ¿Permite Duplicados?         | Eficiencia de Búsqueda (Big O)                                      |
| :----------------------- | :--------------: | :----------: | :-----------------------------: | :---------------------------------: | :------------------------------------------------------------------ |
| **Lista (`list`)**       |   `[a, b, c]`    |    **Sí**    | **Sí** (Por posición `0, 1...`) |               **Sí**                | • Por Índice: Instantáneo (`O(1)`) <br> • Por Valor: Lento (`O(n)`) |
| **Tupla (`tuple`)**      |   `(a, b, c)`    |      No      | **Sí** (Por posición `0, 1...`) |               **Sí**                | • Por Índice: Instantáneo (`O(1)`) <br> • Por Valor: Lento (`O(n)`) |
| **Diccionario (`dict`)** | `{"key": "val"}` |    **Sí**    |    No (Se accede por Llave)     | Llaves: **No** <br> Valores: **Sí** | • Por Llave: Ultra rápido (`O(1)`) <br> • Por Valor: Lento (`O(n)`) |
| **Conjunto (`set`)**     |   `{a, b, c}`    |    **Sí**    |               No                |               **No**                | • Por Valor: Ultra rápido (`O(1)`)                                  |

---

## 2. Árbol de Decisiones

Cuando estés diseñando un algoritmo y no sepas qué contenedor instanciar en tu código, hazle a tu problema estas tres preguntas en orden:

### Pregunta 1: ¿El orden posicional de los datos importa?

- **SÍ:** Necesitas una **Lista** o una **Tupla**. Tu programa recordará perfectamente quién está en primer lugar, quién en medio y quién al final.
- **NO:** Un **Diccionario** o un **Set** será mucho más eficiente y natural para modelarlo.

### Pregunta 2: ¿Los datos deben estar blindados contra accidentes?

- **SÍ:** Usa una **Tupla**. Te garantiza al 100% que ninguna otra función del código podrá borrar, reordenar o alterar los datos en la memoria durante la ejecución del programa.
- **NO (Los datos van a mutar, crecer o actualizarse continuamente):** Usa una **Lista**, un **Diccionario** o un **Set**.

### Pregunta 3: ¿Voy a realizar búsquedas repetitivas a gran escala?

- **SÍ:** Evita las listas y tuplas. Buscar un elemento por su valor dentro de una lista obliga a Python a escanear todo el contenedor de inicio a fin (tiempo lineal `O(n)`). Buscar una llave en un **Diccionario** o un elemento en un **Set** toma un solo paso inmediato (tiempo constante `O(1)`), sin importar si tienes 10 elementos o 5 millones.

---

## 3. Casos de Estudio del Mundo Real

Veamos cómo aplicarías este criterio técnico en el desarrollo de un videojuego o una aplicación profesional:

### Escenario A: El Inventario de un Personaje **Lista**

- **Por qué:** El jugador puede recoger pociones del mismo tipo (permite duplicados), el orden en que las acomoda en sus ranuras puede importar, y el inventario cambia constantemente a medida que consume recursos o recoge botín (mutabilidad).

### Escenario B: Las Coordenadas de un Mapa (`X`, `Y`, `Z`) **Tupla**

- **Por qué:** Un punto en el espacio tridimensional siempre tiene la misma estructura fija. Si cambias la coordenada `X` de forma aislada, ya destruiste la integridad de ese punto y estás hablando de un lugar completamente diferente en el universo. Es información de solo lectura, segura y de alta velocidad.

### Escenario C: El Perfil de un Usuario o Jugador **Diccionario**

- **Por qué:** Necesitas etiquetar cada propiedad de forma descriptiva: `{"username": "walle", "role": "admin", "level": 5}`. Acceder a los datos mediante una clave de texto es infinitamente más legible y mantenible que intentar adivinar en qué índice numérico de una lista se guardó el nivel del usuario.

### Escenario D: Registro de IDs Únicos / Filtro de Bloqueos **Set**

- **Por qué:** Si estás registrando las direcciones IP que visitan tu servidor y quieres saber cuántos usuarios _únicos_ tienes para evitar ataques o contar tráfico real, el Set se encarga de destruir las IP repetidas de forma automática en un solo paso y te permite verificar bloqueos instantáneamente.

---

## Retos Cortos

Lee los siguientes requerimientos técnicos e identifica qué tipo de colección deberías instanciar en Python para resolverlos de la forma más óptima:

1. Guardar los nombres de los días de la semana.
2. Almacenar los códigos de barras de los productos vendidos en una caja para saber cuántos artículos _diferentes_ se compraron al final del día (sin contar repeticiones).
3. Guardar el historial exacto de canciones reproducidas en orden cronológico por un usuario en Spotify.
4. Almacenar la ficha técnica de un automóvil (Marca, Modelo, Año, Precio).

<details>
<summary>Ver Respuestas Correctas y Justificación</summary>

1. **Tupla:** Los días de la semana nunca cambian, son constantes absolutas y su orden de Lunes a Domingo está completamente definido. No hay razón para permitir que muten.
2. **Set:** Al requerir saber cuántos artículos _diferentes_ se vendieron, el set es la herramienta ideal porque limpia el flujo de datos duplicados de forma nativa sin que tengas que programar bucles condicionales extra.
3. **Lista:** El orden exacto de reproducción importa críticamente (cuál sonó primero y cuál sigue) y el usuario puede escuchar la misma canción varias veces seguidas o en diferentes momentos (requiere duplicados).
4. **Diccionario:** Es la estructura perfecta para mapear propiedades con etiquetas claras y explícitas: `{"brand": "Ford", "model": "Mustang", "year": 2026, "price": 45000}`.

</details>
