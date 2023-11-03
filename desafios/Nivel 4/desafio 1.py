while True:
    signos_zodicales=["Aries","Tauro","Geminis","Cancer","Leo","Virgo","Libra","Escorpio","Sagitario","Capricornio","Acuario","Piscis"]
    estaciones=["Invierno","Otoño","Verano","Primavera"]
    mes=int(input("Introduzca el numero del mes en el que nacio: "))
    dia=int(input("Introuzca el dia de su nacimiento: "))
    if (mes==3 and dia>=21) or (mes==4 and dia<=19):
        print("Su signo zodiacal es: ",signos_zodicales[0])
    else:
        if (mes==4 and dia >=20) or (mes==5 and dia<=20):
            print("Su signo zodiacal es: ",signos_zodicales[1])
        else:
            if (mes==5 and dia>=21) or (mes==6 and dia<=20):
                print("Su signo zodiacal es: ",signos_zodicales[2])
            else:
                if (mes==6 and dia>=21) or (mes==7 and dia<=22):
                    print("Su signo zodiacal es: ",signos_zodicales[3])
                else:
                    if (mes==7 and dia >=23) or (mes==8 and dia<=22):
                        print("Su signo zodiacal es: ",signos_zodicales[4])
                    else:
                        if (mes==8 and dia >=23) or (mes==9 and dia<=22):
                            print("Su signo zodiacal es: ",signos_zodicales[5])
                        else:
                            if (mes==9 and dia >=23) or (mes==10 and dia<=22):
                                print("Su signo zodiacal es: ",signos_zodicales[6])
                            else:
                                if (mes==10 and dia>=23) or (mes==11 and dia<=21):
                                    print("Su signo zodiacal es: ",signos_zodicales[7])
                                else:
                                    if (mes==11 and dia>=22) or (mes==12 and dia<=21):
                                        print("Su signo zodiacal es: ",signos_zodicales[8])
                                    else:
                                        if (mes==12 and dia>=22) or (mes==1 and dia<=19):
                                            print("Su signo zodiacal es: ",signos_zodicales[9])
                                        else:
                                            if (mes==1 and dia>=20) or (mes==2 and dia<=18):
                                                print("Su signo zodiacal es: ",signos_zodicales[10])
                                            else:
                                                print("Su signo zodiacal es: ",signos_zodicales[11])
    if mes==11 or mes==12 or mes==1:
        print("La estacion en la que nacio es: ",estaciones[0])
    else:
        if mes==8 or mes==9 or mes==10:
            print("La estacion en la que nacio es: ".estaciones[1])
        else:
            if mes==5 or mes==6 or mes==7:
                print("La estacion en la que nacio es: ",estaciones[2])
            else:
                print("La estacion en la que nacio es: ",estaciones[3])

    resp=input("Desea seguir? S/N: ")
    if resp.upper() == "N":
        break