class Libro:

    def __init__(self, titulo, autor, genero, paginas, anio_publicacion, 
disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero  # 'novela', 'ciencia', 'historia'
        self.paginas = paginas
        self.anio_publicacion = anio_publicacion
        self.disponible = disponible
 
    def calcular_popularidad(self):

        popularidad_por_genero = {
            'novela': (50, 10),
            'ciencia': (70, 5),
            'historia': (40, 8)
        }
        base, divisor = popularidad_por_genero.get(self.genero, (10, 0))
        return base + (self.paginas / divisor if divisor > 0 else 0)

    def es_antiguo(self):
        return self.anio_publicacion < 1980

    def obtener_datos(self):
        return {
            "Título": self.titulo,
            "Autor": self.autor,
            "Género": self.genero,
            "Páginas": self.paginas,
            "Año": self.anio_publicacion,
            "Disponible": 'Sí' if self.disponible else 'No',
            "Popularidad": self.calcular_popularidad(),
            "Es antiguo": 'Sí' if self.es_antiguo() else 'No'
        }