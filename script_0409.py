'''
Clase Miercoles 09 de Abril 

Hoy se estableceran conceptos y sitaxis basicas de la libreria PANDAS

'''

#* Intalar Libreria
#pip install pandas

#* Importar libreria
# import pandas as pd
# import numpy as np

# #* Crear un DataFrame desde un diccionario
# data = {
#     'Nombre': ['Ana', 'Luis', 'Carlos', 'Sofía'],
#     'Edad': [23, 25, 30, np.nan],
#     'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Madrid']
# }

# df = pd.DataFrame(data)

# #* Acceder a los datos 
# df.head()       # Primeras filas
# df.tail(2)      # Últimas 2 filas
# df['Nombre']    # Columna específica
# df.iloc[1]      # Fila por índice

# #* Descripcion basica
# df.describe()
# #df.info()
# df['Edad'].mean()
# df['Edad'].max()

# #* Filtrado de datos
# df2 = df.copy()

# #df2 = df2[df2['Ciudad'] == 'Madrid']
# df2 = df2[df2['Edad'] > 24]

# #* Limpiar datos
# #df.dropna(inplace=True)            # Eliminar nulos
# #df.fillna(0, inplace=True)           # Reemplazar nulos
# df.rename(columns={'Nombre': 'Nombre_Completo'}, inplace=True)

# #* Cargar y guardar CSV
# #df.to_csv('datos.csv', index=False)     # Guardar
# #df = pd.read_csv('data.txt', sep='\t')           # Cargar


# #* Agrupar y ordenar
# df.groupby(by='Ciudad')
# df.sort_values(by='Edad', ascending=False)


##################################
##################################
####### TRABAJANDO CON MB ########
##################################
import pandas as pd

df = pd.read_csv('data.txt', sep='\t')
df.head()
df.describe()

df = df[df['x'] <= 24325 + 100]
df = df[df['x'] >= 24325 - 100]
df = df[df['y'] <= 25175 + 100]
df = df[df['y'] >= 25175 - 100]

precio_cu = 4.5
costo_ryv = 1
den = 2.7
ton = 1000*den
costo_mina = 18
costo_planta = 19
recuperacion = 0.85
constante = 2204.62

df['Valor_Bloque'] = ton * (precio_cu - costo_ryv) * (df['ley'] / 100) * recuperacion * constante - ton * (costo_mina + costo_planta)
df['state'] = 0

for i in range(len(df)):
    if df.iloc[i][4] >= 0:
        df.iat[i, 5] = 1


print(df.describe())