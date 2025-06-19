#Area de un círculo (con funciones)
def area():
    from math import pi
    while True:
        try:
            radio=float(input("Ingrese el radio del círculo: "))
            if radio>0:
                resultado=pi*(radio**2)
                return resultado
            else:
                print("Ingrese un número positivo")
        except ValueError:
            print("Ingrese un dato válido")
print("-----Programa para calcular el área de un çirculo-----")
print(f"El área del círculo es de: {area():.2f} cm^2")