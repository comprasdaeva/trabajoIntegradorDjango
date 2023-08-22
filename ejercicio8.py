#Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
#CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
#además del titular y la cantidad se debe guardar una bonificación que estará expresada en
#tanto por ciento. Crear los siguientes métodos para la clase:
#Un constructor.
#Los setters y getters para el nuevo atributo.
#En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
#tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
#mayor de edad pero menor de 25 años y falso en caso contrario.
#Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
#El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    # Getter y setter para el nuevo atributo bonificacion
    def get_bonificacion(self):
        return self.__bonificacion
    
    def set_bonificacion(self, bonificacion):
        if bonificacion >= 0:
            self.__bonificacion = bonificacion

    def es_titular_valido(self):
        return self.get_titular().es_mayor_de_edad() and self.get_titular().get_edad() < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No se puede retirar dinero. Titular no válido.")

    def mostrar(self):
        super().mostrar()
        print("Tipo: Cuenta Joven")
        print("Bonificación:", self.__bonificacion, "%")

# Crear una instancia de la clase Persona para usar como titular de la cuenta joven
titular_joven = Persona("Ana", 20, "987654321")

# Crear una instancia de la clase CuentaJoven
cuenta_joven = CuentaJoven(titular_joven, 500.0, 5.0)

# Realizar operaciones en la cuenta joven
cuenta_joven.ingresar(200)
cuenta_joven.retirar(100)

# Mostrar los datos de la cuenta joven
cuenta_joven.mostrar()

# Verificar si el titular es válido
print("¿Es titular válido?", cuenta_joven.es_titular_valido())