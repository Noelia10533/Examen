from personajes.jugador_juego import jugador_del_juego
from personajes.jugador_partida import gestorPartida

def AccionNocturna(self, objetivo=None):  
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
    for j in self.jugadores:
        if j.Nombre == NombreVotado:
            if j.esta_vivo:
                j.esta_vivo=False
                return "El pueblo ha linchado a " + NombreVotado + " en la hoguera."
    return "Nadie fue linchado."   

def ComprobarVictoria(self):  
    
    list = sum(1 for j in self.jugadores if j.rol == "lobo" and j.esta_vivo)
    dict = sum(1 for j in self.jugadores if j.rol != "lobo" and j.esta_vivo)
    
    if list >= dict:
        return "¡Victoria de los Lobos!"
    elif list ==0:
        return "¡Victoria de los Aldeanos!"
    return "La partida debe continuar..."
