import random

LIBROS1 = ["Fundamentos de ", "Introducción a la ", "Historia de la "]
LIBROS2 = ["Biología", "Química", "Física", "Anatomía", "Mecánica"]
NOMBRES = ["Andres", "Sergio", "Mariana", "Isabel", "Nicolle"]
APELLIDOS = ["Calle", "Lopez", "Vargas", "Castrillon", "Baños"]
REGISTRO = []

class Biblioteca():
    def __init__(self, nombre, apellido, libro, cantidad):
        self.nombre = nombre
        self.apellido = apellido
        self.libro = libro
        self.cantidad = cantidad

    def prestar_libro(self):
        if self.cantidad > 0:
            existencia = "Si hay existencia"
            self.cantidad = self.cantidad - 1
            return("{} del libro {}. Se presta el libro. Quedan {} unidades disponibles").format(existencia, self.libro, self.cantidad)
        elif self.cantidad == 0:
            existencia = "No hay existencia"
            return("{} del libro {}. No se puede prestar el libro").format(existencia, self.libro)
    
    def registro_existencias(self):
        if self.cantidad > 0:
            return ("Hay {} existencia(s) del libro {} disponibles".format(self.cantidad, self.libro))
        elif self.cantidad == 0:
            return ("No hay existencias del libro {}").format(self.libro)
    
    def registrar(self):
        nombreapellido= (self.nombre + " " + self.apellido) 
        if nombreapellido not in REGISTRO:
            REGISTRO.append(nombreapellido)
        return("La persona {} {} ya ha sido registrada en la biblioteca.").format(self.nombre, self.apellido)

def crear_biblioteca(lugar):
    libros= []
    numero_libros= random.randint(1,5)
    for i in range(numero_libros):
        l= random.choice (LIBROS1)
        l1= random.choice (LIBROS2)
        cantidad_libro= random.randint(0,10)
        li= (l+l1, cantidad_libro)
        libros.append (li)
    return libros

def persona_prestadora():
    nombre=random.choice (NOMBRES)
    apellido = random.choice (APELLIDOS)
    return (nombre, apellido)

def main():
    ces = crear_biblioteca("CES")
    for i in ces:
        nombre, apellido = persona_prestadora()
        libro=i[0]
        cantidad = i[1]
        b1= Biblioteca(nombre, apellido, libro, cantidad)
        print(b1.registrar())
        print(b1.registro_existencias())
        print(b1.prestar_libro())
        print (" ")
    print("Usuarios registrados en la biblioteca: ", REGISTRO)

if __name__ == "__main__":
    main()