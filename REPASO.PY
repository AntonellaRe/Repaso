def suma(num1, num2):
    return (num1 + num2)

print(4+2)
print(-1 + 5)


def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(es_par(4)) 
print(es_par(7))  

sum1 = 1
sum2 = 2
resultado = sum1 + sum2
print(resultado)

# Definiendo un array (lista) de números
numeros = [1, 2, 3, 4, 5]

# Accediendo al primer elemento del array
print(numeros[0])  # Output: 1
print(numeros[1]) #: 2


# Definiendo una función que suma dos números
def suma(a, b):
    return a + b

# Usando la función suma
resultado = suma(3, 4)
print(resultado)  # Output: 7

def resta (a, b):
    return a - b
resultado = resta(10,5)
print(resultado)

# Definiendo una variable para almacenar un número
mi_numero = 10

# Definiendo una variable para almacenar una cadena de texto
mi_texto = "Hola, mundo"

# Imprimiendo el valor de las variables
print(mi_numero)  # Output: 10
print(mi_texto)   # Output: Hola, mundo

#Escribe una función llamada area_rectangulo 
# que reciba dos parámetros (ancho y alto) 
# y retorne el área de un rectángulo.

def area_rectangulo(ancho, alto):
    return ancho * alto

# Prueba de la función
resultado = area_rectangulo(5, 10)
print(resultado)  # Output: 50


#Escribe una función llamada promedio_lista
#  que reciba una lista de números 
# y retorne el promedio de esos números.

def promedio_lista(numeros):
    return sum(numeros) / len(numeros)

print(promedio_lista([1,2,3,4,5]))

#Escribe una función llamada es_par que reciba un número
#  y retorne True si el número es par y False si es impar.

def es_par(numero):
    return numero % 2 == 0

# Prueba de la función
print(es_par(4))  # Output: True
print(es_par(7))  # Output: False


