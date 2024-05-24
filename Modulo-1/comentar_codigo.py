# COMENTAR EL CÓDIGO

# Al finalizar esta lectura, podrá explicar por qué y dónde usar los comentarios en la codificación.
# Agregar comentarios al código no solo lo ayuda como desarrollador, sino que también ayuda a otros miembros de su equipo. 
# Los comentarios son excelentes para actualizar su memoria de código que puede haber escrito hace meses y es posible 
# que haya olvidado lo que se pretendía hacer. Existen varias razones por las que debe agregar comentarios a un archivo 
# de código. Que abarcan desde los siguientes:

# - Explicar la finalidad del código.
# - Informar a los desarrolladores que el código está obsoleto.
# - Agregar comentarios TODO para completar el trabajo más adelante.
# - A continuación se presentan ejemplos de los diferentes tipos de comentarios que se pueden utilizar.
#
# Comentarios de una línea
# 
# El uso de un símbolo # le dice a Python que ignore todo después de este punto hasta el final de la línea actual.

# Don't try to Run Me, I'm a comment
x = 10

# Comentarios en varias líneas
# Python realmente no tiene un método para declarar comentarios multilínea por lo que se puede usar un 
# símbolo # al principio de cada línea del comentario.

#---------------------------------------------------
# La siguiente función acepta dos enteros y
# suma ambos números para devolver el valor.
def add_two_numbers(a, b):
 return a + b


# Comentarios en línea
# El símbolo # le indica a Python que ignore todo después de este punto hasta el final de la línea actual,
# lo que permite colocar los comentarios dentro del código en sí. Los comentarios en línea deben utilizarse 
# para proporcionar información importante sobre el código con el que tratan.

x = 1 # Restablecer el tamaño del buffer

# Recuerde siempre tener una razón para un comentario, ya que deben proporcionar información al 
# lector y no ser una molestia que distraiga.