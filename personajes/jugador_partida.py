from personajes.jugador_juego import jugador_del_juego

class gestorPartida:  
    def __init__(self):
        self.jugadores =[]

    def anadirJugador(self, nombre, rol_asignado):  
        nombre = input('Ingrese su nombre: ')
        rol_asignado = input('Ingrese su rol: ')
        self.jugadores.append(jugador_del_juego(nombre,rol_asignado)) 