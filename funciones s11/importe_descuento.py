# Función para calcular el total con el descuento aplicado
def calcular_descuento(monto):
    if monto > 700:
        descuento = 0.12
    elif monto > 500:
        descuento = 0.10
    elif monto > 300:
        descuento = 0.05
    else:
        descuento = 0.0

    total = monto * (1 - descuento)
    return total, descuento

# Programa principal
print("----------- Programa para calcular el total de una compra ------------")
while True:
    try:
        importe = float(input("Ingrese el costo inicial de su compra: $"))
        if importe > 0:
            total, desc = calcular_descuento(importe)
            print(f"Se aplicó un descuento del {desc * 100:.0f}%. Total a pagar: ${total:.2f}")
            break
        else:
            print("Ingrese un valor positivo.")
    except ValueError:
        print("Error: ingrese un número válido.")
