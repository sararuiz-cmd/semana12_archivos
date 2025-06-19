#Tabla de multiplicar con funciones
def tabla(a):
    for i in range(1,11):
        print(f"{a} * {i} = {a*i}")
print("----Programa para saber las tablas de multiplicar de un número-----")
while True:
    try:
        numero=int(input("Ingrese un número entero: "))
        print("La tabla es: ")
        print(tabla(numero))
        break
    except ValueError:
        print("Ingrese sólo números")