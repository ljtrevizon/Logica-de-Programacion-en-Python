cont=0
cont_may_mil = 0
acum_sueldo=0
acum_year = 0
cont_may_diez_year = 0
acum_may_diez_year = 0

while True:
    cont=cont+1

    sueldo=float(input('Introduzca el sueldo: '))
    year=int(input("Introduzca los anyos de servicio: "))

    if sueldo > 1000:
        cont_may_mil = cont_may_mil+1
    if year > 10:
        cont_may_diez_year = cont_may_diez_year+1
        acum_may_diez_year = acum_may_diez_year+year

    acum_sueldo=acum_sueldo+sueldo
    acum_year = acum_year + year

    continuar=input("Desea continuar? S/N: ")
    if continuar.upper() == "N":
        break


if cont_may_diez_year > 0:
    promedio_may_diez_year=acum_may_diez_year/cont_may_diez_year
else:
    promedio_may_diez_year=0

porcentaje_may_diez_year=cont_may_diez_year*100/cont
porcentaje_sueld_mil=cont_may_mil*100/cont
promedio_year = acum_year/cont
promedio_sueldo = acum_sueldo/cont


print("----------------")
print("El total de los empleados: ",cont)
print("El total de los trabajadores con mas de 10 anyos de servicios: ",cont_may_diez_year)
print("El total de los sueldos es: ",acum_sueldo)
print("El total de los anyos de servicio con mas de 10: ",acum_may_diez_year)
print("El total de los anyos de servicios es: ",acum_year)
print("El promedio de los anyos de servicio: ",promedio_year)
print("El promedio de los sueldos es: ",promedio_sueldo)
print("El promedio de los anyos de servicio con mas de 10: ",promedio_may_diez_year)
print("El porcentaje de las personas con sueldo mayor a mil: ",porcentaje_sueld_mil,"%")
print("El porcentaje de las personas con mas de diez anyos de servicio: ",porcentaje_may_diez_year)
print("----------------")
