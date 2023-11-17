# Se genera una lista vacía llamada Contactos
Contactos=[]
Entradas=[
 ['correo','nombre','telefono'],
 ['juan@gmail.com','Juan','8123232323'],
 ['maria@gmail.com','Maria','5545454545'],
 ['diana@homail.com','Diana','4490909090']
]
# Abrir el archivo de datos CSV, en modo de solo lectura.
# usa open, en modo r.
f = open('agenda.csv','r')
# Elabora un ciclo for, que coloque en una variable llamada
# linea a cada una de las líneas en el archivo apuntado
# como f. Recuerda que leer un archivo plano con for equivale
# a leerlo línea por línea.
for linea in f:
 # Asigna a una variable llamada lista_datos, el equivalente
 # en lista del contenido de datos, usando como separador
 # el pipe line. Usa split(), con "|" como delimitador.
 lista_datos=linea.split('|')
 print(lista_datos)
 # Elimina el salto de línea del último elemento de la lista
 lista_datos[2]=lista_datos[2].replace("\n","")
 # Agrega la lista de datos contenida en lista_datos
 # a la lista Contactos
 Contactos.append(lista_datos)
# Cerrar archivo
f.close()
# Imprime Entradas y Contactos, y comprueba que son iguales
print(Entradas)
print(Contactos)

#lab_import_libjson.py
import json

datos_json=json.dumps(Contactos,indent=4)
# Muestra el contenido serializado.
print(datos_json)

#Se hace otra vez este ejercicio
f = open('agenda.json','w+')
f.write(datos_json)
f.close()
# Este código no genera salidas.
# 
# 
# 
#JSON A LISTA
f = open('agenda.json','r')
# Carga el contenido JSON en una lista. Usa loads() y read().
# Almacena la lectura en una variable llamada Contactos_JSON.
Contactos_JSON=json.loads(f.read())
# Imprime Entradas, Contactos y Contactos JSON.
# Comprueba que son iguales.
print(Entradas)
print(Contactos)
print(Contactos_JSON)

