import hashlib

class Password:
    def quitarEspacios(self, nombre):
        return nombre.replace(" ", "")

    def encriparPassword(self, nombre_sin_espacios):
        encoded_password = nombre_sin_espacios.encode()
        return hashlib.sha256(encoded_password).hexdigest()
