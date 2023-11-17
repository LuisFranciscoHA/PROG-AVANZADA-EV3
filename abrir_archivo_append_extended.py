# Se abre un archivo en modo Append Extended (a+). Si el archivo no
# existe, lo crea, con capacidad de lectura y escrituta. El
# apuntador de escritura se coloca al final del archivo.
import os
archivo="colores.txt"
f = open(archivo,"a+")
# Verificación de que ya se creo.
if os.path.exists(archivo):
 print("\nEl archivo ya existe")
else:
 print("\nEl archivo no existe")
# Se cierra el archivo.
f.close()