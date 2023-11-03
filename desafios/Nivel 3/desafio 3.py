def leer_entradas():
    print("---------------------")
    nombre = input("Ingrese su nombre: ")
    nota = int(input("Ingrese su nota: "))
    monto = int(input("Ingrese el monto pagado: "))
    print("---------------------")
    return nombre,nota,monto

def mostrar(aprend_super,aprend_no_super,mont_pag,mont_pag_menos_cincuent):
    print("")
    print("Los estudiantes que superaron los desafios: ",aprend_super)
    print("Los estudiantes que no superaron los desafios: ",aprend_no_super)
    print("El total del monto pagado por los estudiantes: ",mont_pag)
    print("El total del monto pagado por los estudiantes que tienen menos de 50 pts: ",mont_pag_menos_cincuent)
    print("---------------------")


cont_aprend_super = 0
cont_aprend_no_super = 0
acum_mont_pag = 0
acum_mont_pag_menos_cincuent = 0
while True:
    nombre,nota,mont_pag = leer_entradas()
    if nota < 80:
        cont_aprend_no_super = cont_aprend_no_super+1
    else:
        cont_aprend_super = cont_aprend_super + 1
    acum_mont_pag = acum_mont_pag+mont_pag
    if nota < 50:
        acum_mont_pag_menos_cincuent = acum_mont_pag_menos_cincuent + mont_pag
    mostrar(cont_aprend_super,cont_aprend_no_super,acum_mont_pag,acum_mont_pag_menos_cincuent)
    seguir = input("Desea seguir? Y/N: ")
    if seguir.upper() == "N":
        break


