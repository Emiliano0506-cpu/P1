"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""

# Funcion o procedimiento que borre pantalla
def borrarPantalla():
    print("\033c")  # Este codigo es para borrar la pantalla en la terminal


# 1.- Funcion que no recibe parametros y no regresa valor
def funcion1():
    nombre = input("Ingresa tu nombre: ").strip().upper()
    apellido = input("Ingresa tu apellido: ").strip().upper()
    print(f"Hola soy {nombre} {apellido}")


# 3.- Funcion que recibe parametros y no regresa valor
def funcion3(nom, ape):
    nombre = nom.strip().upper()
    apellido = ape.strip().upper()
    print(f"Hola mucho gusto soy {nombre} {apellido}")


# 2.- Funcion que no recibe parametros y regresa valor
def funcion2():
    nombre = input("Ingresa tu nombre: ").strip().upper()
    apellido = input("Ingresa tu apellido: ").strip().upper()
    return nombre, apellido


# 4.- Funcion que recibe parametros y regresa valor
def funcion4(nom, ape):
    nombre = nom.strip().upper()
    apellido = ape.strip().upper()
    return nombre, apellido


# ==========================================
# Invocar las funciones
# ==========================================

# Prueba de función 1
funcion1()

# Prueba de función 3
nombre = input("Nombre: ").strip().upper()
apellido = input("Apellido: ").strip().upper()
funcion3(nombre, apellido)

# Prueba de función 2
nombre, apellido = funcion2()
print(f"El nombre del alumno es {nombre} {apellido}")

# Prueba de función 4
nombre = input("Nombre: ").strip().upper()
apellido = input("Apellido: ").strip().upper()
nom, ape = funcion4(nombre, apellido)
print(f"El nombre del alumno es: {nom} {ape}")