## 
## Siempre comentar de que se trata el codigo
""""
en este codigo vamos a ver la sintaxis basica de python
fecha: 03
03_21
"""
#! SINTAXIS EN PYTHON

#? IDENTACION
# a = 10 #siempre trabajen con espacios
# b = 50

# if b > a:
#     print('b es mayor que a')
#     print('a es mayor que b')

#? VARIABLES
# los nombres de las variables no pueden llevar puntos, guiones ni empezar por numeros
# precio_cu = 4.5
# p_cu = 4.5

# x = 10 #interger --> numero entero
# y = 10.0 #float
# print(type(x))
# print(type(y))
# nombre = 'Juan' #str
# print(len(nombre))


# x = float(x)
# x = str(x)
# x = 10.5
# x = int(x)
# print(x)

x, y, z = 15, 20, 3

#? ESTRUCTURAS DE CONTROL

# if x > y:
#     print('x es mayor que y')
# elif y == x:
#     print(' y es mayor que x')
# elif z > x:
#     print('z es mayor que x')
# else:
#     print('no se cumple nada')

# # ciclos
# for x in range(5, 20+1, 5):
#     print(x)
#     if x <= 15:
#         print('x es menor o igal a 15')

# while x > 10:
#     print('x es mayor que 10')

#? FUNCIONES
# def Suma(a, b):
#     return a + b

# sumando = Suma(5, 10)
# print(sumando)

#? EXCEPCIONES
# try; except; finally

# try:
#     resultado = 10/0
# except ZeroDivisionError:
#     print('imposible dividir por cero')
# finally:
#     print('Fin del bloque try')

#? LIBRERIAS
# import math
# a = math.sqrt(16)
# print(a)

# import math as mt
# a = mt.sqrt(16)
# print(a)

# from math import sqrt
# a = sqrt(16)
# print(a)

#? OPERADORES COMUNES
# artirmeticos
# +; -; *; /; //(division entera); %(modulo); **(potencia)

#comparacion
# >; <; ==; >=; <=; !=

# if 4 != 5:
#     print('4 es diferente a 5')

#logicos 
# and; or; not

#?LISTAS Y DICCIONARIOS