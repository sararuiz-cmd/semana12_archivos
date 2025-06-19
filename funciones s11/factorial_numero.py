#Calcular el factorial de un número
def factorial():
    while True:
        try:
            a=int(input("Ingrese un número: "))
            if a>0:
                f=1
                for i in range(1,a+1):
                    f=f*i
                return f
            else:
                print("Ingrese un número positivo")
        except ValueError:
            print("Ingrese un número valido")
print("--------Programa para calcular el factorial de un número--------")
print(F"El factorial del número ingresado es {factorial()}")