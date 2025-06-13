#Hacer un archivo que simule un diario
from datetime import date
fecha_actual=date.today()
nombre=input("Ingresa el nombre de tu diario: ")
texto=input("Ingresa el texto de tu diario: \n")

with open(f'{nombre}.txt',"a",encoding="utf-8") as archivo:
    archivo.write(f"Fecha de hoy: {fecha_actual}\n")
    archivo.write(f"Querido diario: \n")
    archivo.write(texto)

