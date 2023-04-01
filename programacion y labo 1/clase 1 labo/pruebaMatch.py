contador1 = 0
contador2 = 0 
contador3 = 0
sigue = "s"
while sigue == "s":
    numero = int(input("ingrese un numero"))
    match numero:
        case 1 :
            contador1 += 1
        case 2: 
            contador2 +=1
        case 3:
            contador3 +=1
    sigue = input("desea continuar? s/n")
print(f"la cantidad de 1 = {contador1}")
print(f"la cantidad de 2 = {contador2}")
print(f"la cantidad de 3 = {contador3}")