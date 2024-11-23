 # biblioteca/__init__.py

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} de {self.autor}"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo, autor):
        nuevo_libro = Libro(titulo, autor)
        self.libros.append(nuevo_libro)
        return f"Libro '{titulo}' agregado."

    def listar_libros(self):
        if not self.libros:
            return "No hay libros en la biblioteca."
        return "\n".join(str(libro) for libro in self.libros)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return str(libro)
        return f"No se encontró el libro '{titulo}'."