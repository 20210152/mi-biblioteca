class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo):
        """Agrega un libro a la biblioteca."""
        self.libros.append(titulo)

    def listar_libros(self):
        """Devuelve una lista de todos los libros en la biblioteca."""
        return self.libros

    def buscar_libro(self, titulo):
        """Busca un libro en la biblioteca y devuelve True si existe, False si no."""
        return titulo in self.libros