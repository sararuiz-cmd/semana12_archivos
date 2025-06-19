"""
1.	Crear un programa que dado un monto para presupuesto anual de una fábrica calcule el porcentaje de dinero que le corresponde a cada departamento. El cálculo se realizará en una función que recibe como argumento el monto.
Recursos Humanos		50%
Manufactura			25%
Empaquetado		15%
Publicidad			10
"""
print("Programa para calcular el porcentaje correspondiente a cada departamento de una fábrica a partir del monto del presupuesto anual")
while True:
    try:
        monto_dinero=float(input("Ingrese el monto del presupuesto anual: "))
        if monto_dinero>0:
            break
        else:
            print("Ingrese un valor positivo")
    except ValueError:
        print("Ingrese un valor numeral")
def monto(dinero,porcentaje):
    return dinero*porcentaje
print("\n -----RESUMEN-----")
print(f"En el sector de Recursos Humanos {monto(monto_dinero,0.50)}")
print(f"En el sector de Manufactura {monto(monto_dinero,0.25)}")
print(f"En el sector de Empaquetado {monto(monto_dinero,0.15)}")
print(f"En el sector de Publicidad {monto(monto_dinero,0.10)}")

    