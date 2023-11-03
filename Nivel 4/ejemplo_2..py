nombres=["","","","",""]

for i in range(5):
    print("--------------------")
    print("Introduzca el nombre",i+1,": ")
    nombres[i] = input()
print("--------------------")
print("Los nombres leidos: ")
for nomb in nombres:
    print(nomb)