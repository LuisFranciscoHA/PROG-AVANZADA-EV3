# Abro el archivo en modo Write Extended.
# Si el archivo no existe, lo genera. Si existe, lo remplaza.
# Los contenidos van en secuencia.
archivo="colores.txt"
f = open(archivo,"w+")
# Escribo 4 contenidos en secuencia.
f.write("Blanco")
f.write("Negro")
f.write("Naranja")
# Cierro el archivo.
f.close()
