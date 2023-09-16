import random

edad = random.randint(1, 100)
dia_semana = random.randint(1, 7)
hora_pelicula = random.randint(13, 21)

print("El dia de semana es: ", dia_semana)
print("La edad es: ", edad)
print("La hora de la pelicula es: ", hora_pelicula)

if (edad >= 60) or (dia_semana == 1) or (edad <= 10 and hora_pelicula < 17):
    print("Le toca pagar mitad de precio")
    descuento = 50
else:
    descuento = 0

print("el descuento es de ", descuento, "%")
