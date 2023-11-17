# Recupera el contenido del archivo Entradas.pickle, y asígnalo a una
# lista llamada Recuperado. Recuerda que pickle es formato binario
# por lo que el tipo de contenido debe ser binario, al leer.
# Utilza with, open() en modo Read Binary, y load(), para
# el manejo de pickle con archivos.
import pickle
with open("Entradas.pickle","rb") as f:
 Recuperado=pickle.load(f)
# Compara el objeto Entradas con el objeto Recuperado
# deben ser iguales.
print(Entradas==Recuperado)