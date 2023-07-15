from pprint import pprint

miDiccionario = {
    "Alemania": "Berlin",
    "Francia": "Paris",
    "Reino Unido": "Londres",
    "España": "Madrid",
    "Peru": "Lima",
    "otrosDatos": {
        "poblacion": 1000000,
        "presidente": "Pedro",
        "tags": ["turismo", "economia"]
    }
}

# Imprimir el valor de una llave
print(miDiccionario["Francia"])

# Agregar un elemento al diccionario
miDiccionario["Italia"] = "Roma"

# El pprint imprime el diccionario de una forma más legible
pprint(miDiccionario)
