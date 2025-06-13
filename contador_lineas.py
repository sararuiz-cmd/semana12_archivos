#Contador de líneas
nombre=input("Ingrese el nombre del archivo: ")
try:
    with open(f'{nombre}',"r",encoding="utf-8") as archivo:
        lineas=archivo.readlines()
        print(f"El archivo tiene {len(lineas)} líneas")
        print("EL contenido del archivo: ")
        for linea in lineas:
            contenido=print(linea,end='')
            
except FileNotFoundError:
    print("El archivo no se encontró, por favor intente de nuevo")