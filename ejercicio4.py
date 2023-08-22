#Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
#palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
#que reciba el diccionario generado con la función anterior y devuelva una tupla con la
#palabra más repetida y su frecuencia.

def contar_palabras(cadena):
  #Recibe una cadena de caracteres y regresa un diccionario con las palabras (keys) y conteo (value)
  cadena= cadena.split()
  palabras={}
  for i in cadena:
    if i in palabras:
      palabras[i] +=1
    else:
      palabras[i]= 1
  return palabras

def contador_dict(dictionario):
  #Recibe un diccionario y regresa una tupla: la palabra mas repetida y cuantas veces aparece
  palabra_frecuente= ''
  cantidad=0
  for keys,values in dictionario.items():
    if values > cantidad:
      cantidad= values
      palabra_frecuente= keys
  return palabra_frecuente,cantidad
entrada=input('Ingrese su cadena de caracteres: ')
print(contar_palabras(entrada))
print(contador_dict(contar_palabras(entrada)))