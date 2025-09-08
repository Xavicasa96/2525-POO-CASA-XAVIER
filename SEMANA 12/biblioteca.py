from libro import Libro
from usuario import Usuario

# Clase Biblioteca: gestiona libros y usuarios
class Biblioteca:
    def __init__(self):
        self.libros = {}       # ISBN -> Libro
        self.usuarios = {}     # ID -> Usuario
        self.ids_usuarios = set()  # IDs únicos

    # Agregar libro
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("El libro ya existe.")

    # Quitar libro
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            print(f"Libro eliminado: {self.libros.pop(isbn)}")
        else:
            print("El libro no existe.")

    # Registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario registrado: {usuario}")
        else:
            print("ID de usuario ya registrado.")

    # Prestar libro
    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros.pop(isbn)
            self.usuarios[id_usuario].libros_prestados.append(libro)
            print(f"Libro prestado: {libro} a {self.usuarios[id_usuario].nombre}")
        else:
            print("Libro o usuario no encontrado.")

    # Devolver libro
    def devolver_libro(self, isbn, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    print(f"Libro devuelto: {libro}")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no encontrado.")

    # Buscar libros
    def buscar_libro(self, clave):
        return [libro for libro in self.libros.values() if clave.lower() in libro.info[0].lower()
                or clave.lower() in libro.info[1].lower()
                or clave.lower() in libro.categoria.lower()]

    # Listar libros prestados de un usuario
    def listar_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")
