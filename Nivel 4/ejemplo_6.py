import random
notas=[0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    notas[i]=random.randint(0,100)

print(notas)

acum=0

for i in range(10):
    acum=acum+notas[i]

promedio = acum/10

print("El promedio de notas es: ",promedio)