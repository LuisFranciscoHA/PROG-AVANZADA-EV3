# Grabando el JSON en un archivo.
import json
with open("archivo.json","w+") as f:
    json.dump(Original,f,indent=4)
# Leyendo datos de un archivo json
with open("archivo.json","r") as f:
     recuperados=json.load(f)
print(recuperados)
print("\n>> Comprobando igualdad de objetos.\n")
print(Original==recuperados)