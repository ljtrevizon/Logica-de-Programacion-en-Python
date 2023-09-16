import random

nro_azar = random.randint(1, 100)
ticket = int(input("Introduzca un numero: "))
intentos = 5

# el juego se termina cuando se adivina el
# numero o se acaban los intentos
while nro_azar != ticket and intentos >= 1:

    print("No atinaste al numero, te quedan ", intentos, "intentos")
    if nro_azar > ticket:
        print("es muy bajo")
    else:
        print("es muy alto")
    ticket = int(input("Introduzca otro numero: "))
    intentos -= 1

if intentos == 0:
    print("se te acabaron los intentos...perdiste")
else:
    print("Adivinó!!!")
