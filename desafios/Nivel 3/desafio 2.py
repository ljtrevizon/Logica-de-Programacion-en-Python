def leer_entradas():
    print("Ingrese los datos del articulo: ")
    c_u=int(input("Codigo numerico: "))
    ca=int(input("Cantidad del articulo: "))
    p=int(input("Precio unitario del articulo: "))
    return c_u,ca,p

def calculo_subtotal(p,c):
    return p*c

def mostrar(cantidad,codigo,precio,subtotal):
    print("Datos del articulo")
    print("Codigo numero: ",codigo)
    print("Cantidad: ",cantidad)
    print("Precio por unidad: ",precio)
    print("Subtotal: ",subtotal)

while True:
    codigo_numerico,cantidad,precio = leer_entradas()
    subtotal = calculo_subtotal(precio,cantidad)
    print("-----------------------")
    mostrar(cantidad,codigo_numerico,precio,subtotal)
    continuar = input("Desea continuar? S/N: ")
    if continuar.upper() == "N":
        break