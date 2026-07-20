# OOP Workshop — Building a Music Player Platform

¡Bienvenido al taller de Programación Orientada a Objetos! En este taller vas a construir un sistema modular que simula la lógica interna de una plataforma de streaming como Spotify.

En el mundo real, los sistemas complejos se construyen conectando componentes más pequeños. Tu computadora no es una sola pieza indestructible: está formada por una pantalla, un teclado, un procesador y módulos de memoria RAM. Cada uno es un objeto independiente, pero juntos forman un sistema funcional.

En Python ocurre exactamente lo mismo. Un atributo de una clase no se limita a ser un número, un texto o un booleano (`str`, `int`, `bool`). Un atributo dentro de un objeto puede almacenar instancias completas de OTRA clase.

## El Proyecto: Spotify Engine

Vas a desarrollar dos clases que interactúan entre sí para gestionar canciones, listas de reproducción (playlists) y favoritos de un usuario.

```text
        ┌────────────────────────┐
        │        Spotify         │ (Orquestador)
        ├────────────────────────┤
        │ - user_name: str       │
        │ - favorite_songs: list ┼──► Almacena objetos [ Song, Song, ... ]
        │ - playlists: dict      ┼──► Almacena { "Playlist": [ Song, Song ] }
        └────────────────────────┘
                        │
                        ▼
        ┌────────────────────────┐
        │          Song          │ (Objeto Atómico)
        ├────────────────────────┤
        │ - name: str            │
        │ - artist: str          │
        │ - is_playing: bool     │
        └────────────────────────┘
```

### Clase `Song`

Crea la clase `Song` con los siguientes requisitos:

1. **Atributos**:
   - `name` (`str`): Nombre de la canción.
   - `artist` (`str`): Nombre del artista.
   - `album` (`str`): Nombre del álbum al que pertenece la canción.
   - `genre` (`str`): Género musical de la canción.
   - `is_playing` (`bool`): Indica si la canción se está reproduciendo actualmente. Inicialmente, debe ser `False`.

2. **Métodos**:
   - `play()`: Cambia el estado de `is_playing` a `True` y muestra un mensaje indicando que la canción está reproduciéndose.
   - `pause()`: Cambia el estado de `is_playing` a `False` y muestra un mensaje indicando que la canción ha sido pausada.
   - `__str__()`: Devuelve una representación en cadena de la canción, incluyendo su `name`, `artist`, `album` y `genre`.

<details>
<summary> Ver Solución</summary>

```python
class Song:
    def __init__(self, name, artist, album, genre):
        self.name = name
        self.artist = artist
        self.album = album
        self.genre = genre
        self.is_playing = False

    def play(self):
        self.is_playing = True
        print(f"Reproduciendo ahora: '{self.name}' de {self.artist}")

    def pause(self):
        self.is_playing = False
        print(f"Pausado: '{self.name}' de {self.artist}")

    def __str__(self):
        return f"'{self.name}' por {self.artist} (Álbum: {self.album} - Género: {self.genre})"

print("--- PRUEBAS DE LA CLASE SONG ---")
# Instanciando las nuevas canciones
song1 = Song("Smells Like Teen Spirit", "Nirvana", "Nevermind", "Grunge")
song2 = Song("Sweet Child O' Mine", "Guns N' Roses", "Appetite for Destruction", "Hard Rock")
song3 = Song("Back In Black", "AC/DC", "Back In Black", "Hard Rock")

# Probar __str__
print(song1)
print(song2)
print(song3)
print()

# Probar play y pause con la canción de Nirvana
song1.play()
print(f"¿Está sonando? {song1.is_playing}")
song1.pause()
print(f"¿Está sonando? {song1.is_playing}\n")
```

</details>

### Clase `Spotify`

Crea la clase Spotify que administrará las canciones:

1. **Atributos**:
   - `user_name` (`str`): Nombre del usuario.
   - `favorite_songs` (`list`): Lista que almacena objetos de tipo `Song`.
   - `playlists` (`dict`): Diccionario que almacena listas de reproducción, donde la clave es el nombre de la playlist y el valor es una lista de objetos `Song`.

