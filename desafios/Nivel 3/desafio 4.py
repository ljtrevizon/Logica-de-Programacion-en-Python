monto_total_surcursales=0
for i in range(4):
    nombre_surcursal=input("Ingrese el nombre de la surcursal: ")
    monto_promedio_facturas=0
    cont_monto_menos_mil_facturas=0
    monto_total_facturas=0
    nro_facturas=0
    while True:
        print("---------------------")
        monto_base=float(input("Ingrese el monto base: "))
        cantidad_articulos=int(input("Ingrese la cantidad de articulos vendidos: "))
        print("---------------------")
        monto_iva=monto_base*0.16
        monto_total=monto_base+monto_iva
        monto_promedio=monto_total/cantidad_articulos
        print("Monto del IVA: ",monto_iva)
        print("Monto total: ",monto_total)
        print("Monto promedio: ",monto_promedio)
        monto_total_facturas=monto_total_facturas+monto_total
        nro_facturas=nro_facturas+1
        if monto_total<1000:
            cont_monto_menos_mil_facturas=cont_monto_menos_mil_facturas+1
        print("---------------------")
        resp=input("Quiere continuar? (S/N): ")
        if resp.upper() == "N":
            break
    if cont_monto_menos_mil_facturas>=0:
        porcentaje_montos_menos_mil=cont_monto_menos_mil_facturas/nro_facturas*100
    else:
        porcentaje_montos_menos_mil=0
    monto_promedio_facturas=monto_total_facturas/nro_facturas
    monto_total_surcursales=monto_total_surcursales+monto_total_facturas
    print("---------------------")
    print("Monto promedio de todas las facturas: ",monto_promedio_facturas)
    print("Porcentje de las facturas con un monto total a 1000: ",porcentaje_montos_menos_mil,"%")
    print("---------------------")
monto_promedio_surcursales=monto_total_surcursales/4
print("Monto promedio de las surcursales: ",monto_promedio_surcursales)