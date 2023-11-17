# Importa la librería para el soporte JSON
import json
# Almacena en una variable llamada datos_json, que almacene
# un volcado de datos. Utiliza dumps().
# Proporciona formato con identación a 4 posiciones.

datos_json=json.dumps(Contactos,indent=4)
# Muestra el contenido serializado.
print(datos_json)

#este lo colocque en lab_lista_contactos.py