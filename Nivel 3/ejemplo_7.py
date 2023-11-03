acum_sueldo = 0

for i in range(1,5):
    sueldo=int(input('Introduzca el sueldo: '))

    acum_sueldo=acum_sueldo+sueldo

promedio = acum_sueldo/5

print("El total de los sueldos es: ",acum_sueldo)
print("El promedio de los sueldos es: ",promedio)