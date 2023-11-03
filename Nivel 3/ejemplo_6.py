def mostrar_menu():
    print("================")
    print("MENU DE OPCIONES")
    print("================")
    print("1. Leer datos")
    print("2. Calcular sueldo")
    print("3. Mostrar salidas")
    print("4. Salir")
    print("================")
    return int(input())

def leer_datos(i):
    print("Introduzca el nombre del empleado #",i,": ")
    nombre = input()
    print("Introduzca los años de servicio del empleado #",i,": ")
    años = int(input())
    print("Introduzca el género del empleado #",i," (H:hombre,M:mujer): ")
    genero = input()

    return nombre,años,genero

def mostrar_salidas(cont_empleados,cont_emp_may10,cont_h_5_y_8):
    print("Se procesaron ",cont_empleados," empleados")
    print("En la empresa hay ",cont_emp_may10," empleados con mas de 10 años")
    print("En la empresa hay ",cont_h_5_y_8," empleados hombre con antiguedad entre 5 y 8 años")
    input()

# cuerpo principal
cont_empleados = 0
cont_emp_may10 = 0
cont_h_5_y_8 = 0
while True:
    opcion = mostrar_menu()
    match opcion:
        case 1:
            cont_empleados = cont_empleados + 1
            nombre,años,genero = leer_datos(cont_empleados)
            if años > 10:
                cont_emp_may10 = cont_emp_may10 + 1
            if  genero.upper() == "H" and años >= 5 and años <= 8:
                cont_h_5_y_8 = cont_h_5_y_8 + 1
        case 3:
            mostrar_salidas(cont_empleados,cont_emp_may10,cont_h_5_y_8)
        case 4:
            break
        case _:
            print("Introdujo una opcion incorrecta. Intente de nuevo")
# fin del ciclo