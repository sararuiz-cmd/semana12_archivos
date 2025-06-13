#Generador de lista de compras
lista_productos=[]
cantidades=[]
archivo=open("compras.txt","w",encoding="utf-8")
lista_productos=[]
cantidades=[]
print("PROGRAMA PARA CREAR UN ARCHIVO CON UNA LISTA")
print("Ingrese la palabra 'fin' para terminar la lista")
while True:
    try:
        producto=input("Ingrese un producto: ")
        product=producto.capitalize()
        if product=="Fin":
            break
        lista_productos.append(product)
    except ValueError:
        print("Por favor, ingrese letras")
for i in lista_productos:
    while True:
        try:
            cantidad=int(input(f"Ingrese la cantidad del producto {i}: "))
            if cantidad>0:
                cantidades.append(cantidad)
                break
            else:
                print("Ingrese cantidades positivas")
        except ValueError:
            print("Ingrese sólo números enteros")

archivo.write("======================================================== \n")
archivo.write("                    LISTA DE COMPRAS                   \n")
archivo.write("=========================================================\n")
for i in range(len(lista_productos)):
    archivo.write(f"{lista_productos[i]}: {cantidades[i]}\n")
archivo.close()
       