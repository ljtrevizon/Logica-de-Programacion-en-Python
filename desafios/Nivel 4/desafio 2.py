nombres_vendedores=[0,0,0,0,0,0,0,0,0,0]
montos_vendidos=[0,0,0,0,0,0,0,0,0,0]
facturas=[0,0,0,0,0,0,0,0,0,0]



def leer_datos(nombres,montos,facturas):
    for i in range(10):
        print("Ingrese el nombre del vendedor",i+1,end=": ")
        nombres[i]=input()
        print("Ingrese el monto vendido",i+1,end=": ")
        montos[i]=int(input())
        print("Ingrese el numero total de facturas procesadas",i+1,end=": ")
        facturas[i]=int(input())

def mostrar_datos(nombres,montos,facturas):
    print("N  Nombre      Monto       Facturas")
    print("--------------------------------------")
    for i in range(10):
        print(i+1," ",nombres[i],"      ",montos[i],"        ",facturas[i])

def promedio_montos(montos):
    cont=len(montos)
    if cont == 0:
        return 0
    else:
        acum=0
        for i in range(cont):
            acum=acum+montos[i]
        return acum/cont

def mayor_factura(facturas):
    mayor=facturas[0]
    for i in range(1,len(facturas)):
        if facturas[i]>mayor:
            mayor=facturas[i]
    return mayor

def mostrar_estadisticas(nombres,montos,facturas):
    promedio=promedio_montos(montos)
    mayor=mayor_factura(facturas)
    print("El promedio de todos los montos vendidos es:",promedio)
    print("Los vendedores con la mayor cantidad de facturas procesadas son:")
    for i in range(len(facturas)):
        if facturas[i]==mayor:
            print(nombres[i])

def mostrar_menu():
    print("------------------")
    print("Opciones de Menu")
    print("------------------")
    print("1. Leer datos")
    print("2. Mostrar lista")
    print("3. Ver estadisticas")
    print("4. Salir")
    print("")
    print("Selecciona una opcion",end=": ")
    menu= int(input())
    print("------------------")
    return menu

while True:
    match mostrar_menu():
        case 1:
            leer_datos(nombres_vendedores,montos_vendidos,facturas)
        case 2:
            mostrar_datos(nombres_vendedores,montos_vendidos,facturas)
        case 3:
            mostrar_estadisticas(nombres_vendedores,montos_vendidos,facturas)
        case 4:
            break
        case _:
            print("Error")