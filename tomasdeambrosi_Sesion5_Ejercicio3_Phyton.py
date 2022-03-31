# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

'''Matemáticamente podemos saber si un año es bisiesto si este es múltiplo de 4. Si además es múltiplo de 100 
no será bisiesto a no ser que sea múltiplo de 400, que sí será bisiesto.'''

def esBisiesto (año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return 'El año ' + str(año) + ' es bisiesto'
    else:
        return 'El año ' + str(año) + ' no es bisiesto'

añoIngresado = input('Ingrese un año')
print(esBisiesto(int(añoIngresado)))