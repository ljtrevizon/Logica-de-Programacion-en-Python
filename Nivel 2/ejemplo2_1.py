service_year=int(input("Introduzca los años de servicio: "))
dia_libre=input("Introduzca el dia libre: ")
dia_libre=dia_libre.upper()
bono = 0
sueldo = float(input("Introduzca el sueldo actual: "))
if dia_libre == "SABADO":
    bono=50
    sueldo_final=sueldo+bono
    print("Su nuevo sueldo es: ",sueldo)
if service_year>5 :
    aumento=sueldo*0.05
    print("Le toca un aumento el cual es: ",aumento)
    sueldo_final=sueldo+aumento
print("Sueldo final: ",sueldo_final)
