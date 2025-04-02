## Clase Miercoles 04-02
## Ejercicios practicos de funciones, ciclos, listas, diccionarios y tuplas

# ## manejo de cadenas
# texto = 'Hola Mundo'
# print(texto.upper())
# print(type(texto))
# print(texto.lower())
# print(texto.split())

# ## Comprensiones
# result = [x**2 for x in range(10)]
# print(result)

# ## funcion lamba
# multiplicar = lambda x,y : x*y
# print(multiplicar(3,4))

# #* Funcion recibe lista de numeros y devuelve lista con pares
# def filtrar_pares(lista_numeros):
#     pares = []
#     for num in lista_numeros:
#         if num % 2 == 0:
#             pares.append(num)
#     return pares

# # Ejemplo de uso:
# numeros = [x for x in range(1,10+1)]
# print(filtrar_pares(numeros))  # Salida: [2, 4, 6, 8, 10]

# #*Contar veces que aparece una palabra
# def contar_palabras(frase):
#     palabras = frase.lower().split()
#     conteo = {}
#     for palabra in palabras:
#         if palabra in conteo:
#             conteo[palabra] += 1
#         else:
#             conteo[palabra] = 1
#     return conteo

# # Ejemplo de uso:
# # texto = "El sol brilla y el cielo está despejado"
# texto = input('Ingresa una oracion: ')
# print(contar_palabras(texto))  
# # # Salida: {'el': 2, 'sol': 1, 'brilla': 1, 'y': 1, 'cielo': 1, 'está': 1, 'despejado': 1}

# #* Listas y tuplas
# def mayores_de_edad(personas):
#     nombres = []
#     global x
#     x = 5
#     for nombre, edad in personas:
#         if edad >= 18:
#             nombres.append(nombre)
#     return nombres

# # Ejemplo de uso:
# datos = [("Ana", 25), ("Luis", 19), ("Carlos", 30), ("Marta", 19)]
# print(mayores_de_edad(datos))  # Salida: ['Ana', 'Carlos']
# print(x)

#* Adivinar el número
# import random

# def adivina_el_numero():
#     numero_secreto = random.randint(1, 2)
#     print(numero_secreto)
#     intentos = 0
#     while True:
#         intento = float(input("Adivina el número (0-1): "))
#         intentos += 1
#         if intento < numero_secreto:
#             print("¡Más alto!")
#         elif intento > numero_secreto:
#             print("¡Más bajo!")
#         else:
#             print(f"¡Correcto! Lo lograste en {intentos} intentos.")
#             break

# # Ejemplo de uso:
# adivina_el_numero()

#* Gestor de tareas
def gestor_tareas():
    tareas = []
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Completar tarea")
        print("3. Listar tareas")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            tarea = input("Describe la tarea: ")
            tareas.append({"tarea": tarea, "completada": False})
            print("✓ Tarea agregada.")
        elif opcion == "2":
            for i, tarea in enumerate(tareas):
                print(f"{i + 1}. {tarea['tarea']} ({'✓' if tarea['completada'] else '✗'})")
            num = int(input("Número de tarea a completar: ")) - 1
            tareas[num]["completada"] = True
            print("✓ Tarea marcada como completada.")
        elif opcion == "3":
            print("\n--- Tareas Pendientes ---")
            for tarea in tareas:
                if not tarea["completada"]:
                    print(f"- {tarea['tarea']} (✗)")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

# Ejemplo de uso:
gestor_tareas()


# #* Ejercicio por hacer 
# import math
# def calcular_circulo(radio):
#     area = math.pi * radio ** 2
#     perimetro = 2 * math.pi * radio
#     return (area, perimetro)  # Retorna una tupla

# # Ejemplo de uso (desempaquetando):
# a, p = calcular_circulo(5)
# print(f"Área: {a:.2f}, Perímetro: {p:.2f}")
# # Salida: Área: 78.54, Perímetro: 31.42

# #* Funcion avanzada JUEGO DEL AHORCADO
# import random

# def ahorcado():
#     palabras = ["python", "programacion", "computadora", "teclado", "desarrollo"]
#     palabra = random.choice(palabras)
#     letras_adivinadas = []
#     intentos = 6
    
#     while intentos > 0:
#         palabra_mostrada = ""
#         for letra in palabra:
#             if letra in letras_adivinadas:
#                 palabra_mostrada += letra
#             else:
#                 palabra_mostrada += "_"
#         print(f"\nPalabra: {palabra_mostrada}")
#         print(f"Intentos restantes: {intentos}")
        
#         if palabra_mostrada == palabra:
#             print("¡Ganaste! La palabra era:", palabra)
#             return
        
#         letra = input("Ingresa una letra: ").lower()
#         if letra in letras_adivinadas:
#             print("Ya usaste esa letra.")
#         elif letra in palabra:
#             letras_adivinadas.append(letra)
#         else:
#             intentos -= 1
#             print("Letra incorrecta.")
    
#     print("\n¡Perdiste! La palabra era:", palabra)

# # Ejemplo de uso:
# ahorcado()