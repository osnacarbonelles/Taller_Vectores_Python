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


"""
6. Dado un vector v, indique si es simétrico, un vector es simétrico si siendo
longitud par los números de la primera mitad son iguales al inverso de la
otra mitad por ejemplo: X=[1,2,3,3,2,1], en el ejemplo x es un vector
simétrico, en caso que la longitud del vector sea impar, se ignorará el
elemento central y se seguirá la misma lógica anterior, por ejemplo:
Y=[3,5,7,8,7,5,3], en este ejemplo Y es simétrico.
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


def simetrico(listaNumeros):
    if listaNumeros == listaNumeros[:: -1]:
        print("Si es simétrico")
    else:
        print("No es simétrico")


simetrico(listaNumeros)


"""
7. Dado dos vectores númericos A y B debe realizar las siguiente operaciones
con conjuntos:
a. Unión: Conjunto que contiene(sin repetir) los elementos de A y B.
b. Intersección: Conjunto que contiene los elementos comunes que
aparecen en los conjuntos A y B
c. Diferencia(A-B) Conjunto formado por los elementos que pertenecen
al conjunto A y no pertenecen al conjunto B.
d. Diferencia (B-A) Conjunto formado por los elementos que pertenecen
al conjunto B y no pertenecel al conjunto A.
"""
# Capturar datos para el vector A
i = 1
listaNumeros1 = []
while True:
    numero = int(input(f'Digite cualquier número para el vector A. '
                       'Si desea salir digite 0: '))
    if numero == 0:
        break
    listaNumeros1.append(numero)
    i += 1
print(f'Los numeros ingresados para el vector A fueron: {listaNumeros1}')

# Capturar datos para el vector B
j = 1
listaNumeros2 = []
while True:
    numero = int(input(f'Digite cualquier número para el vector B. '
                       'Si desea salir digite 0: '))
    if numero == 0:
        break
    listaNumeros2.append(numero)
    j += 1
print(f'Los numeros ingresados para el vector B fueron: {listaNumeros2}')

listaUnion = []
listaInterseccion = []
listadiferenciaAB = []
listadiferenciaBA = []


def union(a, b):
    listaUnion = set(a) | set(b)
    return print(f'La lista resultante de la union es: {listaUnion}')


def interseccion(a, b):
    listaInterseccion = set(a) & set(b)
    return print(f'La lista resultante de la Interseccion es: '
                 f'{listaInterseccion}')


def diferenciaAB(a, b):
    listadiferenciaAB = set(a) - set(b)
    return print(f'La lista resultante de la Diferencia(A-B) es: '
                 f'{listadiferenciaAB}')


def diferenciaBA(a, b):
    listadiferenciaBA = set(b) - set(a)
    return print(f'La lista resultante de la Diferencia(B-A) es: '
                 f'{listadiferenciaBA}')


union(listaNumeros1, listaNumeros2)
interseccion(listaNumeros1, listaNumeros2)
diferenciaAB(listaNumeros1, listaNumeros2)
diferenciaBA(listaNumeros1, listaNumeros2)
