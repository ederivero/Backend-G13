a = 10
b = 5

if a < b:
    print("Se cumple la condición")
elif a == b:
    print("Se cumple la condición 2")
else:
    print("No se cumple la condición")


if a > b and a == 10:
    print("Se cumple la condición 3")

if a > b or a == 10:
    print("Se cumple la condición 4")

users = None

if not users:
    print("No se encontro ningun usuario")
else:
    print("Se encontro usuarios")
