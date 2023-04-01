acumulador_barbijos = 0
acumulador_jabon = 0 
acumulador_alcohol = 0 

acumulador_importe = 0
productos = {
    "Barbijo":[acumulador_barbijos,acumulador_importe,[],[]],
    "Jabon":[acumulador_jabon,acumulador_importe,[],[]],
    "Alcohol":[acumulador_alcohol,acumulador_importe,[],[]]
    }

sigue = "S"
while sigue == "S":
    tipo = input("ingrese el tipo de producto: ").capitalize()
    while tipo != "Barbijo" and tipo != "Jabon" and tipo != "Alcohol":
        tipo = input("ingrese el tipo de producto: ").capitalize()
    cant = int(input(f"Ingrese la cantidad de '{tipo}': "))
    precio = float(input("Ingrese el precio: "))
    marca = input("Ingrese la marca: ")
    fabricante = input("Ingrese el fabricante: ")
    #logica
    lista = productos.get(tipo)
    
    match tipo:
        case "Barbijo":
            acumulador_barbijos += cant
        case "Alcohol":
            acumulador_alcohol += cant
        case "Jabon":
            acumulador_jabon += cant
    
    sigue = input("desea seguir ingresando productos ?").capitalize()