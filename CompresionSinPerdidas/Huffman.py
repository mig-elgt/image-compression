# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 14:04:00 2013

@author: miguel
"""

from PIL import Image
import Simbolo as S
import numpy as np

class Huffman(object):
    
    def __init__(self,img,hist,L,A,rutaArchivo):
        self.rutaFile = rutaArchivo        
        self.img = img
        self.hist = hist
        self.largo = L
        self.ancho = A
        self.tablaSimb = []
        self.listaBloques = []
        self.diccionarioSimbolos = {}
        self.cadenaSimbolos = ""
        
    def getTablaSimbolo(self):
        return self.tablaSimb;
    
    def comprimir(self):
        self.obtenerFrecuencias()
        self.generaCodigo(self.tablaSimb)
        self.crearCadenaCodigo()
        self.escribirCodigo()        
            
    def crearCadenaCodigo(self):
        #Se crea el diccionario de simbolos
        for simb in self.tablaSimb:
             self.diccionarioSimbolos[simb.getSimbolo()] = simb.getCodigo()
             
        for i in range(self.largo):
            for j in range(self.ancho):
                self.cadenaSimbolos += self.diccionarioSimbolos[self.img[i,j]]
    
    def escribirTablaSimbolos(self,fh):
        cadAux = ""
        #Se escribe la tabla de simbolos
        for item in self.diccionarioSimbolos:
            cadAux += str(item)+"-"+ (self.diccionarioSimbolos[item])+"-"
        
        cadAux = cadAux[:len(cadAux)-1]+"\n"
        fh.write(cadAux)
    
    def escribirCadenaCodigo(self,fh):
        palabra = ""
        #Se escribe la cadena de codigo
        for i in range(len(self.cadenaSimbolos)):
            palabra += self.cadenaSimbolos[i]
            if((i+1)%8 == 0):
               fh.write(chr(int(palabra,2)))
               palabra = ""
        
        if len(palabra)!=0:
            palabra = palabra + ("0"*(8-len(palabra)))
            fh.write(chr(int(palabra,2)))
            
    def escribirCodigo(self):
        fh = open(self.rutaFile,'w')
        fh.write(str(self.largo)+"\n")
        fh.write(str(self.ancho)+"\n")
        self.escribirTablaSimbolos(fh)
        self.escribirCadenaCodigo(fh)
        fh.close()
    
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
            s = S.Simbolo(tabla[i].getSimbolo(),tabla[i].getProbabilidad())
            tabla[i].setSucesor(s)          
            newTabla.append(s)
        
        sumaF = tabla[numElem-2].getProbabilidad() + tabla[numElem-1].getProbabilidad()
        s = S.Simbolo(1,sumaF)
        tabla[numElem-2].setSucesor(s)
        tabla[numElem-1].setSucesor(s)
        self.insertOrd(s,newTabla)
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
        
        numSim = self.largo * self.ancho        
        
        for i in range(256):
            f = self.hist[i]/float(numSim)
            simb = S.Simbolo(i,f)
            self.insertOrd(simb,self.tablaSimb)
             
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
        cont = 0
        for i in tabla:
            print "Simbolo -> "+str(i.getSimbolo())+ " Probabilidad -> "+str(i.getProbabilidad()) + " Codigo -> "+ i.getCodigo()         
            cont += i.getProbabilidad()* len(i.getCodigo())
        
        print "L media => "+ str(cont)
    
    def sumarProba(self,rango,tablaSimb):
        acum = 0
        for i in range(rango,256):
            acum += self.tablaSimb[i].getProbabilidad()
        return acum
    
    def creaBloques(self,numBloques):
        if numBloques != 0:    
            tam = 256;
            cociente = tam/numBloques
            residuo = tam%numBloques
        
        for i in range(numBloques):
            if residuo == 0:
                self.listaBloques.append(cociente)
            else:
                if i < residuo:
                    self.listaBloques.append(cociente+1)
                else:
                    self.listaBloques.append(cociente)
    
    def descomprimir(self, urlImg):
        self.leerCogido(urlImg)
        self.decodificaImagen()
    
    def decodificaImagen(self):
        x,y = 0,0        
        palabra = ""
        self.img = (np.zeros((int(self.largo),int(self.ancho))))
        
        for i in self.cadenaSimbolos:
            palabra += i
            if self.diccionarioSimbolos.has_key(palabra):
                self.img[x,y] = self.diccionarioSimbolos[palabra]
                palabra = ""
                y += 1
            
            if y == int(self.ancho):
                y = 0
                x += 1
        
        
    def leerCogido(self,urlImg):
        
        fh = open(urlImg,'r')
        self.largo = fh.readline()
        self.ancho = fh.readline()
        tablaS = fh.readline()
        
        for l in fh.readlines():
            for c in range(len(l)):
                self.cadenaSimbolos += np.binary_repr(ord(l[c]),8)
        
        self.crearDiccionarioSimbolos(tablaS)   
    
        fh.close() 
    
    def crearDiccionarioSimbolos(self,T):
        T = T[:len(T)-1]        
        tAux = T.split("-")
        
        i = 0
        while i < len(tAux):
            self.diccionarioSimbolos[tAux[i+1]] = int(tAux[i])            
            i+=2
        
    
#img = Image.open("/home/miguel/Documentos/PDI/Imagenes/cameraman.jpg")
#img.show()
#x = np.asarray(img)
#img.show()
#h = Huffman(x,img.histogram(),x.shape[0],x.shape[1],'/home/miguel/Documentos/PDI/Proyecto/Procesamiento Digital de Imagenes/Compresion/prueba.h')
#h.comprimir()
#h.descomprimir('/home/miguel/Documentos/PDI/Proyecto/Procesamiento Digital de Imagenes/Compresion/prueba.h')
#print x
#print h.img
#Image.fromarray(h.img).show()





 