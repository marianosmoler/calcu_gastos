# -*- coding: utf-8 -*-
"""
Created on Sun May 26 21:36:34 2024

@author: mariano
"""
#%%

from operator import itemgetter

#%%
# ejemplo=[('Ballester',85776), ('Park Av',0),('Hele',17800),('Gabi',8200),('Munro',0),('Urquiza',0)]
ejemplo=[('Nacho',80776), ('Nuria',5000),('Marian',0),('Kuko',0),('Hele',17800),('Gabi',8200),('Guille',0),('Dogui',40000),('Belen',0), ('Dante',0)]

# ejemplo2=[('Kuko',10000),('Nuria',49400),('nacho',9600),('marian',0),('guille',0),('gabi',0),('hele',0),('dan',0),('belen',0)]

#%%
def cuota(lista):
    total=0
    for i in range(len(lista)):
        total=total+lista[i][1]
    
    division=total/len(lista)
    cuota=round(division,2)
    print (('el total es ', total, 'per capita son: ', cuota))
    return('el total es ', total, 'per capita son: ', cuota)


#%%       

def define_deudores_acreed (entrada, cuota):
    deudores=[]
    exceso=[]
    
    for i in range(len(entrada)):
        cada_entrada=entrada[i]
        if cada_entrada[1]<cuota:
            resta1=round(cuota-cada_entrada[1],2)
            tupla1=(cada_entrada[0],resta1)
            deudores.append(tupla1)
        if cada_entrada[1]> cuota:
            resta2=round(cada_entrada[1]-cuota,2)
            tupla2=(cada_entrada[0],resta2)
            exceso.append(tupla2)
    
    print('los deudores son', deudores,' hay que pagarles a ', exceso)
    return('los deudores son', deudores,' hay que pagarles a ', exceso)

# print(define_deudores_acreed(ejemplo,320))

#%%

def de_tupla_a_lista(lista):
    tupla=lista.copy()
    for i in range(len(tupla)):
        if type(tupla[i])== tuple:
            tupla[i]=list(tupla[i])
            
    return tupla

# print(de_tupla_a_lista(a))

#%%

def ordena_lista_tuplas(lista, elemento, descendente=True):
    bis = lista.copy()
    return sorted(bis, key=itemgetter(elemento), reverse=descendente)

#al darle valor false o true las tuplas quedan ordenadas de forma ascendente o descendente





#%%

cuotaej= cuota(ejemplo)

casoej=define_deudores_acreed(ejemplo, cuotaej[3])

deudores_desc=ordena_lista_tuplas(casoej[1], 1,descendente=True) #esto deberia ser llamado dentro de una funcion

exceso_desc=ordena_lista_tuplas(casoej[3], 1,descendente=True) #esto deberia ser llamado dentro de una funcion

#convierto a listas las tuplas para poder reasignarles valores
solo_deudas=de_tupla_a_lista(deudores_desc)     #lista de los que tienen que pagar OJO que usa una variable global
    
exceso_plata=de_tupla_a_lista(exceso_desc)  #lista de los que tienen que cobrar  OJO que usa una variable global
#%%

def quien_paga_cuanto(solo_deudas,exceso_plata):
    
    i=0
    
    while len(solo_deudas)>0:
        # print('len de solo_deudas es: ', len(solo_deudas))
        if solo_deudas[i][1]<=exceso_plata[i][1]:
            # print('deudas:', solo_deudas, 'acreededores: ',exceso_plata)
            exceso_plata[i][1]=exceso_plata[i][1]-solo_deudas[i][1]
            print(solo_deudas[i][0], 'le paga a ', exceso_plata[i][0], solo_deudas[i][1])
            solo_deudas[i][1]=0
            # print(solo_deudas)
            solo_deudas.pop(0)  
            # print(solo_deudas)
    
        if solo_deudas[i][1]> exceso_plata[i][1]:
            # print('deudas:', solo_deudas, 'acreededores: ',exceso_plata)
            solo_deudas[i][1]=solo_deudas[i][1]-exceso_plata[i][1]
            print(solo_deudas[i][0], 'le paga a ', exceso_plata[i][0], exceso_plata[i][1])
            exceso_plata[i][1]=0
            # print(exceso_plata)
            exceso_plata.pop(0)
            # print(exceso_plata)
            
        else :
            pass

