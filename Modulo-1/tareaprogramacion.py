# Tareas de programación: Escribir entrada de fundición

# Objetivo
# - Comprender cómo y dónde utilizar la fundición implícita.

# Objetivos
# - Ejercicio 1: Utilizar la fundición explícita para aplicar el tipo de fundición correcto
# - Ejercicio 2: Corregir el script para que genere correctamente el total de la factura Instrucciones para el alumno

#-------------------------------------------------------------------------------------------------------------------

# Ejercicio-1
# Using explicit type conversion, change the following 
#   Usando la conversión explícita de tipos, cambia las siguientes 
# inputs so the types match with the following below
#   entradas para que los tipos coincidan con los siguientes
#  
# nombre = tipo cadena
#   name = type string
# edad = tipo int
#   age = type int
# altura = tipo float
#   height = type float
# lealtad = tipo booleano
#   loyalty = type boolean


# Modify the line below
# Modifica la línea de abajo
nombre = str(input('¿Cuál es tu nombre? '))
print(f"El tipo de la variable nombre es: {type(nombre)}. Debería ser <clase 'str'>")
print()
print("-----------------------------------------------------------------------------")
print()

# Modify the line below
# Modifica la línea de abajo
edad = int(input('¿Cual es tu edad? '))
print(f"El tipo de la variable edad es: {type(edad)}. Debería ser <clase 'int'>")
print()
print("-----------------------------------------------------------------------------")
print()

# Modify the line below
# Modifica la línea de abajo
altura = float (input('¿Cuál es tu altura en metros? '))
print(f"El tipo de variable de altura es: {type(altura)}. Debería ser <clase 'float'>")
print()
print("-----------------------------------------------------------------------------")
print()

# Modify the line below
# Modifica la línea de abajo
fidelidad = bool(input('¿Forma parte de nuestro programa de fidelidad? '))
print(f"El tipo de variable de fidelidad es: {type(fidelidad)}. Debería ser <clase 'bool'>")
print()
print("-----------------------------------------------------------------------------")
print()

#-------------------------------------------------------------------------------------------

# Ejercicio-2

# El siguiente script pedirá 3 entradas. Cada entrada se basará
# en el precio de los artículos - el precio es determinado por usted. La salida
# debe imprimir el total de las 3 entradas redondeado a 2 decimales, por ejemplo
#
# 1 café a 2,00
# 1 sándwich a 4,99
# 1 tarta a 2,75
#
# Su cuenta total es de $ 9.74

# The below script will ask for 3 inputs. Each input will be based
# on the price of the items - the price is determined by you. The output
# should print the total of the 3 inputs rounded to 2 decimal places e.g
#
#   1 coffee @ $ 2.00
#   1 sandwich @ $ 4.99
#   1 cake @ $ 2.75
#
#   Your total bill is $ 9.74

# Modifica la línea de abajo
café = float(input('1 café @: $ '))

# Modifica la línea de abajo
sandwich = float(input('1 sandwich @: $ '))

# Modificar la línea de abajo
tarta = float(input('1 tarta @: $ '))

total_factura = café + sandwich + tarta

print('Tu factura total es $', total_factura)
