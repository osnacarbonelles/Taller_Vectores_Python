# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 18:20:55 2021

@author: Osnaider Carbonell
"""


"""
1. De los n elementos de un vector dado calcule:
a. La sumatoria
b. La productoria
c. El Mayor Elemento
d. El menor Elemento
"""
i = 1
listaNumeros = []
while True:
    numero = int(input(f'Digite cualquier número. Si desea salir digite 0: '))
    if numero == 0:
        break
    listaNumeros.append(numero)
    i += 1
print(f'Los numeros ingresados fueron: {listaNumeros}')


def sumatoria(listaNumeros):
    acumulado = 0
    for i in listaNumeros:
        acumulado = acumulado + i
    return print(f'La sumatoria del vector es: {acumulado}')


def productoria(listaNumeros):
    acumulado = 1
    for i in listaNumeros:
        acumulado = acumulado * i
    return print(f'La productoria del vector es: {acumulado}')


def mayor(listaNumeros):
    mayor_elemento = listaNumeros[0]
    actual_elemento = 0
    for i in listaNumeros:
        actual_elemento = i
        if actual_elemento > mayor_elemento:
            mayor_elemento = actual_elemento
    return print(f'El mayor elemento del vector es: {mayor_elemento}')


def menor(listaNumeros):
    menor_elemento = listaNumeros[0]
    actual_elemento = 0
    for i in listaNumeros:
        actual_elemento = i
        if actual_elemento < menor_elemento:
            menor_elemento = actual_elemento
    return print(f'El menor elemento del vector es: {menor_elemento}')


sumatoria(listaNumeros)
productoria(listaNumeros)
mayor(listaNumeros)
menor(listaNumeros)


"""
2. De los n elementos de un vector dado calcule:
a. Cantidad de elementos pares
b. Cantidad de elementos impares
c. Cantidad de elementos primos
"""
i = 1
listaNumeros = []
while True:
    numero = int(input(f'Digite cualquier número. Si desea salir digite 0: '))
    if numero == 0:
        break
    listaNumeros.append(numero)
    i += 1
print(f'Los numeros ingresados fueron: {listaNumeros}')


def par(listaNumeros):
    cont_par = 0
    for i in listaNumeros:
        if i % 2 == 0:
            cont_par = cont_par + 1
    return print(f'La cantidad de elementos pares es: {cont_par}')


def impar(listaNumeros):
    cont_impar = 0
    for i in listaNumeros:
        if i % 2 != 0:
            cont_impar = cont_impar + 1
    return print(f'La cantidad de elementos impares es: {cont_impar}')


def primos(listaNumeros):
    cont_primos = 0
    for i in listaNumeros:
        if i % 2 == 1:
            cont_primos = cont_primos + 1
    return print(f'La cantidad de elementos primos es: {cont_primos}')


par(listaNumeros)
impar(listaNumeros)
primos(listaNumeros)


"""
3. Dado un Vector v y un Vector v1 de cómo resultado un Vector resultante de
las siguientes operaciones:
a. Suma
b. Resta
"""
# Capturar datos para el vector v
i = 1
listaNumeros1 = []
while True:
    numero = int(input(f'Digite cualquier número para el vector v. '
                       'Si desea salir digite 0: '))
    if numero == 0:
        break
    listaNumeros1.append(numero)
    i += 1
print(f'Los numeros ingresados para el vector v fueron: {listaNumeros1}')

# Capturar datos para el vector v1
j = 1
listaNumeros2 = []
while True:
    numero = int(input(f'Digite cualquier número para el vector v1. '
                       'Si desea salir digite 0: '))
    if numero == 0:
        break
    listaNumeros2.append(numero)
    j += 1
print(f'Los numeros ingresados para el vector v fueron: {listaNumeros2}')

listaResultanteSuma = []
listaResultanteResta = []


def sumaListas(a, b):
    for i in range(len(a)):
        listaResultanteSuma.append(a[i] + b[i])
    return print(f'La lista de la Suma resultante es: {listaResultanteSuma}')


def restaListas(a, b):
    for i in range(len(b)):
        listaResultanteResta.append(b[i] - a[i])
    return print(f'La lista de la Resta resultante es: {listaResultanteResta}')


sumaListas(listaNumeros1, listaNumeros2)
restaListas(listaNumeros1, listaNumeros2)


"""
4. De los n elementos de un vector dado identifique el número que mas se
repite e indique cual es.
"""
i = 1
listaNumeros = []
while True:
    numero = int(input(f'Digite cualquier número. Si desea salir digite 0: '))
    if numero == 0:
        break
    listaNumeros.append(numero)
    i += 1
print(f'Los numeros ingresados fueron: {listaNumeros}')


def vecesRepetido(listaNumeros):
    contador = 0
    num_repetido = 0
    for i in listaNumeros:
        frecuencia = listaNumeros.count(i)
        if frecuencia > contador:
            contador = frecuencia
            num_repetido = i
    return print(f'El número que mas se repite es {num_repetido}'
                 f' con {contador} cantidad de veces')


vecesRepetido(listaNumeros)


"""
5. Dado un Vector v de longitud par, divida en 2 partes, en la primera parte
realice la productoria y en la segunda la sumatoria. Entregue los valores
resultantes.
"""
i = 1
listaNumeros = []
while True:
    numero = int(input(f'Digite cualquier número. Si desea salir digite 0: '))
    if numero == 0:
        break
    listaNumeros.append(numero)
    i += 1
print(f'Los numeros ingresados fueron: {listaNumeros}')


def dividirLista(listaNumeros):
    mitad = len(listaNumeros)//2
    return listaNumeros[:mitad], listaNumeros[mitad:]


listaNumerosB, listaNumerosC = dividirLista(listaNumeros)
productoria(listaNumerosB)  # se utiliza la funcion del primer ejercicio
sumatoria(listaNumerosC)  # se utiliza la funcion del primer ejercicio




