# %%

#version que andaba pero rompi

# def quien_paga_cuanto(solo_deudas, exceso_plata):
    
#     i=0
#     # mensajes=[]
#     while len(solo_deudas)>0:
#         # print('len de solo_deudas es: ', len(solo_deudas))
#         if solo_deudas[i][1]<=exceso_plata[i][1]:
#             # print('deudas:', solo_deudas, 'acreededores: ',exceso_plata)
#             exceso_plata[i][1]=exceso_plata[i][1]-solo_deudas[i][1]
#             print(solo_deudas[i][0], 'le paga a ', exceso_plata[i][0], solo_deudas[i][1])
#             comentario=(solo_deudas[i][0], 'le paga a ', exceso_plata[i][0], solo_deudas[i][1])
#             print(comentario)
#             # mensajes.append(comentario)
#             solo_deudas[i][1]=0
#             # print(solo_deudas)
#             solo_deudas.pop(0)  
#             # print(solo_deudas)
    
#         if solo_deudas[i][1]> exceso_plata[i][1]:
#             # print('deudas:', solo_deudas, 'acreededores: ',exceso_plata)
#             solo_deudas[i][1]=solo_deudas[i][1]-exceso_plata[i][1]
#             print(solo_deudas[i][0], 'le paga a ', exceso_plata[i][0], exceso_plata[i][1])
#             comentario2=(solo_deudas[i][0], 'le paga a ', exceso_plata[i][0], exceso_plata[i][1])
#             print(comentario2)
#             # mensajes.append(comentario2)
#             exceso_plata[i][1]=0
#             # print(exceso_plata)
#             exceso_plata.pop(0)
#             # print(exceso_plata)
            
#         # else :
#         #     pass
    
#     # print(mensajes)

# # a=quien_paga_cuanto(solo_deudas,exceso_plata)
    
#%% esta es MI version pero no anda (no lo gra generar lista de salida)

# # def ordena_lista_de_tuplas (lista, elemento):
#     if len(lista) <= 1: #caso base
    
#         salida=lista
    
#     # recursive case
#     pivot = lista[0][elemento]
#     menor_o_igual=[]
#     mayor_que=[]
   
#     for t in lista[1:]:
#         nvo_valor=t[elemento]
#         if nvo_valor <= pivot:
#             menor_o_igual.append(nvo_valor)
#         if nvo_valor > pivot:
#             mayor_que.append(nvo_valor)
            
                     
#     # recursively sort the two sublists
   
#     ordenado_menor_o_igual = ordena_lista_de_tuplas(menor_o_igual, elemento)

#     ordenado_mayor_que = ordena_lista_de_tuplas(mayor_que, elemento)

#     # return the sorted concatenation of the two sublists
   

#     salida = ordenado_menor_o_igual + [lista[0]] + ordenado_mayor_que
    
#     return salida

#%%
# def ordena_lista_de_tuplas (lista, elemento):
#     if len(lista) <= 1: #caso base
        
#         salida=lista
    
#     # recursive case
#     pivot = lista[0][elemento]
   
#     menor_o_igual = [t for t in lista[1:] if t[elemento] <= pivot]

#     mayor_que = [t for t in lista[1:] if t[elemento] > pivot]
                     
#     # recursivamente ordena las 2 sublistas
   
#     ordenado_menor_o_igual = ordena_lista_de_tuplas(menor_o_igual, elemento)

#     ordenado_mayor_que = ordena_lista_de_tuplas(mayor_que, elemento)

#     # devuelve la lista concatenada por las 2 sublistas y ordenada 
   

#     salida = ordenado_menor_o_igual + [lista[0]] + ordenado_mayor_que
    
    # return salida
    
#%%  Esto anda, hay que convertirlo en funcion

# solo_deudas=[220,120,20]
# exceso_plata=[280,80]
# solo_nombresd=['a','b','d']
# solo_nombrese=['c','e']