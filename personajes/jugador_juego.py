class jugador_del_juego:
    '''
    Representa todos los jugadores que están jugando, sus roles y si siguen vivos
    '''  
    def __init__(self, nombre, Rol): 
        '''Constructor de la clase que guarda los datos del jugador'''
        self.Nombre = nombre 
        self.rol=Rol 
        self.esta_vivo=True
    
    