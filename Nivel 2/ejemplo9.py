import random

edad = random.randint(0,100)
print("La edad es ",edad,"años")
descuento = 0
# entre (5,10] no toma el extremo inferior 5 pero si toma el extremo superior 10
if edad>5 and edad<=10: 
    print("Es un niño")
    descuento = 5
else:
    # [30,40) toma el extremo inferior 30 pero no toma el extremo superior 40
    if edad>=30 and edad<40: 
        print("Esta en sus treinta")
        descuento = 10
    else:
        # [60,70) toma el extremo inferior (el 70) pero no toma el extremo superior
        if edad>=60 and edad<70:
            print("es un sexagenario")
            descuento = 50

print("el descuento asignado es de ",descuento,"%") 