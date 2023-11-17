# Verifica si existen los archivos de respaldo, en cuyo
# caso, se eliminan. Usa exists() y remove()
import os
if os.path.exists('agenda.csv.bak'):
 os.remove('agenda.csv.bak')
if os.path.exists('agenda.json.bak'):
 os.remove('agenda.json.bak')
# Verifica si existen los archivos de trabajo con datos, en cuyo
# caso, se renombran a sus equivalentes de respaldo.
# Usa exists() y rename()
if os.path.exists('agenda.csv'):
 os.rename('agenda.csv','agenda.csv.bak')
if os.path.exists('agenda.json'):
 os.rename('agenda.json','agenda.json.bak')
# Este código no genera salidas.