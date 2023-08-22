# Escribir una función que calcule el máximo común divisor entre dos números
#MCD: El numero mas grande que divide dos numeros.


def mcd(x, y):
    mcd = 1  #variable que se asigna 1 divide a cualquier numero

    if x % y ==0:
        return y
    
    for k in range(int(y/2),0,-1):
        if x % k ==0 and y % k ==0:
            mcd = k
            break
    return mcd

print(mcd(8,4))
print(mcd(13,7))    