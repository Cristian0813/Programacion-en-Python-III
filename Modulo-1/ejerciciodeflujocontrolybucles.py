# Ejercicio: utilice el flujo de control y los bucles para resolver un problema

# Introducción
# En este ejercicio, practicará el flujo de control con bucles para resolver problemas.
# Se le dará una lista de enteros y tendrá que agregar algún código para encontrar un número
# concreto en una lista y devolverlo. 

# Instrucciones
# 1. En num_list cree un bucle "for" nuevo e imprima cada valor de la lista en orden secuencial.
# 2. Dentro del bucle "for", cree una condición que busque todos los números mayores que
#    45 e imprima solo números quecumplan esa condición.
# 3. Cambie la sentencia "print" a "Más de 45" y agregue una condición "else" con una
#    sentencia "print" de "Menos de 45".
# 4. Actualice el bucle "for" para utilizar la función enumerar y poder obtener y utilizar
#    el índice. Modifique lacondición para buscar el número 36 e imprima lo siguiente:
#    "Número encontrado en la posición:", número de índice
# 5. A continuación, cree una nueva variable denominada "count", asígnele el valor
#    0 y ubíquela fuera del bucle "for".
# 6. Dentro del bucle "for" incremente el contador en 1.
# 7. Agregue una sentencia "print" fuera del bucle "for" para imprimir el valor de la variable "count".
# 8. Por último, agregue una sentencia "break" directamente luego de la sentencia "print"
#    dentro de la condición "if" paraencontrar el número. 

num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39, 53, 67, 89, 11]
count = 0 

for i, num in enumerate(num_list):
    print(num)
    
    if num > 45:
        print("Más de 45")
        
        break
    else:
        print("Menos de 45")

    if num == 36:
        print("Número encontrado en la posición:", i)
        break

    count += 1

print("Valor de count:", count)