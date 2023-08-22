#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
#persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
#opcional. Crear los siguientes métodos para la clase:
#Un constructor, donde los datos pueden estar vacíos.
#Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
#directamente, sólo ingresando o retirando dinero.
#mostrar(): Muestra los datos de la cuenta.
#ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
#negativa, no se hará nada.
#retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    # ... (otros métodos y getters/setters)

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    # Getter para el atributo titular
    def get_titular(self):
        return self.__titular
    
    # Getter y setter para el atributo cantidad
    def get_cantidad(self):
        return self.__cantidad
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad

    def mostrar(self):
        print("Titular:")
        self.__titular.mostrar()
        print("Cantidad:", self.__cantidad)

# Crear una instancia de la clase Persona para usar como titular de la cuenta
titular = Persona("Juan", 30, "123456789")

# Crear una instancia de la clase Cuenta
cuenta1 = Cuenta(titular, 1000.0)

# Realizar operaciones en la cuenta
cuenta1.ingresar(500)
cuenta1.retirar(200)

# Mostrar los datos de la cuenta
cuenta1.mostrar()