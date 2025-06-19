print("Programa para calcular la comisión a trabajadores")
def calculo(a):
    return a*0.10*3
venta_total=0
venta_semanas=[]
total=[]
while True:
    try:
        nombre_empresa=input("Ingresa el nombre de la compañía: ")
        break
    except ValueError:
        print("Error, ingresa un dato válido(letras, no números)")
try:
    numero_vendedores=int(input("Ingrese el número de vendedores contratados: "))
    if numero_vendedores>0:
        for i in range(1,numero_vendedores+1):
            sueldo=float(input(f"Ingrese el sueldo base del vendedor {i}: "))
            if sueldo>0:
                comision=calculo(sueldo)
                venta_semanas.append(comision)
                total_semana=sueldo+comision
                total.append(total_semana)

            else:
                print("Ingrese un número positivo")
                exit()
    else:
        print("Ingrese una cantidad positiva")
except ValueError:
    print("Ingrese datos válidos")

#SALIDAS
print("===============================================================")
print("-------------COMISIÓN DE VENTAS POR VENDEDOR-------------------")
print(f"NOMBRE DE LA COMPAÑÍA: {nombre_empresa}")
print("================================================================")
print("-----------REPORTE DE GANANCIAS POR SEMANA----------------------")
for i,j in enumerate(venta_semanas,start=1):
    print(f"El vendedor {i} obtuvo ganancias de ${j:.2f} en una semana")
print("----------- REPORTE DE GANANCIAS TOTALES---------------------------")
for h,k in enumerate(total,start=1):
    print(f"El vendedor {h} obtuvo ${k:.2f} ganancias en total")


