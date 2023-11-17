with open("colores.txt","r") as f:
 contenido=f.read()
 print(contenido)
# Comprobando que, aunque no se aplicó close(), el archivo
# está cerrado.
print("¿Archivo cerrado?",f.closed)