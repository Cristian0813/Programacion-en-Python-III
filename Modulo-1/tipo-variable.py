# Tipos de Datos en Python

# 1. Numéricos (Numeric):
#     - Estos tipos de datos representan números y se dividen en dos subtipos:
#     - Enteros (int): Representan números enteros, como 1, -5, 100, etc.
#     - Flotantes (float): Representan números decimales, como 3.14, -0.5, 2.718, etc.

# Numeric int
edad = 30
print(edad)  # Salida: 30
# Numeric Float
pi = 3.14159
print(pi)  # Salida: 3.14159

print()
print("------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------
print()

# 2. Secuenciales (Sequence):
#     - Estos tipos de datos contienen una secuencia de elementos y se dividen en tres subtipos:
#     - Cadenas (str): Representan texto y se definen entre comillas simples o dobles, como "Hola, mundo" o 'Python'.
#     - Listas (list): Son colecciones ordenadas de elementos, que pueden ser de diferentes tipos. 
#       Por ejemplo: `[1, 2, 3]` o `['manzana', 'banana', 'pera']`.
#     - Tuplas (tuple): Son similares a las listas, pero son inmutables (no se pueden modificar después de su creación).
#       Por ejemplo: `(10, 20, 30)`.

# Sequence str
nombre = "Juan"
print("Hola, " + nombre)  # Salida: Hola, Juan
# Sequence list
frutas = ["manzana", "banana", "pera"]
print(frutas[0])  # Salida: manzana
# Sequence tuple
coordenadas = (10, 20)
print(coordenadas)  # Salida: (10, 20)
print()

print("------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------
print()

# 3. Diccionarios (Dictionary):
#     - Los diccionarios (dict) almacenan pares clave-valor. Cada valor se asocia con una clave única.
#       Por ejemplo: `{'nombre': 'Juan', 'edad': 30}`.

# Dictionary
persona = {"nombre": "Juan", "edad": 30}
print(persona["nombre"])  # Salida: Juan

print()
print("------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------
print()
# 4. Booleanos (Boolean):
#     - Los valores booleanos (`True` o `False`) representan la lógica verdadero/falso en Python.
#       Se utilizan en expresiones condicionales y operaciones lógicas.

# Boolean
es_mayor_de_edad = True
print(es_mayor_de_edad)  # Salida: True

print()
print("------------------------------------------------------------------------------------")
#------------------------------------------------------------------------------------------
print()
# 5. Conjuntos (set):
#     - Los conjuntos son colecciones no ordenadas de elementos únicos. Se utilizan para operaciones de conjunto,
#       como unión, intersección, etc. Por ejemplo: `{1, 2, 3}`.

# set
numeros_primos = {2, 3, 5, 7}
print(numeros_primos)  # Salida: {2, 3, 5, 7}

