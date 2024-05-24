# "Cheatsheet" de sintaxis de Python
#
# Esta lectura le proporciona una hoja con trucos que puede utilizar como referencia rápida.

#Espaciado
#Correcto
#any ammount of whitespace on a single line is ok
x     =        1        +        2
print(x) # 3

# Incorrecto

x = 1
+ 2
print(x) # 1

# Sangría
# Correcto

def say_hello():
    print("Hello there!")
print(say_hello())

def say_hello(): print("Hello there!")
print(say_hello())


# Incorrecto

def say_hello():
print("Hello there!") # print("Hello there!")
                      # ^

    def say_hello():
print("Hello there") # print("Hello there!")
                     # ^