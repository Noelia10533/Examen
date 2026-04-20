

from lógica.metodos import AccionNocturna
from lógica.metodos import VotacionDia
from lógica.metodos import ComprobarVictoria
from personajes.jugador_partida import gestorPartida


juego=gestorPartida()
accion = AccionNocturna()
votacion = VotacionDia()
victoria = ComprobarVictoria()

print('INICIO DE LA PARTIDA')
juego

print('FASE 1: LA NOCHE')
accion

print('FASE 2: EL DÍA')
votacion
victoria


print(juego.jugadores[0].AccionNocturna(juego.jugadores[2]))
print(juego.ComprobarVictoria())


# Intenta estructurar el main.py con el siguiente orden.
# --- FASE 1: LA NOCHE 🌙 ---
# Comprobamos estado antes de que amanezca
# --- FASE 2: EL DÍA ☀️ ---
# El motor de la partida ejecuta el linchamiento
# --- FINAL DE LA PARTIDA ---