# Si el archivo existe, lo borra
import os
archivo="colores.txt"
# Si el archivo existe, lo elimina.
# Informa qué se hizo.
if os.path.exists(archivo):
 os.remove(archivo)
 print("\nEl archivo se eliminó")
else:
 print("\nEl archivo no existe. No se eliminó nada.")