import random

LIBROS1 = ["Fundamentos de ", "Introducción a la ", "Historia de la "]
LIBROS2 = ["Biología", "Química", "Física", "Anatomía", "Mecánica"]
NOMBRES = ["Andres", "Sergio", "Mariana", "Isabel", "Nicolle"]
APELLIDOS = ["Calle", "Lopez", "Vargas", "Castrillon", "Baños"]
REGISTRO = []

class Biblioteca():
    def _init_(self, nombre, apellido, libro, cantidad):
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
    
    def validar_existencias(self):
        if self.cantidad > 0:
            return ("Si hay existencia")
        elif self.cantidad == 0:
            return ("No hay existencia")
        
    def cantidad_libro(self):
        return ("Hay {} unidades del libro {} disponibles").format(self.cantidad, self.libro)
    
    def registrar(self):
        nombreapellido= (self.nombre + " " + self.apellido) 
        if nombreapellido not in REGISTRO:
            REGISTRO.append(nombreapellido)
        return("La persona {} {} ya ha sido registrada en la biblioteca.").format(self.nombre, self.apellido)

def crear_biblioteca(lugar):
    libros= []
    for i in range(2):
        l= random.choice (LIBROS1)
        l1= random.choice (LIBROS2)
        cantidad= random.randint(0,2)
        li= (l+l1, cantidad)
        libros.append (li)
    return libros

def main():
    ces = crear_biblioteca("CES")
    for i in ces:
        nombre=random.choice (NOMBRES)
        apellido = random.choice (APELLIDOS)
        libro=i[0]
        cantidad = i[1]
        b1= Biblioteca(nombre, apellido, libro, cantidad)
        print(b1.registrar())
        print(b1.cantidad_libro())
        print(b1.prestar_libro())
        print (" ")
    print("Usuarios registrados en la biblioteca: ", REGISTRO)

      
    
if __name__ == "_main_":
    main()