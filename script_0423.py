import pandas as pd
import plotly.express as px

df = pd.read_csv('data.txt', sep='\t')

# Crear el histograma de la columna 'ley'
#fig = px.histogram(df, x='ley', nbins=30, title='Distribucion de Ley')

# Mostrar el gráfico
#fig.show()

# fig2 = px.histogram(
#     df, #Desde donde se extraen los datos
#     x = 'ley', #la variable que se quiere graficar
#     y = None, #Opcion para contar algo diferente a la frecuencia
#     color = None, #'ley', #Columna para colorear por categoría
#     nbins = 50, #Numero de barras
#     barmode = 'stack', # Como se apilan las barras: stack, overlay, relative
#     histnorm = 'percent', #Normalizacion: percent, probability
#     marginal = 'box', #Grafico adicional: rug, box, violin
#     title = 'Histrograma de ley'
# )
# fig2.show()

# fig3 = px.box(df, y='ley', title='Boxplot de la columna "ley"')

# fig3.show()

# fig4 = px.box(
#     df,               # datos
#     x = None,         # Eje X (usado cuando quieres agrupar por categorías)
#     y = 'ley',           # Eje Y (variable numérica)
#     color = None,       # Agrupación por color
#     points= 'outliers',      # Cómo mostrar los puntos individuales: outliers, all, suspectedoutliers, False
#     notched = False,    # Mostrar notch en la mediana
#     title = 'Boxplot de Ley',       # Título del gráfico
#     hover_data = None,  # Datos extra que se muestran al pasar el mouse
#     facet_col = None,   # Para crear subgráficos por columna
#     facet_row = None,   # Para subgráficos por fila
# )

# fig4.show()

import plotly.graph_objects as go

df = df[(df['z'] >= 2900) & (df['z'] <= 3300)] 
df = df[(df['x'] >= 24250) & (df['x'] <= 24450)]
df = df[(df['y'] >= 24550) & (df['y'] <= 24750)]
df = df[df['ley'] >= 0.55]

fig5 = go.Figure(data=[go.Scatter3d(
    x = df['x'],
    y = df['y'],
    z = df['z'],
    mode = 'markers',
    marker = dict(
        size = 8,
        color = df['ley'],                 # El color se basa en los valores de 'cu'
        symbol = 'circle',
        colorscale = 'Jet',                # Escala de color 'Jet'
        colorbar = dict(title="Ley de Cu", orientation = 'h' ),# Barra de color con título
        showscale = True                   # Mostrar la escala de color
    ),
    text = ["Cu (%) : {:.3f}".format(cu) for cu in df['ley']],  # Texto mostrado al pasar el mouse
    hoverinfo = 'text'                    # Mostrar solo la información de texto en el hover
)])

# Layout del gráfico (Ejes)
fig5.update_layout(
    scene=dict(
        xaxis_title="Easting",           # Título del eje X
        yaxis_title="Northing",          # Título del eje Y
        zaxis_title="Elevation",         # Título del eje Z
        aspectmode='data'                # Asegura que el aspecto del gráfico sea proporcional
    ),
    margin = dict(l=10, r=10, b=10, t=10)
)

fig5.show()


