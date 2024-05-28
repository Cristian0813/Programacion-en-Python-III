# MÓDULO 2

## Función y Ámbito de la Variable

Es esencial comprender los niveles de ámbito en Python y cómo se puede acceder a las cosas desde los cuatro niveles de ámbito diferentes. A continuación se presentan los cuatro niveles de ámbito y una breve explicación de dónde y cómo se utilizan.

### Niveles de Ámbito en Python

1. **Ámbito Local:** Se refiere a una variable declarada dentro de una función. Por ejemplo,
    ```py
    def get_total(a, b):
        total = a + b
        return total

    print(get_total(5, 2))
    ```

2. **Ámbito Cerrado:** Es cuando se declara una variable fuera de una función. Esto significa que se puede acceder desde cualquier lugar. Por ejemplo,
    ```py
    def get_total(a, b):
        total = a + b
        def double_it():
            double = total * 2
            print(double)
        double_it()
    ```

3. **Ámbito Global:** S Por ejemplo,
    ```py
    special = 5
    def get_total(a, b):
        total = a + b
        print(special)
    ```

4. **Ámbito Integrado:** Se refiere a las palabras clave reservadas que Python usa para sus funciones integradas, como `print`, `def`, `for`, `in` y así sucesivamente.  Se puede acceder a las funciones con ámbito integrado en cualquier nivel.

---

# ¿Qué son las estructuras de datos?

Las estructuras de datos son formas de organizar y almacenar información en un computador para que se pueda utilizar de manera eficiente. Permiten a los programadores:

* Almacenar y recuperar datos de forma organizada.
* Realizar operaciones con los datos, como buscar, insertar, eliminar y modificar.
* Administrar la memoria de la computadora de forma eficiente.

**Tipos de estructuras de datos en Python:**

Python ofrece varias estructuras de datos integradas:

* **Listas:** Colecciones ordenadas de elementos.
* **Diccionarios:** Colecciones no ordenadas de pares clave-valor.
* **Tuplas:** Colecciones ordenadas e inmutables de elementos.
* **Conjuntos:** Colecciones no ordenadas de elementos únicos.

**Creación de estructuras de datos personalizadas:**

Además de las estructuras de datos integradas, Python permite crear estructuras personalizadas, como pilas (**stacks**), colas (**queues**) y árboles (**trees**).

**Elección de la estructura de datos adecuada:**

La elección de la estructura de datos adecuada depende de:

* El tipo de datos que se va a almacenar.
* Las operaciones que se van a realizar con los datos.
* El rendimiento que se desea obtener.

    ```py
    # Ejemplo de lista de números
    numeros = [1, 2, 3, 4, 5]
    print(numeros[2])  # Imprime el elemento en la posición 2 (que es 3)

    # Ejemplo de lista de cadenas
    nombres = ["Juan", "María", "Pedro"]
    print(nombres[1])  # Imprime el elemento en la posición 1 (que es "María")

    # Ejemplo de diccionario de ciudades
    ciudades = {"Colombia": "Bogotá", "Argentina": "Buenos Aires", "Chile": "Santiago"}
    print(ciudades["Colombia"])  # Imprime el valor asociado a la clave "Colombia" (que es "Bogotá")

    # Ejemplo de diccionario con clave numérica
    edades = {1: 30, 2: 25, 3: 40}
    print(edades[2])  # Imprime el valor asociado a la clave 2 (que es 25)

    # Ejemplo de tupla de nombres
    nombres_tupla = ("Juan", "María", "Pedro")
    print(nombres_tupla[1])  # Imprime el elemento en la posición 1 (que es "María")

    # Ejemplo de tupla con un solo elemento
    pais = ("Colombia",)  # Se necesita una coma al final para indicar que es una tupla
    print(pais[0])  # Imprime el único elemento de la tupla (que es "Colombia")

    # Ejemplo de conjunto de números
    numeros_set = {1, 2, 3, 4, 5}
    print(numeros_set)  # Imprime el conjunto completo (ordenado de forma aleatoria)

    # Ejemplo de conjunto de cadenas
    nombres_set = {"Juan", "María", "Pedro", "Pedro"}  # Se ignora el valor repetido "Pedro"
    print(nombres_set)  # Imprime el conjunto sin elementos duplicados (ordenado de forma aleatoria)
    ```

### Mutabilidad e Inmutabilidad

- **Mutables:** Pueden modificarse después de su creación. Ejemplo: lista.
- **Inmutables:** No pueden modificarse después de su creación. Ejemplo: tupla.

---

# Elegir y utilizar estructuras de datos   

## ¿Qué estructura de datos elegir?

Elegir la estructura de datos adecuada es crucial para el rendimiento y la eficiencia. Factores como tamaño, velocidad y rendimiento influyen en la elección. Veamos un ejemplo práctico.

### Ejemplo: Lista de Empleados

Para encontrar un empleado por su ID, podemos usar una lista o un diccionario.

**Uso de Lista:**
```py
employee_list = [
    {"id": 12345, "name": "John", "department": "Kitchen"},
    {"id": 12458, "name": "Paul", "department": "House Floor"}
]

def get_employee(id):
    for employee in employee_list:
        if employee['id'] == id:
            return employee

print(get_employee(12458))
# OUTPUT: {'id': 12458, 'name': 'Paul', 'department': 'House Floor'}
```

Este enfoque funciona bien con pocas entradas, pero se vuelve ineficiente a medida que la lista crece.

**Uso de Diccionario:**
```py
employee_dict = {
    12345: {"id": "12345", "name": "John", "department": "Kitchen"},
    12458: {"id": "12458", "name": "Paul", "department": "House Floor"}
}

def get_employee_from_dict(id):
    return employee_dict[id]

print(get_employee_from_dict(12458))
# OUTPUT: {'id': 12458, 'name': 'Paul', 'department': 'House Floor'}
```
El diccionario permite búsquedas rápidas sin importar el tamaño, ya que no necesita iterar por cada entrada.

---

### Recursos Adicionales

_Esta es una lista de recursos que pueden ser útiles a medida que avanza con el proceso de aprendizaje._ 

- Obtenga más información sobre las estructuras de datos Python (documentación de Python) en el sitio web de Python:
    * [Python.org - Estructuras de datos](https://docs.python.org/3/tutorial/datastructures.html)
- Explore las estructuras de datos comunes de Python en el sitio web Real Python:
    * [Real Python - Estructuras de datos](https://realpython.com/python-data-structures/)

- Obtenga más información sobre excepciones y errores en Python en el sitio web de Python:
    * [Exceptions and Errors in Python - Python docs](https://docs.python.org/3/library/exceptions.html)
    
- Consulte el sitio web PyNative para obtener más información sobre la gestión de archivos en Python:
    * [File handling in Python](https://pynative.com/python/file-handling/)


---

**_Licencia:_**
Este curso está licenciado bajo los términos y condiciones de Coursera. Para más detalles sobre la licencia, por favor consulta los [Términos de Servicio de Coursera](https://www.coursera.org/about/terms).