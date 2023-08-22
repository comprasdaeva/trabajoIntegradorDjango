#Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
#siguientes métodos para la clase:
#Un constructor, donde los datos pueden estar vacíos.
#Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#mostrar(): Muestra los datos de la persona.
#Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    # Getter y setter para el atributo nombre
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    # Getter y setter para el atributo edad
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("La edad debe ser un valor positivo.")

    # Getter y setter para el atributo DNI
    def get_dni(self):
        return self.__dni
    
    def set_dni(self, dni):
        if len(dni) == 8:
            self.__dni = dni
        else:
            print("El DNI debe tener 8 caracteres.")

    def mostrar(self):
        print("Nombre:", self.__nombre)
        print("Edad:", self.__edad)
        print("DNI:", self.__dni)

    def es_mayor_de_edad(self):
        return self.__edad >= 18

# Crear una instancia de la clase Persona
persona1 = Persona()

# Configurar los atributos usando los setters
persona1.set_nombre("Juan")
persona1.set_edad(25)
persona1.set_dni("23456789")

# Mostrar los datos y verificar si es mayor de edad
persona1.mostrar()
print("¿Es mayor de edad?", persona1.es_mayor_de_edad())