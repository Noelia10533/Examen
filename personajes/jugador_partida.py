from personajes.jugador_juego import jugador_del_juego

class gestorPartida:  
    '''
    Esta clase representa los jugadores que van a jugar la partida con sus respectivos roles
    '''
    def __init__(self):
        '''Constructor de la clase que guarda los jugadores en una lista'''
        self.jugadores =[]

    def anadirJugador(self, Nombre, rol_asignado):  
        '''
        Añade jugadores a la partida con sus roles asignados
        :param nombre: Nombre del jugador
        :type nombre: string
        :returns: Nombre del jugador
        :param rol_asignado: Rol de este jugador
        :type rol_asignado: string
        :returns: Rol asignado al jugador
        '''
        Nombre = input('Ingrese su nombre: ')
        rol_asignado = input('Ingrese su rol: ')
        self.jugadores.append(jugador_del_juego(Nombre,rol_asignado)) 