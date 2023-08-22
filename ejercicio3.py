#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que 
#contiene y la cantidad de veces que aparece (frecuencia)

def contar_palabras(text):
    text = text.split()
    palabras={}
    for i in text:
        if i in palabras:
            palabras[i]+=1
        else:
            palabras[i]=1
    return palabras

def most_repeated(palabras):
    max_palabras = ''
    max_freq = 0
    for palabras, freq in palabras.items():
        if freq > max_freq:
            max_palabras = palabras
            max_freq = freq
    return max_palabras, max_freq       

text = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(contar_palabras(text))
print(most_repeated(contar_palabras(text)))     