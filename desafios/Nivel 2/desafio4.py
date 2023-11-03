while True:
    edad = int(input("Ingrese la edad: "))
    dia = input("Ingrese el dia de la semana: ")
    hora_pelicula = int(input("Ingrese la hora de la pelicula (1 pm, 3 pm, 5 pm, 7 pm, 9 pm): "))
    descuento=0

    match hora_pelicula:
        case 1:
            precio_pelicula = 1
        case 3:
            precio_pelicula=2
        case 5:
            precio_pelicula=3
        case 7 | 9:
            precio_pelicula=4
        case _:
            print("Hora incorrecta")
            
    if edad < 2 or edad > 85:
        print("El descuento es del 100%.")
        descuento=100
    else:
        if (edad < 10 and (hora_pelicula==1 or hora_pelicula == 3 or hora_pelicula==5)) or dia.upper()=="LUNES":
            print("El descuento es del 50%")
            descuento=50
        else:
            print("No hay ningun descuento")
    monto_total=precio_pelicula-precio_pelicula*descuento/100
    print("El monto a pagar es: ",monto_total)
    print("-----------------")
    terminar=input("Desea continuar? (si/no): ")
    print("-----------------")
    if terminar.upper()=="NO":
        break