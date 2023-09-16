import random

edad = random.randint(1, 100)
dia_semana = random.randint(1, 7)
hora_pelicula = random.randint(13, 21)

print("El dia de semana es: ", dia_semana)
print("La edad es: ", edad)
print("La hora de la pelicula es: ", hora_pelicula)

if dia_semana == 1:
    print("Lunes popular, el descuento es del 50%")
    descuento = 50
else:
    if edad >= 60:
        print("Es un adulto mayor, su descuento es del 50%")
        descuento = 50
    else:
        if edad <= 10 and hora_pelicula < 17:
            print("Es un nino, le toca un descuento del 50")
            descuento = 50
        else:
            descuento = 0

print("El descuento final es del: ", descuento, "%")
