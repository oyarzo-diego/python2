import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np

df = pd.read_csv('grafico_400m_sd.csv')
print (df.describe())

#? GRAFICO cota vs VAN vs TON
# Crear una figura con dos ejes Y
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Añadir la primera traza (ton) al eje izquierdo (primary)
fig.add_trace(
    go.Scatter(x=df['z'], y=df['ton_total'], name='Toneladas Mineral [t]', mode='lines+markers'),
    secondary_y=False,
)

# Añadir la segunda traza (VAN) al eje derecho (secondary)
fig.add_trace(
    go.Scatter(x=df['z'], y=df['USD_env'], name='VAN [USD]', mode='lines+markers', line=dict(dash='dash')),
    secondary_y=True,
)

# Configurar los títulos de los ejes
fig.update_layout(
    title_text='Gráfico de Toneladas y VAN según Cota',
    xaxis_title='Cota',
)

# Configurar los títulos de los ejes Y
fig.update_yaxes(title_text='Toneladas', secondary_y=False)
fig.update_yaxes(title_text='VAN', secondary_y=True)

fig.show()

#? GRAFICO ENVOLVENTE
envolvente = pd.read_csv('envolvente_3025.csv')
# Filtrar bloques de acuerdo al valor
envolvente = envolvente[envolvente['antes_max'] == 1].copy()

# Configurar los puntos y sus colores
x = envolvente['x']
y = envolvente['y']
z = envolvente['z']
valor = envolvente['valor'] / 1000000  # Escalado de valor

# Crear la figura en Plotly
fig2 = go.Figure()

# Agregar puntos en 3D que representan los bloques
fig2.add_trace(go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers',
    marker=dict(
        size=5,                  # Tamaño del "bloque"
        color=valor,             # Color en base al valor
        colorscale='jet',   # Escala de colores
        colorbar=dict(
            title="Valor de cada bloque [USDe6]",
            tickvals=np.linspace(-0.1, 0.2, 5),
            ticktext=[f'{v:.2e}' for v in np.linspace(-0.1, 0.2, 5)],
            titlefont=dict(size=20),
            tickfont=dict(size=15),
            len=0.5,             # Altura de la barra de color
            thickness=15,        # Grosor de la barra de color
            x=0.9,               # Posición de la barra de color en x
            y=0.5,               # Posición de la barra de color en y
        ),
        cmin=-0.1,
        cmax=0.2,
    )
))

# Configuración de la cuadrícula y el fondo
fig2.update_layout(
    scene=dict(
        xaxis=dict(showgrid=True, gridcolor='black', title='X', color='black'),
        yaxis=dict(showgrid=True, gridcolor='black', title='Y', color='black'),
        zaxis=dict(showgrid=True, gridcolor='black', title='Z', color='black'),
        bgcolor="white"
    ),
    title="Distribución de valor en bloques 3D",
)

fig2.show()

#? GRAFICAR FOOTPRINT
pares_xy = envolvente.groupby(['x','y'])['valor_acum'].max().copy()
coor_x = [point[0] for point in pares_xy.index.values]
coor_y = [point[1] for point in pares_xy.index.values]
valor_par = pares_xy.values
df = pd.DataFrame(columns=['x','y','valor'])
df['x']=coor_x 
df['y']=coor_y
df['valor']=valor_par.T
df = df[df['valor'] > 0]

fig3 = go.Figure()

fig3.add_trace(go.Scatter(
    x=df['x'],
    y=df['y'],
    mode='markers',
    marker=dict(
        symbol='square',        # Forma de marcador cuadrada
        size=20,                # Tamaño del marcador
        color=df['valor'],      # Color según el valor
        # colorscale=[(0, 'white'), (0.01, 'white'), (0.01, 'blue'), (1, 'red')],
        colorscale='turbo',   # Escala de color para los valores
        colorbar=dict(title="Valor"),
        # cmin=0.01,   # Valor mínimo de color en 0
        # cmax=df['valor'].max(),  # Valor máximo según los datos
        showscale=True
    )
))

fig3.update_layout(
    title="Valor Columnas en Footprint",
    xaxis_title="Coordenada X",
    yaxis_title="Coordenada Y"
)

fig3.show()
