import random

nro_azar = random.randint(1, 100)
intentos = 50

# el juego se termina cuando se adivina el
# se obliga a entrar al ciclo al menos una vez
while True:
    ticket = int(input("Introduzca un numero "))
    intentos -= 1
    if nro_azar == ticket:
        break
    else:
        print("No atinaste al numero")
        if intentos == 0:
            break  # se forzosamente rompe el ciclo
        else:
            print("te quedan ", intentos, "intentos")
            if nro_azar > ticket:
                print("es muy bajo")
            else:
                print("es muy alto")

if intentos == 0:
    print("se te acabaron los intentos...perdiste, el numero era ", nro_azar)
else:
    print("Adivinó en !!!")
