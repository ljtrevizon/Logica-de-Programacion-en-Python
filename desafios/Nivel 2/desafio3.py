
for i in range (30):
    print("Tipo de boleto:")
    print("Primer tipo (v/V): 50$")
    print("Segundo tipo (p/P): 30$")
    print("Tercer tipo (G/g): 15$")
    tipo_boleto=input("Introduzca el tipo deseado: ")
    numero_boleto=int(input("Introduzca la cantidad deseada de boletos: "))
    if tipo_boleto.upper()=="V":
        subtotal=50*numero_boleto
    else:
        if tipo_boleto.upper()=="P":
            subtotal=30*numero_boleto
        else:
            if tipo_boleto.upper()=="G":
                subtotal=15*numero_boleto
    if subtotal<200:
        print("No hay descuento")
        descuento=0
    else:
        if subtotal <=400:
            print("El descuento es del 5%")
            descuento=5
        else:
            if subtotal <=1000:
                print("El descuento es del 7%")
                descuento=7
            else:
                print("El descuento es del 10%")
                descuento=10
    print("---------------------")