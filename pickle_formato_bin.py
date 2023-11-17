# Se importa el módulo para trabajar con JSON.
import pickle
# Observa cómo pickle es un formato binario.
Original=[
 ['correo','nombre','telefono'],
 ['juan@gmail.com','Juan','8123232323'],
 ['maria@gmail.com','Maria','5545454545'],
 ['diana@homail.com','Diana','4490909090']
]

print("\n>> Serialización a Pickle.\n")
Original_pickle=pickle.dumps(Original)
print(Original_pickle)
print("\n>> Deserialización desde Pickle.\n")
Nueva_Lista=pickle.loads(Original_pickle)
print(Nueva_Lista)
print(type(Nueva_Lista))
print("\n>> Comprobando igualdad de objetos.\n")
print(Original==Nueva_Lista)

import json
# Grabando el JSON en un archivo.
with open("archivo.json","w+") as f:
 json.dump(Original,f,indent=4)
# Leyendo datos de un archivo json
with open("archivo.json","r") as f:
 recuperados=json.load(f)
print(recuperados)
print("\n>> Comprobando igualdad de objetos.\n")
print(Original==recuperados)

# Se importa el módulo para trabajar con JSON.
import pickle
# Observa cómo pickle es un formato binario.
print("\n>> Serialización a Pickle.\n")
Original_pickle=pickle.dumps(Original)
print(Original_pickle)
print("\n>> Deserialización desde Pickle.\n")
Nueva_Lista=pickle.loads(Original_pickle)
print(Nueva_Lista)
print(type(Nueva_Lista))
print("\n>> Comprobando igualdad de objetos.\n")
print(Original==Nueva_Lista)

# Grabando el pickle en un archivo.
with open("archivo.pickle","wb+") as f:
 pickle.dump(Original,f)
# Leyendo datos de un archivo pickle
with open("archivo.pickle","rb") as f:
 recuperados=pickle.load(f)
print(recuperados)
print("\n>> Comprobando igualdad de objetos.\n")
print(Original==recuperados)