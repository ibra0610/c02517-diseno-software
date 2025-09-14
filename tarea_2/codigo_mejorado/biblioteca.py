from libro import Libro

class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, titulo, autor, genero, paginas, anio):
        
        l = Libro(titulo, autor, genero, paginas, anio)
        self.libros.append(l)
        print("Libro agregado!")
    
    def enviar_reporte(self):
        total = len(self.libros)
        if total == 0:
            return {"Total libros": 0, "Disponibles": 0, "Antiguos": 0, "Promedio de popularidad": 0}
        
        antiguos = sum(1 for l in self.libros if l.es_antiguo())
        disponibles = sum(1 for l in self.libros if l.disponible)
        popularidad_total = sum(l.calcular_popularidad() for l in self.libros)
        
        return {
            'total': total,
            'disponibles': disponibles,
            'antiguos': antiguos,
            'popularidad_promedio': popularidad_total / total
        }
