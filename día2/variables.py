# Imprimir el valor de la variable
# print("Hello World")

# Sintaxis de python
if 5 == 5:
    print("El numero es igual a 5")
    
# Comentarios en python
"""
Comentario de varias lineas
Este es otro comentario
Mas comentarios por aquí
🖐️ Hey soy un comentario también
"""

# Variables en python
numero = 5
texto = "Hola Mundo"

# Imprimir el tipo de dato de la variable
# print(type(texto))

# Nombrar variables
numero4 = 5 # Si se puede
numero = 5 # Si se puede
numero_4 = 5 # Si se puede
miNumero = 5 # Si se puede
Numero = 6 # Si se puede
NUMERO = 7 # Si se puede
# 4numero = 5 # No se puede
# numero-4 = 5 # No se puede
# numero 4 = 5 # No se puede

# Declarar multiples variables
numero1, numero2, numero3 = 1, 2, 3
numero1 = numero2 = numero3 = 5

# Asignar valores a mi variable
numero = 5
numero = 6
numero = "numero"
numero = 5.5
numero = True
# print(numero)

# Variables
a = "Fácil"

def miFuncion():
    a = "Hermoso"
    # print("Python es " + a)
    # "Python es Hermoso"

miFuncion()

# print("Python es " + a)
# "Python es Fácil"

def miFuncion2():
    global b
    b = "Hermoso"

miFuncion2()

# print("Python es " + b)
# "Python es Hermoso"