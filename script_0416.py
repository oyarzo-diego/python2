""""
Clase miercoles 16 de abril
Temas: libreria numpy y aplicacion en pandas

"""
#? CREAR ARRAYS
#* Es una estructura de datos que permite almacenar una coleccion de elementos
#* del mismo tipo.
#* Se usan cuando se necesita eficiencia en el manejo de datos numericos

import numpy as np

# a = np.array([1, 2, 3])             # Array 1D
# b = np.array([[1, 2, 3 ], [3, 4, 5], [5, 6, 7]])      # Array 3D
# c = np.zeros((2, 3))                # Matriz 2x3 llena de ceros
# d = np.ones((3, 3))                 # Matriz 3x3 llena de unos
# e = np.eye(3)                       # Matriz identidad 3x3
# f = np.arange(0, 10, 2)             # [0 2 4 6 8]
# g = np.linspace(0, 1, 5)            # 5 valores entre 0 y 1

# #print(g)

# #? PROPIEDADES DE LOS ARRAYS
# a.shape       # Tamaño
# a.dtype       # Tipo de dato
# a.ndim        # Dimensión (1D, 2D, etc.)
# a.size        # Número total de elementos
# #print(f.size)

# #? OPERACIONES
# x = np.array([1, 2, 3])
# y = np.array([4, 5, 6])

# x + y         # [5 7 9]
# x * y         # [4 10 18]
# x.mean()      # Media
# x.std()       # Desviación estándar
# x.sum()       # Suma total

# #? INDEXACION
# a = np.array([[1, 2, 3], [4, 5, 6]])
# a[0, 1]       # 2
# a[:, 1]       # Segunda columna
# a[1, :]       # Segunda fila
# print(a[1, :])


#? EJEMPLO
# Simulación de 1000 valores de una distribución normal
# mu, sigma = 0.5, 0.3
# samples = np.random.normal(mu, sigma, 1000)
# print(samples)

# import matplotlib.pyplot as plt
# count, bins, ignored = plt.hist(samples, 30, density=True)
# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
#                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
#          linewidth=2, color='r')
# plt.show()

#? PANDAS
import pandas as pd

data = np.array([[1, 2], [3, 4], [5, 6]])
df = pd.DataFrame(data, columns=['A', 'B'])


df = pd.DataFrame({
    'Altura (cm)': np.random.normal(170, 10, 100),
    'Peso (kg)': np.random.normal(65, 15, 100)
})

media_altura = df['Altura (cm)'].mean()
matriz_covarianza = df.cov().to_numpy()


datos = np.random.randn(100, 4)  # 100 filas, 4 columnas
df = pd.DataFrame(datos, columns=["A", "B", "C", "D"])
estadisticas = df.describe(percentiles=[0.1, 0.5, 0.9])
print(estadisticas)

#? EJEMPLO PRACTICO CON MODELO DE BLOQUES
#* Filtrar el modelo en x/2 +/- 200 [m]; y/2 +/- 200 [m]; z <= 3500
#* Realizar analisis descriptivo de la ley
#* Crear ley2 random con estadisticas parecidas