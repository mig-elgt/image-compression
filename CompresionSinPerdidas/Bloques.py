# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:56:37 2013

@author: miguel
"""

def creaBloques(numBloques):
    if numBloques != 0:    
        tam = 256;
        cociente = tam/numBloques
        residuo = tam%numBloques
        
        for i in range(numBloques):
            if residuo == 0:
                listaBloques.append(cociente)
            else:
                if i < residuo:
                    listaBloques.append(cociente+1)
                else:
                    listaBloques.append(cociente)

for i in range(256):
    cont = 0
    listaBloques = []
    print "Num Bloques :" + str(i)
    creaBloques(i)
    print listaBloques
    for i in listaBloques:
            cont += i
    print cont
    