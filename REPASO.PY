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


def num_par(numero):
    return numero % 2 == 0

print(num_par(8))
print(num_par(5))

#Define una función llamada factorial que calcule el factorial de un número.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Prueba de la función
print(factorial(5))  # Output: 120

#Asigna valores a tres variables (a, b, c) e imprime sus valores.
a = 5
b = 6
c = 8
print(a, b, c)

#Sumar Elementos de una Lista:
#Crea una lista con cinco números e imprime la suma de sus elementos.

numeros = [1,2,3,4,5]
suma = sum(numeros)
print(suma)

#Función que Retorna un Saludo:
#Define una función saludar que retorne un saludo como cadena de texto.

def saludar():
    return "Hola!!"
print(saludar())

#Define una función suma que reciba dos números y retorne su suma.
def suma(b, c):
        return b + c
resultado = suma(10, 8)
print(resultado)

#Crea una lista con una mezcla de números y cuenta cuántos son mayores que 10.
numeros = [4, 8, 15, 16, 23, 42]
contador = sum(1 for x in numeros if x > 10)
print(contador)

##Crea una lista con una mezcla de números y cuenta cuántos son menores que 10.
numeros = [2, 5, 6, 9, 8, 10, 15, 18]
contador = sum(1 for n in numeros if n < 10)
print(contador)

##Crea una lista con una mezcla de números y cuenta cuántos son par.
numeros = [1, 2, 3, 8, 10, 13, 15, 18, 22, 25]
contador = sum(1 for x in numeros if x % 2)
print(contador)

#Define una función encontrar_maximo que reciba una lista de números y retorne el mayor de ellos.
def encontrar_maximo(lista):
    return max(lista)
print(encontrar_maximo([1,8,15,22,70]))

#Define una función encontrar_minimo que reciba una lista de números y retorne el menor de ellos.
def encontrar_minimo(lista):
    return min(lista)
print(encontrar_minimo([15, 9, 84, 94, 12, 7, 22]))

#Define una función es_primo que reciba un número y retorne True si es primo y False en caso contrario
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(es_primo(7))  # True
print(es_primo(10)) # False

#Crea una lista con números desordenados y ordénalos en orden ascendente.

