import random
for i in range (5,0,-1):
    temp= random.randint(0,500)
    print("La temperatura",i," es: ",temp)
    if temp<=50:
        print("Grave")
    else:
        if temp<=100:
            print("Peligro")
        else:
            if temp<=200:
                print("Advertencia")
            else:
                if temp<=300:
                    print("Bien")
                else:
                    print("Optimo")