import random

NOMBRES = ["Andres", "Sergio", "Mariana", "Isabel", "Nicolle"]
APELLIDOS = ["Calle", "Lopez", "Vargas", "Castrillon", "Baños"]


class Player():
    def __init__(self, nombre, apellido, numero, equipo, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.equipo = equipo
        self.edad = edad

    def presentation(self):
        return ("Hola soy {} {} y soy jugador del equipo {}".format(
            self.nombre, self.apellido, self.equipo))


class SoccerPlayer(Player):
    def __init__(self, nombre, apellido, numero, equipo, edad):
        super().__init__(nombre, apellido, numero, equipo, edad)
        self.anotaciones = 0
        self.asistencias = 0
        self.tarjetas = 0

    def presentation(self):
        return ("Hola soy {} {}".format(
            self.nombre, self.apellido))

    def anotar(self):
        self.anotaciones += 1

    def asistir(self):
        self.asistencias += 1

    def tarjeta(self):
        self.tarjetas += 1


def crear_equipo(equipo):
    equipo = []
    for i in range(11):
        nombre = random.choice(NOMBRES)
        apellido = random.choice(APELLIDOS)
        numero = random.randint(1, 99)
        edad = random.randint(16, 35)
        jugador = SoccerPlayer(nombre, apellido, numero, equipo, edad)
        equipo.append(jugador)
    return equipo


def juego(partido):
    random.choice(partido).anotar()
    random.choice(partido).asistir()
    # random.choice(partido).tarjeta()


def contar_goles(equipo):
    goles = 0

    for jugador in equipo:
        goles += jugador.anotaciones
    return goles


def main():
    medellin = crear_equipo("Medellin")
    nacional = crear_equipo("Nacional")

    partido = [medellin, nacional]

    for i in range(46):
        juego(random.choice(partido))

    goles_medellin = contar_goles(medellin)
    goles_nacional = contar_goles(nacional)

    if goles_medellin > goles_nacional:
        print("Gano Medellin con:", goles_medellin,
              "goles contra ", goles_nacional, "goles de nacional")
    elif goles_medellin < goles_nacional:
        print("Gano Nacional con:", goles_nacional,
              "goles contra ", goles_medellin, "goles de medellin")


if __name__ == "__main__":
    main()
