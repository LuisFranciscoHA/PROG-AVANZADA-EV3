# Abrir el archivo de datos CSV como Write Extended.
# Usar como apuntador de archivo "f".
# usa open() y el modo w+
f = open('agenda.csv','w+')
# Escribir los datos de la lista, como datos del CSV
# Usa for para leer la lista secuencialmente.
# Apóyate en F-String para el formato.
# No olvides el salto de línea.
Entradas=[
 ['correo','nombre','telefono'],
 ['juan@gmail.com','Juan','8123232323'],
 ['maria@gmail.com','Maria','5545454545'],
 ['diana@homail.com','Diana','4490909090']
]

for e in Entradas:
 f.write(f'{e[0]}|{e[1]}|{e[2]}\n')
# No olvides cerrar el archivo
f.close()
# Comprueba en tu directorio de trabajo, si ya existe el
# archivo de datos CSV.
# Este código no genera salidas
