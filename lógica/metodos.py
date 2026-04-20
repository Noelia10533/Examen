

def AccionNocturna(self, objetivo=None):
    '''
    Define lo que ocurre durante la noche; a quién ha eliminado el lobo, qué ve el vidente y los aldeanos que siguen durmiendo
    :param objetivo: Variable que guarda el jugador señalado
    :type objetivo: string
    :returns: La secuencia final de los hechos
    '''  
    if not self.esta_vivo:
        return f"{self.Nombre} está muerto."
        
    if self.rol=="lobo": 
        if objetivo: 
            objetivo.esta_vivo=False
            return f"El lobo {self.Nombre} ha eliminado a {objetivo.Nombre}."
    elif self.rol== "vidente":
        if objetivo: 
            return f"La vidente {self.Nombre} ve que {objetivo.Nombre} es {objetivo.rol}."
    elif self.rol == "aldeano":
        return f"El aldeano {self.Nombre} duerme profundamente."
    return "Rol desconocido."

def VotacionDia(self, NombreVotado):
    '''
    Representa la votación que se hace para hechar al sospechoso lobo durante el día
    :param NombreVotado: Nombre del jugador que ha recibido la mayoría de votos
    :type NombreVotado: string
    :returns: La resolución de si se ejerce la votación o no
    '''
    for j in self.jugadores:
        if j.Nombre == NombreVotado:
            if j.esta_vivo:
                j.esta_vivo=False
                return "El pueblo ha linchado a " + NombreVotado + " en la hoguera."
    return "Nadie fue linchado."   

def ComprobarVictoria(self): 
    '''
    Comprobación de quien ha ganado, en caso de que alguien hubiese salido victorioso
    :returns: La resolución de la victoria si hubiera, sino se continua la partida
    ''' 
    lobos_vivos = sum(1 for j in self.jugadores if j.rol == "lobo" and j.esta_vivo)
    aldeanos_vivos = sum(1 for j in self.jugadores if j.rol != "lobo" and j.esta_vivo)
    
    if lobos_vivos >= aldeanos_vivos:
        return "¡Victoria de los Lobos!"
    elif lobos_vivos ==0:
        return "¡Victoria de los Aldeanos!"
    return "La partida debe continuar..."
