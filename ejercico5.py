#Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
#cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
#del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
#ejercicio tanto de manera iterativa como recursiva.

#Versión Iterativa

def get_int():
    while True:
        try:
            user_input = input("Ingrese un valor entero: ")
            integer_value = int(user_input)
            return integer_value
        except ValueError:
            print("Valor incorrecto. Intente nuevamente.")

# Llamada a la función para obtener un valor entero
result = get_int()
print("Valor entero ingresado:", result)


#Versión Recursiva:

def get_int_recursive():
    user_input = input("Ingrese un valor entero: ")
    try:
        integer_value = int(user_input)
        return integer_value
    except ValueError:
        print("Valor incorrecto. Intente nuevamente.")
        return get_int_recursive()  # Llamada recursiva

# Llamada a la función para obtener un valor entero
result = get_int_recursive()
print("Valor entero ingresado:", result)