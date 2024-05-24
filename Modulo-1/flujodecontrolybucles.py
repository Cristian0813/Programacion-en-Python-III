# PRACTIRCAR EL FLUJO DE CONTROL Y LOS BUCLES

"IF ELSE"
# En muchos casos, es posible que necesite buscar un elemento concreto en una lista.
# Una vez encontrado el elemento, no es necesario seguir repasando los demás resultados.
# Si utilizamos el ejemplo anterior, supongamos que solo necesita comprobar si el postre
# "Churros" está en la lista y, en caso afirmativo, imprimir una única sentencia. 

#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        print('Yes! One of my favorite desserts is', dessert)        

# Ejecutar el código anterior generará lo siguiente:
# 'Yes! One of my favorite desserts is Churros' 

# Pero, ¿qué pasa si busca un postre y ese postre no está en la lista? El código anterior
# no está configurado actualmente para resolver esta situación. Busquemos el postre "Pudding"
# que no está en la lista,y agreguemos también una sentencia else para manejar el caso de que
# no se encuentre. Si el postre no forma parte de la lista, imprimirá una nueva sentencia.

#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert) 
else:
    print('No sorry, that dessert is not on my list')

# Al ejecutar el código anterior se obtendrá la siguiente salida:
# 'No sorry, that dessert is not on my list'

#---------------------------------------------------------------------------------------------------------

# Sentencias de control de bucle

# Interrupción (break)
#El código funciona según lo previsto, pero puede notar un fallo. Si cambia el término de
# búsqueda a algo que está en la lista como "Churros" y lo ejecuta de nuevo, obtendrá el siguiente resultado:

# Yes one of my favorite desserts is Churros No sorry, not a dessert on my list

# ¡Esto no es lo que quiere! El postre está en la lista, pero aún se imprime en la condición else.
# Para solucionarlo, debe utilizar una instrucción de control denominada break. 

# Agregue lo siguiente:

#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert)
        break 
else:
    print('No sorry, not a dessert on my list')

# Ejecutar el código anterior resolverá el problema. La sentencia break se utiliza
# para detener el bucle, que a su vez también detiene la condición else . Sin break,
# el bucle continuará incluso después de que se cumpla la condición if.

#Continuar (continue)
# Al igual que break, continue se puede utilizar para controlar la iteración del bucle.
# La diferencia clave es que puede permitirle saltar una sección del bucle, pero luego
# continuar con el resto. Si cambia su código a este, notará que el resultado
# imprimirá todo excepto el postre Churros.

#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert) 


# Pase (pass)
# La sentencia pass le permite pasar por el bucle en su totalidad e ignorar eficazmente
# que se ha cumplido la condición if.

#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert) 
