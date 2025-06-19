#Devolver el menor de los números
def menor(a,b,c):
    if a<b and a<c:
        minor=a
    if b<c and b<a:
        minor=b
    if c<a and c<b:
        minor=c
    return minor
print("---------Programa para calcular el menor de 3 números----------")
while True:
    try:
        num1=float(input("Ingresa el primer número: "))
        num2=float(input("Ingresa el segundo número: "))
        num3=float(input("Ingresa el tercer número: "))
        result=menor(num1,num2,num3)
        print(f"EL menor es {result}")
        break
    except ValueError:
        print("Ingresa un valor número")