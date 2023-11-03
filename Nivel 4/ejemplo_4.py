nombres=[]

i=0

while True:
    i=i+1
    print("Introduzca el nombre",i,": ")
    nomb=input()
    print("----------------")
    nombres.append(nomb)
    resp=input("Desea agregar otro nombre? (S/N): ")
    print("----------------")
    if resp.upper() == "N":
        break
print("Los nombres leidos fueron: ")
for nomb in nombres:
    print(nomb)
print("----------------")
