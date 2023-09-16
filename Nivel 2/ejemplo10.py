import random

edad = random.randint(0,100)

print("la edad es ",edad)
print("edad>=18", edad>=18)
print("edad<=25", edad<=25)
print("edad>=18 and edad<=25",edad>=18 and edad<=25)
print("edad>=40", edad>=40)
print("edad<=50", edad<=50)
print("edad>=40 and edad<=50",edad>=40 and edad<=50)

if (edad>=18 and edad<=25) or (edad>=40 and edad<=50):
    descuento=25
else:
    descuento=0

print("el descuento que le toca es ",descuento) 