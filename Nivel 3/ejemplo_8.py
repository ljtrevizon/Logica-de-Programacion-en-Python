n=int(input("Introduzca el total de empleados: "))
if n<=0:
    print("Tiene que ser mayor a 0")
else:
    acum_sueldo = 0

    for i in range(1,n+1):
        sueldo=int(input('Introduzca el sueldo: '))

        acum_sueldo=acum_sueldo+sueldo

    promedio = acum_sueldo/n

    print("El total de los sueldos es: ",acum_sueldo)
    print("El promedio de los sueldos es: ",promedio)