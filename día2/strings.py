cadenaCaracteres = "Hola Mundo"

print(cadenaCaracteres[1])
# H

print(cadenaCaracteres[:4])
# Hola

print(cadenaCaracteres[5:])
# Mundo

print(cadenaCaracteres[2:7])
# la Mu

# Convertir a mayúsculas
print(cadenaCaracteres.upper())
# HOLA MUNDO

# Convertir a minúsculas
print(cadenaCaracteres.lower())
# hola mundo

# Remover espacios en blanco al inicio y al final
print(cadenaCaracteres.strip())

# Reemplazar caracteres
print(cadenaCaracteres.replace("o", "0"))

# Dividir una cadena de caracteres
cadenaCaracteres = "Eduardo De Rivero"
print(cadenaCaracteres.split(" "))
primerNombre = cadenaCaracteres.split(" ")

# Formatear cadenas de caracteres

print("Hola {} bienvenido a Código {}".format(primerNombre[0], "Python"))
print(f"Hola {primerNombre[0]} bienvenido a Código Python")
