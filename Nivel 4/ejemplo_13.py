import random

numeros=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def numeros_aleatorios(numeros):
    for i in range(len(numeros)):
        numeros[i] = random.randint(1,100)

def ordenar_ascendente(numeros):
    for i in range(len(numeros)-1):
        for j in range(len(numeros)-i-1):
            if numeros[j]>numeros[j+1]:
                aux=numeros[j]
                numeros[j]=numeros[j+1]
                numeros[j+1]=aux

def ordenar_descendente(numeros):
    for i in range(len(numeros)-1):
        for j in range(len(numeros)-1):
            if numeros[j]<numeros[j+1]:
                aux=numeros[j]
                numeros[j]=numeros[j+1]
                numeros[j+1]=aux

def mostrar_numeros(numeros):
    print(numeros)

numeros_aleatorios(numeros)
mostrar_numeros(numeros)
ordenar_ascendente(numeros)
mostrar_numeros(numeros)
ordenar_descendente(numeros)
mostrar_numeros(numeros)