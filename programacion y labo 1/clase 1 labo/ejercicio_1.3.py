#ejercicio 1.3 "gala de gran hermano
contadorF = 0

contadorNyJ = 0

edadJovenNacho = 0

contadorM = 0
contadorJ = 0
contadorN = 0
contadorTotal = 0

sigue = "S"

while sigue == "S":
    nombreVotante = input("ingrese su nombre:   ")
    edadVotante = int(input("Ingrese su edad:   "))
    if edadVotante >= 13:
        #inputs---
        genero = input("ingrese su genero (Masculino, Femenino, Otro)").capitalize()
        while genero != "Masculino" and genero != "Femenino" and genero!= "Otro":
            genero = input("error, ingrese un genero valido: (Masculino, Femenino, Otro)    ").capitalize()
        votado = input("ingrese el finalista al que desea votar, Nacho, Julieta o Marcos.   ").capitalize()
        while votado !="Nacho" and votado != "Julieta" and votado != "Marcos":
            votado = input("error,ingrese un finalista valido, Nacho, Julieta o Marcos.").capitalize()
        #logica---
        
        #punto A
        if genero == "Femenino":
            contadorF += 1
        
        match votado:
            case  "Nacho" :
                contadorN += 1
            #punto B
                if edadVotante > 24 and edadVotante < 41:
                    contadorNyJ += 1
            #punto C
                if edadVotante < edadJovenNacho:
                    nombreJovenNacho = nombreVotante
                edadJovenNacho = edadVotante  
            case "Julieta":
                contadorJ += 1
                if edadVotante > 24 and edadVotante < 41:
                    contadorNyJ += 1
            case "Marcos":
                contadorM += 1
            
        contadorTotal += 1     
        
    else:
        print("Para votar a los finalistas se debe ser mayor de 13 años")  
        
    sigue = input("desea ingresar otro votante ? s/n").capitalize()
#trmina el while

if contadorN != 0:
    porcenajeN = contadorTotal/contadorN * 100
    print(f"Del finalista Nacho se ingresaron {contadorN} votos")
    print(f"El porcentaje de votos es del {porcenajeN}")
else :
    print("no se ingresaron votos de Nacho")
    
if contadorJ != 0:
    porcenajeJ = contadorTotal/contadorJ * 100
    print(f"Del finalista Julieta se ingresaron {contadorJ} votos")
    print(f"El porcentaje de votos es del {porcenajeJ}")
else :
    print("no se ingresaron votos de Julieta")
    
if contadorM != 0:
    porcenajeM = contadorTotal/contadorM * 100
    print(f"Del finalista Marcos se ingresaron {contadorM} votos")
    print(f"El porcentaje de votos es del {porcenajeM}")
else :
    print("no se ingresaron votos de Marcos")
    
if contadorN > contadorM and contadorN > contadorJ:
    ganador = "Nacho"
elif contadorM > contadorJ:
    ganador = "Marcos"
else:
    ganador = "Julieta"
print(f"el/ la ganadora de Gran Hermano es: {ganador}")
        