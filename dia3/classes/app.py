"""
Convertir el nombre del usuario en una contraseña
    - Quitar los espacios entre palabras
    - Todo tienes que estar en minusculas
    - Encriptamos la contraseña
"""

from metodos import Password


nombre = "Eduardo De Rivero"

passwordObject = Password()

nombre_sin_espacios_min = passwordObject.quitarEspacios(nombre).lower()
password_encriptado = passwordObject.encriparPassword(nombre_sin_espacios_min)
print(password_encriptado)