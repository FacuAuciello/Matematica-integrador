#time para medir el tiempo de ejeucuion y random para generar plabaras alearorias y simular un texto
import time
import random

def generarTexto (cantidad):
    palabras = ["programacion", "python", "utn", "variables", "ayso", "oe", "matematica", "funciones"]
    resultado = []
    for i in range(cantidad):
        palabrasAzar = random.choice(palabras)
        resultado.append(palabrasAzar)
    return resultado