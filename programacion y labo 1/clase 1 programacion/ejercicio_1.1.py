acumulador_barbijo = 0
acumulador_jabon = 0 
acumulador_alcohol = 0 

marca_barbijo = []
marca_jabon = []
marca_alcohol = []

fabricante_barbijo = []
fabricante_jabon = []
fabricante_alcohol = []



acumulador_importe = 0

sigue = "S"
while sigue == "S":
    tipo = input("ingrese el tipo de producto: ").capitalize()
    while tipo != "Barbijo" and tipo != "Jabon" and tipo != "Alcohol":
        tipo = input("ingrese el tipo de producto: ").capitalize()
    cant = int(input(f"Ingrese la cantidad de '{tipo}': "))
    precio = float(input("Ingrese el precio: "))
    marca = input("Ingrese la marca: ")
    fabricante = input("Ingrese el fabricante: ")
    #logica--
    
    acumulador_importe += precio * cant
    
    match tipo:
        case "Barbijo":
            acumulador_barbijo += cant
            if not(marca in marca_barbijo):
                marca_barbijo.append(marca)
            if not(fabricante in fabricante_barbijo):
                fabricante_barbijo.append(fabricante)
                
        case "Alcohol":
            if not(marca in marca_alcohol):
                 marca_alcohol.append(marca)
            if not(fabricante in fabricante_alcohol):
                 fabricante_alcohol.append(fabricante)
            acumulador_alcohol += cant
        case "Jabon":
            if not(marca in marca_jabon):
                 marca_jabon.append(marca)
            if not(fabricante in fabricante_jabon):
                 fabricante_jabon.append(fabricante)
            acumulador_jabon += cant
    #termina el match
    
    sigue = input("desea seguir ingresando productos ?").capitalize()


#salida
print("las cantidades compradas de cada tipo son")
if acumulador_alcohol != 0:
    print(f"La cantidad del alcohol es: {acumulador_alcohol}")
    print(f"las marcas de alcohol son: {marca_alcohol}")
    print(f"los fabricantes de alcohol son: {fabricante_alcohol}")
    
else:
    print("No se realizaron compras de alcohol")    
if acumulador_jabon != 0:
    print(f"La cantidad del jabon es: {acumulador_jabon}")
    print(f"las marcas de jabon son {marca_jabon}")
    print(f"los fabricantes de jabon son: {fabricante_jabon}")
    
else:
    print("No se realizaron compras de jabon")    
if acumulador_barbijo != 0:
    print(f"La cantidad del barbijos es: {acumulador_barbijo}")
    print(f"las marcas de barbijo son {marca_barbijo}")
    print(f"los fabricantes de barbijo son: {fabricante_barbijo}")
    
else:
    print("No se realizaron compras de barbijos")    

print(f"el total de la compra fue: {acumulador_importe}")