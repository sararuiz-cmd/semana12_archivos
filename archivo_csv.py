import os

# Asegura que el script use su propia carpeta como ruta base
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("productos.csv", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        linea = linea.strip()
        if linea:  # Verifica que la línea no esté vacía
            datos = linea.split(",")
            print(" | ".join(datos))
archivo.close()