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
#ELECCIÓN CARTA DE LA BANCA
def banca_azar():
    import random
    carta_banca = random.choice(list(cartas.keys()))
    puntuacion_banca = int(cartas[carta_banca])
    return puntuacion_banca, carta_banca
puntuacion_banca, carta_banca = banca_azar()
puntuacion_banca2, carta_banca2 = banca_azar()
#JUGADOR DOS CARTAS AL AZAR
print("Bienvenido al juego de Black Jack")
import random
carta_jugador = random.choice(list(cartas.keys()))
puntuacion = int(cartas[carta_jugador])
print("Ha seleccionado la siguiente carta ", carta_jugador, " teniendo un valor de: ", puntuacion)
p = input("¿Desea seleccionar otra carta?")
print(p)
if p == "si" or p == "Si":
    carta_jugador_2 = random.choice(list(cartas.keys()))
    puntuacion+=cartas[carta_jugador_2]
    print("Ha seleccionado las siguientes cartas ", carta_jugador, "y",carta_jugador_2," teniendo un valor de: ", puntuacion)
    banca_azar()
    print("La banca ha seleccionado las siguientes cartas ", carta_banca, "y", carta_banca2, " teniendo un valor de: ", puntuacion_banca+puntuacion_banca2)
elif p == "no" or p == "No":
    print("Ha seleccionado la siguiente carta ", carta_jugador, " teniendo un valor de: ", puntuacion)
    banca_azar()
    print("La banca ha seleccionado la siguiente carta ", carta_banca, " teniendo un valor de: ", puntuacion_banca)
else:
    print("Opción no válida")
