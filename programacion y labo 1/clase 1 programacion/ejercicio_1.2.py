sigue = "S"
while sigue == "S":
    print("sobre cual regal de estilo de python desea informarse ?")
    print("""
    1-Sangría con 4 espacios
    2-Líneas de hasta 79 caracteres
    3-Líneas en blanco para separar bloques de código
    4-Nombres de variables expresivos
    5-Evitar abreviaturas de una letra
    6-Nombres de clases en CamelCase
    7-Nombres de funciones y variables en minúsculas
    8-Espacios alrededor de operadores y comas.""")

    eleccion = int(input("ingrese el respectivo numero"))
    while eleccion > 8 or eleccion < 1:
        print("error, ingrese un numero valido (1-8)")

    match eleccion:
        case 1:
            print("Python no usa corchetes para designar bloques. Utiliza sangrias de 4 espacios.")
            
        case 2:
            print("Las líneas no deben superar los 79 caracteres de longitud. Para una mayor legbilidad")
        case 3:
            print("Utilizar líneas en blanco para separar funciones y clases, y bloques lógicos dentro de una función.")
            
        case 4:
            print("Usar nombres de variables que sean significativos y expresivos.")
            
        case 5:
            print("Evitar abreviaturas o acrónimos de una sola letra en los nombres de variables, a menos que se utilicen comúnmente.")
            
        case 6:
            print("En las clases, el nombre de la clase debe estar en CamelCase, comenzando con una letra mayúscula.")
            
        case 7:
            print("Las funciones y variables deben tener nombres en minúsculas, separados por guiones bajos si es necesario para mayor claridad.")
            
        case 8:
            print("Utilizar espacios alrededor de operadores y después de comas en las listas, tuplas y argumentos de funciones, pero no en la parte interior de las expresiones")
    sigue = input("desea elegir otra de las reglas de estilo ? s / n").capitalize()
            
        