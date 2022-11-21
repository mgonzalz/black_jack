cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}
print("***"*5, "\n")
print ("BLACK JACK", "\n")
print("***"*5, "\n")
#VALOR DE CADA CARTA
print("Cartas disponibles: {}".format(list(cartas.keys())))
print("Valor correspondiente de las cartas: {}".format(list(cartas.values())))
#LISTA CON PUNTOS CARTAS
print ("1. Valor de cada carta:")
for clave, valor in cartas.items():
    print(clave, ": ", valor)
#JUGADOR DOS CARTAS AL AZAR
print("Bienvenido al juego de Black Jack")
import random
carta_jugador = random.choice(list(cartas.keys()))
puntuacion = int(cartas[carta_jugador])
print("Ha seleccionado la siguiente carta ", carta_jugador, " teniendo un valor de: ", puntuacion)
input(print("¿Desea seleccionar otra carta?"))
if input == "si" or input == "Si":
    carta_jugador_2 = random.choice(list(cartas.keys()))
    puntuacion+=cartas[carta_jugador_2]
    print("Ha seleccionado las siguientes cartas ", carta_jugador, "y", carta_jugador_2," teniendo un valor de: ", puntuacion)
elif input == "no" or input == "No":
    print("Ha seleccionado la siguiente carta ", carta_jugador, " teniendo un valor de: ", puntuacion)
else:
    print("Opción no válida")
