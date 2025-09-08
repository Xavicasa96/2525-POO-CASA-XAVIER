from libro import Libro
from usuario import Usuario
from biblioteca import Biblioteca

# Crear biblioteca
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "978-0307474728")
libro2 = Libro("Python para Todos", "Raúl González", "Programación", "978-1492051367")

# Agregar libros
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Crear usuarios
usuario1 = Usuario("Ana Pérez", "U001")
usuario2 = Usuario("Carlos López", "U002")

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("978-0307474728", "U001")

# Listar libros prestados
print("\nLibros prestados a Ana Pérez:")
biblioteca.listar_prestados("U001")

# Devolver libro
biblioteca.devolver_libro("978-0307474728", "U001")

# Buscar libro
print("\nResultados de búsqueda de 'Python':")
for libro in biblioteca.buscar_libro("Python"):
    print(libro)