2. **Métodos**:
   - `add_song_to_favorites(song)`: Agrega una `song` a `favorite_songs`. Devuelve `True` si la canción se agregó correctamente, o `False` si ya estaba en la lista.
   - `remove_song_from_favorites(song)`: Elimina una `song` de la `favorite_songs`, Devuelve `True` si la canción se eliminó correctamente, o `False` si no estaba en la lista.
   - `create_playlist(playlist_name)`: Crea una nueva playlist con el nombre dado. Devuelve `True` si la playlist se creó correctamente, o `False` si ya existía.
   - `add_song_to_playlist(playlist_name, song)`: Agrega una `song` a la playlist especificada. Devuelve `True` si la canción se agregó correctamente, o `False` si la playlist no existe.
   - `remove_song_from_playlist(playlist_name, song)`: Elimina una `song` de la playlist especificada. Devuelve `True` si la canción se eliminó correctamente, o `False` si la playlist no existe o la canción no estaba en ella.
   - `remove_playlist(playlist_name)`: Elimina la playlist especificada. Devuelve `True` si la playlist se eliminó correctamente, o `False` si no existía.

<details>
<summary> Ver Solución</summary>

```python
class Spotify:
    def __init__(self, user_name):
        self.user_name = user_name
        self.favorite_songs = []
        self.playlists = {}

    def add_song_to_favorites(self, song):
        if song not in self.favorite_songs:
            self.favorite_songs.append(song)
            return True
        return False

    def remove_song_from_favorites(self, song):
        if song in self.favorite_songs:
            self.favorite_songs.remove(song)
            return True
        return False

    def create_playlist(self, playlist_name):
        if playlist_name not in self.playlists:
            self.playlists[playlist_name] = []
            return True
        return False

    def add_song_to_playlist(self, playlist_name, song):
        if playlist_name in self.playlists:
            # Opcional: Podrías añadir un 'if song not in self.playlists[playlist_name]:' 
            # si no quieres permitir canciones duplicadas en una misma playlist.
            self.playlists[playlist_name].append(song)
            return True
        return False

    def remove_song_from_playlist(self, playlist_name, song):
        if playlist_name in self.playlists and song in self.playlists[playlist_name]:
            self.playlists[playlist_name].remove(song)
            return True
        return False

    def remove_playlist(self, playlist_name):
        if playlist_name in self.playlists:
            del self.playlists[playlist_name]
            return True
        return False

print("--- PRUEBAS DE LA CLASE SPOTIFY ---")
mi_spotify = Spotify("Walle")
print(f"Usuario activo: {mi_spotify.user_name}\n")

# -- Favoritos --
print("Agregando a favoritos:")
print("Agregado song1 (Nirvana):", mi_spotify.add_song_to_favorites(song1)) # True
print("Agregado song2 (Guns N' Roses):", mi_spotify.add_song_to_favorites(song2)) # True
print("Agregado song1 de nuevo:", mi_spotify.add_song_to_favorites(song1)) # False (ya existe)
print()

print("Eliminando de favoritos:")
print("Eliminado song2 (Guns N' Roses):", mi_spotify.remove_song_from_favorites(song2)) # True
print("Eliminado song3 (AC/DC):", mi_spotify.remove_song_from_favorites(song3)) # False (no estaba en la lista)
print()

# -- Playlists --
print("Gestionando Playlists:")
print("Crear playlist 'Clásicos del Rock':", mi_spotify.create_playlist("Clásicos del Rock")) # True
print("Crear playlist 'Clásicos del Rock' otra vez:", mi_spotify.create_playlist("Clásicos del Rock")) # False

print("Agregar canción (Nirvana) a 'Clásicos del Rock':", mi_spotify.add_song_to_playlist("Clásicos del Rock", song1)) # True
print("Agregar canción (AC/DC) a 'Clásicos del Rock':", mi_spotify.add_song_to_playlist("Clásicos del Rock", song3)) # True
print("Agregar canción a playlist inexistente:", mi_spotify.add_song_to_playlist("Pop Hits", song2)) # False

print("Quitar canción (Nirvana) de 'Clásicos del Rock':", mi_spotify.remove_song_from_playlist("Clásicos del Rock", song1)) # True

print("Eliminar playlist 'Clásicos del Rock':", mi_spotify.remove_playlist("Clásicos del Rock")) # True
print("Eliminar playlist inexistente:", mi_spotify.remove_playlist("Clásicos del Rock")) # False
```

</details>
