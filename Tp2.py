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
    return array


lista = []
n = int(input("ingresar número n: "))
i = 0
for i in range(n):
    print(i+1)
    lista.append(i+1)  
print(cuadrados(lista))
