# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 14:04:00 2013

@author: miguel
"""

from PIL import Image
import numpy as np

class Simbolo(object):
    
    def __init__(self,dato,p):        
        self.simbolo = dato
        self.probabilidad = p
        self.codigo = ""
        self.sucesor = None
    
    def getProbabilidad(self):
        return self.probabilidad
    
    def getSucesor(self):
        return self.sucesor

    def getSimbolo(self):
        return self.simbolo
    
    def setSucesor(self,nuevo):
        self.sucesor = nuevo
    
    def setCodigo(self,c):
        self.codigo += c
    
    def getCodigo(self):
        return self.codigo
        
class Huffman(object):
    
    def __init__(self,img,hist,L,A):
        self.img = img
        self.hist = hist
        self.largo = L
        self.ancho = A
        self.tablaSimb = []
    
    def comprimir(self):
        self.obtenerFrecuencias()
        self.generaCodigo(self.tablaSimb)
        cont = 0
        for i in self.tablaSimb:
            print "Simbolo -> "+str(i.getSimbolo())+ " Probabilidad -> "+str(i.getProbabilidad()) + " Codigo -> "+ i.getCodigo()         
            cont += i.getProbabilidad()* len(i.getCodigo())
        
        print "L media => "+ str(cont)
            
    def generaCodigo(self,tabla):
        
        if len(tabla) > 2:
            newTabla = self.creaTabla(tabla)            
            self.generaCodigo(newTabla)
            self.asignaCodigo(tabla)
        else:
            tabla[0].setCodigo("0")
            tabla[1].setCodigo("1")
    
    def creaTabla(self,tabla):
        numElem = len(tabla)
        newTabla = []
        
        for i in range(numElem-2):
            s = Simbolo(tabla[i].getSimbolo(),tabla[i].getProbabilidad())
            tabla[i].setSucesor(s)          
            newTabla.append(s)
        
        sumaF = tabla[numElem-2].getProbabilidad() + tabla[numElem-1].getProbabilidad()
        s = Simbolo(1,sumaF)
        tabla[numElem-2].setSucesor(s)
        tabla[numElem-1].setSucesor(s)
        self.insertOrd(s,newTabla)
        print "Se muestra la tabla ordenada ------------"
        print "Nueva probabilidad"
        print "P ->"+ str(s.getProbabilidad())
        self.muestraTablaSim(newTabla)
            
        return newTabla
        
    def asignaCodigo(self,tabla):
        
        numElem = len(tabla)
        
        for i in range(numElem-2):
            cod = tabla[i].getSucesor().getCodigo()       
            tabla[i].setCodigo(cod)
        
        cod = tabla[numElem-2].getSucesor().getCodigo()
        tabla[numElem-2].setCodigo(cod+"0")
        tabla[numElem-1].setCodigo(cod+"1")
                
    def obtenerFrecuencias(self):
        
        #numSim = self.largo * self.ancho        
        
        """for i in range(256):
            f = self.hist[i]/float(numSim)
            simb = Simbolo(i,f)
            self.insertOrd(simb,self.tablaSimb)
        
        """
        s = Simbolo(1,7/float(64))
        self.tablaSimb.append(s)
        s = Simbolo(4,7/float(64))
        self.tablaSimb.append(s)
        s = Simbolo(0,6/float(64))
        self.tablaSimb.append(s)
        s = Simbolo(13,5/float(64))
        self.tablaSimb.append(s)
        s = Simbolo(15,5/float(64))
        self.tablaSimb.append(s)
        s = Simbolo(2,4/float(64))
        self.tablaSimb.append(s)
        s = Simbolo(6,4/float(64))
        self.tablaSimb.append(s)
        s = Simbolo(8,4/float(64))
        self.tablaSimb.append(s)
        s = Simbolo(10,4/float(64))
        self.tablaSimb.append(s)
        s = Simbolo(11,4/float(64))
        self.tablaSimb.append(s)
        s = Simbolo(14,4/float(64))
        self.tablaSimb.append(s)
        s = Simbolo(12,3/float(64))
        self.tablaSimb.append(s)
        s = Simbolo(3,2/float(64))
        self.tablaSimb.append(s)
        s = Simbolo(5,2/float(64))
        self.tablaSimb.append(s)
        s = Simbolo(7,2/float(64))
        self.tablaSimb.append(s)
        s = Simbolo(9,1/float(64))
        self.tablaSimb.append(s)
        
        
             
    def insertOrd(self,s,tablaS):
        
        numElem = len(tablaS)        
        
        if numElem == 0:
            tablaS.append(s)
        else:
            aux = 0
            for i in range(numElem):
                if s.getProbabilidad() > tablaS[i].getProbabilidad():
                    tablaS.insert(i,s)
                    break
                else:
                    aux += 1
            
            if aux == numElem:
                tablaS.append(s)
    
    def muestraTablaSim(self,tabla):
        for i in tabla:
            print i.getProbabilidad()
        

img = Image.open("/home/miguel/Documentos/PDI/Imagenes/cameraman.jpg")
x = np.asarray(img)
h = Huffman(x,img.histogram(),x.shape[0],x.shape[1])
h.comprimir()







 