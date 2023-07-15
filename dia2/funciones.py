def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("Error. División por cero")
        return
    return a / b

# Recursividad en funciones
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))