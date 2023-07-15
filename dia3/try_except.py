dividendo = input("Ingrese el dividendo: ")
divisor = input("Ingrese el divisor: ")

try:
    resultado = dividendo / divisor

except Exception as err:
    print(err)