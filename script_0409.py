'''
Clase Miercoles 09 de Abril 

Hoy se estableceran conceptos y sitaxis basicas de la libreria PANDAS

'''

#* Intalar Libreria
#pip install pandas

#* Importar libreria
import pandas as pd

#* Crear un DataFrame desde un diccionario
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Sofía'],
    'Edad': [23, 25, 30, 22],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Madrid']
}

df = pd.DataFrame(data)
print(df)

#* Acceder a los datos 
df.head()       # Primeras filas
df.tail(2)      # Últimas 2 filas
df['Nombre']    # Columna específica
df.iloc[1]      # Fila por índice

#* Descripcion basica
df.describe()
df.info()
df['Edad'].mean()
df['Edad'].max()

#* Filtrado de datos
df[df['Ciudad'] == 'Madrid']
df[df['Edad'] > 24]

#* Limpiar datos
df.dropna()            # Eliminar nulos
df.fillna(0)           # Reemplazar nulos
df.rename(columns={'Nombre': 'Nombre_Completo'}, inplace=True)

#* Cargar y guardar CSV
df.to_csv('datos.csv', index=False)     # Guardar
#df = pd.read_csv('datos.csv')           # Cargar

#* Agrupar y ordenar
df.groupby('Ciudad')
df.sort_values(by='Edad', ascending=False)

