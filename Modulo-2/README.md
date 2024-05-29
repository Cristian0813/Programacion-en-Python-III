# MÓDULO 2

## Función y Ámbito de la Variable

Es esencial comprender los niveles de ámbito en Python y cómo se puede acceder a las cosas desde los cuatro niveles de ámbito diferentes. A continuación se presentan los cuatro niveles de ámbito y una breve explicación de dónde y cómo se utilizan.

### Niveles de Ámbito en Python

1. **Ámbito Local:** Se refiere a una variable declarada dentro de una función. Por ejemplo,
```python
    def get_total(a, b):
        total = a + b
        return total

    print(get_total(5, 2))
```

2. **Ámbito Cerrado:** Es cuando se declara una variable fuera de una función. Esto significa que se puede acceder desde cualquier lugar. Por ejemplo,
```python
    def get_total(a, b):
        total = a + b
        def double_it():
            double = total * 2
            print(double)
        double_it()
```

3. **Ámbito Global:** S Por ejemplo,
```python
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

```python
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
```python
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
```python
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

## Manejo de archivos: Almacenar contenido y organización

El manejo de archivos es una parte fundamental de la programación, ya que permite a los programas interactuar con el sistema operativo y almacenar datos de forma persistente. Este resumen se centra en los conceptos básicos de la creación, lectura, escritura y organización de archivos en Python.

**Crear un archivo:**

* La función `open()` junto con el modo "w" (escritura) se utiliza para crear un nuevo archivo.
* Ejemplo: `f = open("mi_archivo.txt", "w")`

**Escribir en un archivo:**

* El método `write()` se utiliza para escribir texto en un archivo abierto.
* Ejemplo: `f.write("Esta es una línea de texto.")`
* Es importante cerrar el archivo con `f.close()` cuando se haya terminado de escribir.

**Leer un archivo:**

* La función `open()` junto con el modo "r" (lectura) se utiliza para leer el contenido de un archivo.
* Ejemplo: `contenido = f.read()`
* Cerrar el archivo con `f.close()` es importante.

**Leer un archivo línea a línea:**

* El método `readline()` se utiliza para leer un archivo línea a línea.
* Ejemplo:

```python
    f = open("mi_archivo.txt", "r")
    linea = f.readline()
    while linea:
        print(linea)
        linea = f.readline()
    f.close()
```

**Escribir en un archivo existente:**

* La función `open()` con el modo "a" (agregar) se utiliza para agregar texto al final de un archivo existente.
* Ejemplo: `f.write("Más texto para el archivo.")`

**Organizar archivos:**

* Utilizar carpetas para crear una estructura jerárquica de archivos.
* Nombrar los archivos de forma descriptiva y consistente.
* Documentar la ubicación y el propósito de los archivos.
* Eliminar archivos innecesarios para evitar desorden.

**Ejemplo completo:**

```python
    def crear_archivo(nombre_archivo, contenido):
        """Crea un archivo y escribe contenido en él."""
        with open(nombre_archivo, "w") as f:
            f.write(contenido)

    def leer_archivo(nombre_archivo):
        """Lee el contenido de un archivo y lo devuelve como una cadena."""
        with open(nombre_archivo, "r") as f:
            contenido = f.read()
        return contenido

    def agregar_contenido_archivo(nombre_archivo, contenido):
        """Agrega contenido al final de un archivo existente."""
        with open(nombre_archivo, "a") as f:
            f.write(contenido)

    # Ejemplo de uso
    crear_archivo("archivos/mi_archivo.txt", "Este es un archivo nuevo.\n")
    contenido_archivo = leer_archivo("archivos/mi_archivo.txt")
    print(f"Contenido del archivo: {contenido_archivo}")

    agregar_contenido_archivo("archivos/mi_archivo.txt", "\nMás texto para el archivo.")
    nuevo_contenido_archivo = leer_archivo("archivos/mi_archivo.txt")
    print(f"Contenido del archivo después de agregar: {nuevo_contenido_archivo}")
```

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