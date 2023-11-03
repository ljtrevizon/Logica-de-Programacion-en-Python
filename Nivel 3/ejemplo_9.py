num_sueld=0
acum_sueldo = 0

while True:
    sueldo=float(input('Introduzca el sueldo: '))

    acum_sueldo=acum_sueldo+sueldo
    num_sueld=num_sueld+1
    continuar=input("Desea continuar? S/N: ")
    if continuar.upper() == "N":
        break

promedio = acum_sueldo/num_sueld
print("El total de los empleados: ",num_sueld)
print("El total de los sueldos es: ",acum_sueldo)
print("El promedio de los sueldos es: ",promedio)