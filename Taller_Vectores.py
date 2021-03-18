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
































