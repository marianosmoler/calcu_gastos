# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 20:09:52 2025

@author: mariano
"""


"Para indicar cantidad de lienas a ingresar usar este modelo"

def carga_vector():
    lista = []
    n = int(input("Cantidad de personas: "))
    
    for i in range(n):
        b = list(map(str, input("nombre y monto: ").split()))
        c=(b[0],float(b[1]))
        lista.append(c)
    return(lista)
