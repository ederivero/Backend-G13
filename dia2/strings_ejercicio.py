miNombre = "Eduardo_De_Rivero"

# Imprimir la primera letra de mi nombre convertido en mayúscula y el resto en minúsculas

# Output esperado: Hola soy: EDUARDO de rivero

miNombreLista = miNombre.split("_")
nombreUpper = miNombreLista[0].upper()
apellidoLower = miNombreLista[1].lower()
apellido2Lower = miNombreLista[2].lower()
resultado = f"Hola soy: {nombreUpper} {apellidoLower} {apellido2Lower}"
print(resultado)