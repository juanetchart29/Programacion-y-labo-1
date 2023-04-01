precio_bruto = 0
acumulador_peso = 0
descuento = "No hay descuento"

bandera_alimento_caro = True

contador_precio = 0
acumulador_precio = 0

sigue = "S"
while sigue == "S":
    #ingreso de datos
    peso = int(input("ingrese el peso: "))
    while peso < 10 or peso > 100:
        peso = int(input("error,ingrese un peso valido: "))
    
    precio = float(input("Ingrese el precio por kilo: "))
    while precio < 1 :
        precio = float(input("error,Ingrese el precio por kilo: "))
    
    tipo = input("ingrese el tipo (vegetal, animal, mezcla): ").capitalize()
    while tipo != "Vegetal" and tipo != "Animal" and tipo != "Mezcla":
        tipo = input("error,ingrese el tipo (vegetal, animal, mezcla):  ").capitalize()
    #logica      
    #A
    precio_bruto += precio * peso
    
    #B
    acumulador_peso += peso
    
    #C
    if bandera_alimento_caro :
        precio_alimento_caro = precio
        tipo_alimento_caro = tipo 
        bandera_alimento_caro = False
         
    elif precio_alimento_caro < precio:
        tipo_alimento_caro = tipo 
        precio_alimento_caro = precio 
    #D
    acumulador_precio += precio
    contador_precio += 1
    sigue = input("desea continuar ingresando productos? s/n").capitalize()
    #termina el bucle while
    
if acumulador_peso > 100:
    descuento = 15
elif acumulador_peso > 300:
    descuento = 25

precio_total = precio_bruto * (1+descuento/100)
promedio_precio = acumulador_precio / contador_precio

print(f"el importe bruto es de :{precio_bruto} ")
print(f"el descuento es de: {descuento} ")    
print(f"el importe con descuento es de: {precio_total}")
print(f"el tipo de alimento mas caro es: {tipo_alimento_caro}")
print(f"el promedio de precio por kilo es: {promedio_precio}")
   
    