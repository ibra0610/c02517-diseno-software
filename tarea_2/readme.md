# Tarea 2 - Javier Cruz C02517 

### Analice el código provisto identificando al menos 5 problemas de diseño 

1. En la clase `libro.py`, en la función `def calcular_popularidad(self):` no se sigue el principio open closed. Mantener los géneros de los libros de forma fija en el cálculo puede ocasionar problemas a la hora de dar mantenimiento al código en caso de tener que agregar un género nuevo.
2. En la clase `libro.py`, en la función `def es_antiguo(self):` se podría seguir de mejor forma el principio KISS, ya que tenemos un `if` y `else` innecesarios.
3. En la clase `libro.py`, en la función `def imprimir_datos(self):` podríamos tener problemas con el principio de SoC, esto debido a que la clase libro no debería encargarse de imprimir, esto puede ser realizado desde otra clase.
4. En la clase `biblioteca.py`, en la función `def agregar_libro(self):`, tenemos un problema de SRP ya que la capacidad de agregar un libro no debería incluir obtener la información del libro con `input`, esto puede completarse desde otra clase.
5. En la clase `biblioteca.py`, en la función `def generar_reporte(self):`, también tenemos otro problema con las responsabilidades (SoC), la biblioteca no debería encargarse de generar o imprimir la información, se podrían enviar los datos y completar esta tarea desde otro lugar. 

### Implemente las mejoras en un repositorio Git (opcional) o documento markdown para subir a Mediación Virtual. 

- [Link del repositorio de GitHub.](https://github.com/ibra0610/c02517-diseno-software.git) Los archivos para esta entrega se encuentran dentro de una carpeta tarea_2, la misma contiene una carpeta codigo_original, con el código del enunciado marcando los errores encontrados, y una carpeta codigo_mejorado con las mejoras implementadas luego de indentificar los errores.

### Documente los cambios realizados explicando: Problemas identificados, Soluciones implementadas, Buenas prácticas aplicadas 

1. Para el problema de la clase `libro.py`, en la función `def calcular_popularidad(self):` se modificó la función para calcular la popularidad de los libros basándose en un diccionario definido, de esta forma, si se agrega un género nuevo se puede modificar el diccionario sin tener que hacer cambios en el cálculo. Esto cumpliendo con la buena prática de "Open-Closed" de la siguiente forma:
```[python]
    def calcular_popularidad(self):

        popularidad_por_genero = {
            'novela': (50, 10),
            'ciencia': (70, 5),
            'historia': (40, 8)
        }
        base, divisor = popularidad_por_genero.get(self.genero,(10, 0))
        return base + (self.paginas / divisor if divisor > 0 else 0)
```
2. Para el problema de la clase `libro.py`, en la función `def es_antiguo(self):`. Se eliminó el `if`y `else` innecesarios. Siguiendo con el principio de "KISS" de la siguiente forma: 
```[python]
    def es_antiguo(self):
        return self.anio_publicacion < 1980
```
3. Para el problema de la clase `libro.py`, en la función `def imprimir_datos(self):` se modificó la función para que, en lugar de imprimir, retorne los datos del libro. Esto para asegurarse de que se cumple el principio de "SoC" de la siguiente forma:
```[python]
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
```
4. Para el problema de la clase `biblioteca.py`, en la función `def agregar_libro(self):` se modificó la función para que reciba la información necesaria para agregar un libro como parámetro, en lugar de obtenerla con `input` (que puede utilizarse desde otra clase o función), cumpliendo con el principio de SRP de la siguiente forma:
```[python]
    def agregar_libro(self, titulo, autor, genero, paginas, anio):
        
        l = Libro(titulo, autor, genero, paginas, anio)
        self.libros.append(l)
        print("Libro agregado!")
```
5. En la clase `biblioteca.py`, en la función `def generar_reporte(self):` se modificó la función para que, en lugar de imprimir, retorne las estadísticas de la biblioteca. Esto para asegurarse de que se cumple el principio de "SoC" de la siguiente forma:
```[python]
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
```


