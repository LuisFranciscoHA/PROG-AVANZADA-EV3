# Abro el archivo en modo lectura
archivo="colores.txt"
f = open(archivo,"r")
# Leo el contenido y se lo asigno a la variable
# contenido.
contenido=f.read()
# Muestro el contenido. Debe ser todo el archivo.
print(contenido)
# Cierro el archivo.
f.close()