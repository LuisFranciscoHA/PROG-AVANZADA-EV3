# Se asume que el archivo colores.txt no existe en el
# directorio de trabajo.
import os
archivo="colores.txt"
# Informa si el archivo existe o no existe.
if os.path.exists(archivo):
 print("\nEl archivo ya existe")
else:
 print("\nEl archivo no existe")