import random

dia = random.randint(0,8)

print("El dia es: ",dia)

match dia:
    case 1:
        print("Es lunes")
    case 2:
        print("Es martes")
    case 3:
        print("Es miercoles")
    case 4:
        print("Es jueves")
    case 5:
        print("Es viernes")
    case 6:
        print("Es sabado")
    case 7:
        print("Es domingo")
    case _:
        print("Dia invalido")