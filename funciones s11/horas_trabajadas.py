#Determinar con una función el valor a pagar por las horas trabajadas
print("----Programa para determinar el total a pagar por horas laboradas----")
def total(a):
    if a<160:
        a=a*6.5
    else:
        a=(160*6.5)+((a-160)*7.5)
    return a
while True:
    try:
        horas=int(input("Ingresa el numero de horas laboradas: "))
        if horas<0:
            print("Ingrese un número positivo")
        else:
            calculo=total(horas)
            print("-----------------------------------------------------------------")
            print(f"el total a pagar por las {horas} horas trabajadas es de: ${calculo:.2f}")
            break
    except ValueError:
        print("Ingrese un número válido")
