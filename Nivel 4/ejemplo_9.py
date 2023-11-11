# ambos arreglos estan relacionados entre ellos, es decir, son paralelos
# todos los arreglos deben el mismo tamaño
nombres = ["Jose","Pedro","Maria","Jesus"]
cedulas = ["123456","654321","789456","987654"]
apellidos = ["Rojas","Rodriguez","Martinez","Leon"]
edades = [50,25,50,43]

def consultar_datos(cedulas,nombres,edades,apellidos):
    print("Consultar datos")
    print("=================")
    cedulaBuscada=input("Ingrese la cedula a buscar: ")
    i=buscar_cedula(cedulas,cedulaBuscada)
    if i == -1:
        print("No esta registrada la cedula")
    else:
        print("Esta registrado")
        print("=================")
        print("Nombre:",nombres[i])
        print("Apellidos:",apellidos[i])
        print("Edad:",edades[i])
def buscar_cedula(cedulas,cedula):
    posicion=-1

    for i in range(len(cedulas)):
        if cedulas[i].upper() == cedula.upper():
            posicion=i
            break
    return posicion
def determinar_mayor_edades(edades):
    mayor=edades[0]
    for i in range(1,len(edades)):
        if edades[i] > mayor:
            mayor = edades[i]
    return mayor
def determinar_menor_edades(edades):
    menor=edades[0]
    for i in range(1,len(edades)):
        if edades[i] < menor:
            menor = edades[i]
    return menor


def mostrar_estadisticas(edades,nombres):
    promedio = calcular_promedio_edades(edades)
    edad_mayor = determinar_mayor_edades(edades)
    edad_menor = determinar_menor_edades(edades)
    print(len(edades),"alumnos registrados")
    print("El promedio de edades es",promedio)
    print("La mayor edad es: ",edad_mayor)
    print("La menor edad es: ",edad_menor)
    print("Los alumnos con mayor edad son: ")
    for i in range(len(edades)):
        if edades[i] > promedio:
            print(nombres[i])
    print("Los alumnos con edad igual al mayor: ")
    for i in range(len(edades)):
        if edades[i] == edad_mayor:
            print(nombres[i])
    print("Los alumnos con edad igual al menor: ")
    for i in range(len(edades)):
        if edades[i] == edad_menor:
            print(nombres[i])
def calcular_promedio_edades(edades):
    # len es una funcion que retorna la longitud de un arreglo
    n = len(edades)
    if n == 0:
        return 0
    else:
        acum = 0
        for i in range(n): 
            acum = acum + edades[i]

        return acum / n

def mostrar_arreglos(nombres,edades,apellidos,cedulas):
    print("N Cedulas  Nombres y Apellidos   Edades")
    print("==================================================")
    # se muestran los valores de los arreglos paralelos
    for i in range(4):
        print(i+1,cedulas[i],"  {0} {1:12}".format(nombres[i],apellidos[i]),"\t",edades[i])

def leer_arreglos(nombres,edades,cedulas,apellidos):
    for i in range(4):
        print("Introduzca el nombre",i+1,end=": ")
        nombres[i] = input()
        print("Introduzca el apellido",i+1,end=": ")
        apellidos[i]=input()
        print("Introduzca la edad",i+1,end=": ")
        edades[i] = int(input())
        print("Introduzca la cedula",i+1,end=": ")
        cedulas[i] = input()
        print("=================")


def mostrar_menu():
    print("=================")
    print("Opciones de Menu")
    print("=================")
    print("1. Leer datos")
    print("2. Consultar datos")
    print("3. Mostrar datos")
    print("4. Ver estadisticas")
    print("5. Salir")
    print("")
    print("Selecciona una opcion",end=": ")
    menu= int(input())
    print("=================")
    return menu

# cuerpo principal
while True:
    match mostrar_menu():
        case 1: 
            leer_arreglos(nombres,edades,cedulas,apellidos)
        case 2:
            consultar_datos(cedulas,nombres,edades,apellidos)
        case 3: 
            mostrar_arreglos(nombres,edades,apellidos,cedulas)
        case 4:
            mostrar_estadisticas(edades,nombres)
        case 5: 
            break
        case _:
            print("Opción incorrecta, intente de nuevo") 