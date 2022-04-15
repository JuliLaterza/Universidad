# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 18:32:20 2022

@author: Usuario

TP 2: LISTAS
"""

#%% Ejercicio 1
import random

def funA(arr):
    lista = []
    for i in range(arr):
        lista.append(random.randint(1000,9999))
    return lista
    
def sumatoria(lista):
    total = sum(lista)
    return total

def dupli(valor,lista):
    
    if valor in lista:
        print("se encontró el num")
        lista.remove(valor)
    else:
        print("El número no se encuentra en la lista")

def capicua(lista):
    if lista == lista[::-1]:
        print("es capicua")
    else:
        print("no es capicua")


lista = [50,17,91,17,50]

resultado = funA(random.randint(10,99))
print(resultado)
print(sumatoria(resultado))
print(capicua(lista))
num = int(input("Ingresar número a eliminar: "))
dupli(num,resultado)
print(resultado)

#%% Ejercicio 3

def cuadrados(array:list):
    for i in range(len(array)):
        array[i] = array[i]**2
    return array, array[-10:]

lista = []
n = int(input("ingresar número n: "))
i = 0
for i in range(n):
    #print(i+1)
    lista.append(i+1)

print(cuadrados(lista))
#%% Ejercicio 4

def ejercicio4(lista1:list,lista2: list,eliminados:list,resultante:list):
    for i in lista1:
        if i in lista2:
            eliminados.append(i)
        else:
            resultante.append(i)
    
    return lista1, lista2, eliminados, resultante


lista1 = ["gato","perro","pato"]

lista2 = ["perro","ballena","mariposa"]

lista_resultante = []

lista_eliminados = []


print(ejercicio4(lista1,lista2,lista_eliminados,lista_resultante))


#%% Ejercicio 5


#%% Ejercicio 8

def numImpares(numimp:list):
    impares = [i for i in numimp if (i%2) != 0]
    return impares

numeros = []
for i in range(100,201): #Generar los números del 100-200
    numeros.append(i)

print(numImpares(numeros))