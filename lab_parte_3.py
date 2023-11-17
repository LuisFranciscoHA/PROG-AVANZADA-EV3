#PARTE 3: Serialización pickle en forma abreviada
# Importar los módulos para trabajar con pickle y con archivos
import os
import pickle

Entradas=[
 ['correo','nombre','telefono'],
 ['juan@gmail.com','Juan','8123232323'],
 ['maria@gmail.com','Maria','5545454545'],
 ['diana@homail.com','Diana','4490909090']
]
# Muestra el contenido y el tipo del objeto Entradas, que es el
# objeto que deseamos serializar y transportar.
print(Entradas)
print(type(Entradas))

with open("Entradas.pickle","rb") as f:
 Recuperado=pickle.load(f)
# Compara el objeto Entradas con el objeto Recuperado
# deben ser iguales.
print(Entradas==Recuperado)
