# Para saltos de línea, se utiliza \n
# Abro el archivo en modo Write Extended
archivo="colores.txt"
f = open(archivo,"w+")
# Escribo 4 líneas adicionales.
f.write("Rojo\n")
f.write("Amarillo\n")
f.write("Verde\n")
# Agregando los elementos de un iterable
mas_colores=["Morado\n","Celeste\n","Rosa\n"]
f.writelines(mas_colores)
# Cierro el archivo.
f.close()
