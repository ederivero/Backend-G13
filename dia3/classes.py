# Creación de una clase
class MiClase:
    numero = 12345
    texto = "Hola mundo"
    estado = True

valores = MiClase()

# Acceso a los atributos de la clase
# print(valores.estado)

class Vehiculo:
    # Este metodo nos permite inicializar los atributos de la clase
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca

    # Este metodo nos permite representar el objeto como un string
    def __str__(self):
        return f"Vehiculo {self.mostrarMarca()}"
    
    # Este es un metodo cualquiera de la clase
    def mostrarMarca(self):
        return self.marca

auto = Vehiculo("Rojo", "Mitsubishi")
auto.color = "Azul"
# print(auto.color)


"""
Crear un objeto Operaciones, que tenga los siguientes metodos:
    - Suma
    - Resta

Y los atributos se deben ingresar por el objeto.
print(operacion.suma())
print(operacion.resta())
"""

class OperacionesMatematicas:
    def __init__(self, a:int, b:int):
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f"Los valores a sumar o restar son: {self.a} y {self.b}"

    def suma(self) -> int:
        return self.a + self.b
    
    def resta(self) -> int:
        return self.a - self.b
    
operacion = OperacionesMatematicas(5, 2)

print(operacion.suma())
print(operacion.resta())

