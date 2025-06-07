#time para medir el tiempo de ejeucuion y random para generar plabaras alearorias y simular un texto
import time
import random

def generarTexto(cantidad):
    palabras = ["programacion", "python", "utn", "variables", "ayso", "oe", "matematica", "funciones"]
    resultado = []
    for i in range(cantidad):
        palabrasAzar = random.choice(palabras)
        resultado.append(palabrasAzar)
    return resultado

#algoritmo con lista de tuplas
def contarPalabrasLista(texto):
    conteo = []
    for palabra in texto:
        encontrado = False
        for i in range(len(conteo)):
            if conteo[i][0] == palabra:
                conteo[i] = (palabra, conteo[i][1] + 1)
                encontrado = True
        if not encontrado:
            conteo.append((palabra, 1))
    return conteo

#algoritmo con diccionario
def contarPalabrasDiccionario(texto):
    conteo = {}
    for palabra in texto:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

#medicion del tiempo de ejecucion/ expresamos en miliseg
tamaniosEntrada = [1000, 5000, 10000, 50000, 100000]

for numeros in tamaniosEntrada:
    texto = generarTexto(numeros)

    inicio = time.time()
    contarPalabrasLista(texto)
    fin = time.time()
    print(f"Lista - {numeros} palabras: {round((fin - inicio) * 1000, 2)} ms") 

    inicio = time.time()
    contarPalabrasDiccionario(texto)
    fin = time.time()
    print(f"Diccionario - {numeros} palabras: {round((fin - inicio) * 1000, 2)} ms")

#ejemplo

print ("20 palabras: ")
textoEjemplo = generarTexto(20)

print("Resultado con lista tuplas: ")
print(contarPalabrasLista(textoEjemplo))

print("Resultado del diccionario: ")
print(contarPalabrasDiccionario(textoEjemplo))
