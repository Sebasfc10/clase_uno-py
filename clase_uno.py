# -*- coding: utf-8 -*-
import math

# print('hi world')


# VARIABLES

a = 3
print(type(a))

a = 'gg'
print(type(a))

# potencia 

a = 5
b = 2
c = a ** b
print(c)

# raiz

a = 27
c = a ** (1/3)
print(c)


# conversiones de tipos de datos
# de a entero

a = '3'
y = int(a) #vale para float, str, int, etc...
print(y)
print(type(y))

# capturar por screen

nombre = input('digite su nombre:')
print('hola',nombre)

n1 = input('ingresa el primer numero: ')
n1 = int(n1)
n2 = input('ingresa el segundo numero: ')
n2 = int(n2)
suma= n1 + n2

print(suma)

# segunda tarea

numero = int(input('digite el numero que se elevara al cuadrado: '))
cuadrado = numero ** 2
print(f'el numero elevado es {numero} y elevado da : {cuadrado}')

# tarea 3

precio = float(input('digite el precio a descontar: '))
descuento = precio * 20/100
ahorrado = precio - descuento
print(f'el valor inicial es: {precio}')
print(f'el valor ahorrado es: {ahorrado}')
print(f'el valor en descuento es este: {descuento}')


"""
seguimos
"""

#negacion 
print(not True) #false
print(not False) #true

# mas de dos condiciones al mismo tiempo
print(True and False and True or False or True or True) #true
print(True and (False and True) or False or (True or True)) #true

"""
jerarquias
1. parentesis y llaves
2. potencia y raices
3. multiplicacion y division
4. sumas y restas
"""

"""
jerarquias de operaciones booleanas
1. parentesis y llaves
2. tablas de verdad
"""
#ejericcio IF

age = int(input('ingrese su edad: '))
if age > 18:
    print('es mayor de edad')
else:
    print('es menor de edad')

#ejercicio IF 2

nota = float(input('ingrese su nota: '))
if nota < 3.0:
    print('reprobo')
if nota > 3 and nota < 5:
    print('aprobo')
















