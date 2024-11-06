import random
"""
melyik a legnagyobb
uj lista paros_lista paros szamokkal
5el oszthato szamok osszege mennyi
hanyadik helyen a legkissebb
"""
#1

def hany_negativ(lista):
    i = 0
    negativ = 0
    while i < len(lista):
        if lista[i] < 0:
            negativ += 1
        i += 1 
    return negativ

#2

def legnagyobb(lista):
    max_index:int=0
    for i in range(0,len(lista),1):
        if (lista[i]>lista[max_index]):
            max_index=i
    
    return lista[max_index]

#3
def ujlista():
    paros_lista=[]
    for i in range (0,100,2):
        szam:int=int(random.random()*(151+50)-50)
        paros_lista.append(szam)
    return paros_lista