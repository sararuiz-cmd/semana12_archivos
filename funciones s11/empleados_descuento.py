#Determinar cuánto se le pagará a cada empleado
print("----Programa para determinar el total a pagar para cada empleado----")
def descuento(a):
    return a-(a*0.10)
lista_total=[]
try:
    numero_empleados=int(input("Ingrese la cantidad de empleados: "))
    if numero_empleados>0:
        for i in range(1,numero_empleados+1):
            salario=float(input(f"Ingresa el salario del empleado {i}: "))
            if salario>0:
                total=descuento(salario)
                lista_total.append(total)
            else:
                print("El número ingresado debe ser positivo")
    else:
        print("Ingrese solo datos positivos")
except ValueError:
    print("Ingrese un dato válido")
print("================================================================")
print("------------------TOTAL A PAGAR POR CADA EMPLEADO----------------")
for i,j in enumerate(lista_total,start=1):
    print(f"Al empleado {i} se le debe de pagar una cantidad de C${j}")
