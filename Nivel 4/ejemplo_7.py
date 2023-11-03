import random
notas=[0,0,0,0,0,0,0,0,0,0]

def valores_aleatorios(notas):
    for i in range(10):
        notas[i]=random.randint(0,100)

def promedio_notas(notas):
    acum=0
    for i in range(10):
        acum=acum+notas[i]

    return acum/10

def contar_notas_mayores(promedio,notas):
    cont=0
    for i in range(10):
        if notas[i]>promedio:
            cont=cont+1
    return cont

def contar_notas_menores_cincuenta(notas):
    cont=0
    for i in range(10):
        if notas[i]<50:
            cont=cont+1
    return cont

def determinar_mayor_nota(notas):
    mayor=notas[0]
    for i in range (1,10):
        if notas[i]>mayor:
            mayor=notas[i]
    return mayor

def determinar_menor_nota(notas):
    menor=notas[0]
    for i in range (1,10):
        if notas[i]<menor:
            menor=notas[i]
    return menor
print(notas)
valores_aleatorios(notas)
print("Notas nuevas: ",notas)
promedio=promedio_notas(notas)
print("El promedio de notas es: ",promedio)
print("Cantida de alumnos que tuvieron una nota mayor al promedio: ",contar_notas_mayores(promedio,notas))
print("Cantida de alumnos que tuvieron una nota menor a 50: ",contar_notas_menores_cincuenta(notas))
print("La nota mayor fue: ",determinar_mayor_nota(notas))
print("La nota menor fue: ",determinar_menor_nota(notas))