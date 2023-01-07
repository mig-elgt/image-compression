# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 23:27:41 2013

@author: miguel
"""

from PIL import Image
import numpy as np
import decimal

class Aritmetica():
    
    def __init__(self,img,H,L,A,File):
        self.promedio = 0.0
        self.img = img
        self.tablaPro = []
        self.listaPromedios = []
        self.tablaCod = []
        self.histo = H
        self.largo = L
        self.ancho = A
        self.rutaFile = File

    def crearTablaPro(self):
        totalPixeles = self.largo*self.ancho

        self.tablaPro.append((0,0.0,self.histo[0]/float(totalPixeles)))        
        i = 1
        while i < len(self.histo):
            pro = self.histo[i]/float(totalPixeles)
            p1 = self.tablaPro[i-1][2]
            p2 = pro + p1
            self.tablaPro.append((i,p1,p2))
            i += 1

    def crearTablaOfPromedio(self):
        aux = self.img.flatten()
        numBloques = 4
        LI = 0
        LS = numBloques
        while LS < len(aux):
            pro = self.calculaPromedio(aux[LI:LS])
            LI = LS
            LS += numBloques
            self.listaPromedios.append((pro,4))
        
        if LI < len(aux):
            pro = self.calculaPromedio(aux[LI:len(aux)])
            self.listaPromedios.append((pro,len(aux)-LI))
        
    def calculaPromedio(self,bloque):
        tablaCod = []
        tablaCod.append((0.0,1.0))

        i = 0
        for s in bloque:
            longitud = tablaCod[i][1] - tablaCod[i][0]
            nG = s
            Li = tablaCod[i][0] + (longitud * self.tablaPro[nG][1])
            Ls = tablaCod[i][0] + (longitud * self.tablaPro[nG][2])
#            print nG,  "Li ->", Li , "Ls ->", Ls 
            tablaCod.append((Li,Ls))
            i+=1
        
        return ((tablaCod[i][0]+tablaCod[i][1])/2)
    
    def decodificar(self):
        x = 0
        y = 0
        self.img = (np.zeros((int(self.largo),int(self.ancho))).astype(np.uint8))
        for pro in self.listaPromedios:
            simb = self.buscaCodigo(pro[0])
            self.img[x,y] = simb
            y += 1
            proba = pro[0]
            for i in range(0,pro[1]-1):
               proba = (proba-self.tablaPro[simb][1])/(self.tablaPro[simb][2]-self.tablaPro[simb][1])
               simb = self.buscaCodigo(proba)
               self.img[x,y] = simb
               y += 1
               
               if y == int(self.ancho):
                   y = 0
                   x += 1
        
    def buscaCodigo(self,p):
        cod = -1
        
        for item in self.tablaPro:
            if p > item[1] and p <item[2]:
                cod = item[0]
                break
        
        return cod

    def comprimir(self):
        self.crearTablaPro()
        self.crearTablaOfPromedio()
        self.guardarCodigos()
    
    def descomprimir(self):
        self.leerCodigos()
        self.crearTablaPro()
        self.decodificar()

    def leerCodigos(self):
        fh = open(self.rutaFile,'r')
        decimal.getcontext().prec = 50

        self.largo = int(fh.readline())
        self.ancho = int(fh.readline())
        tamBloque = int(fh.readline())
        
        cadFre = fh.readline()
        frec = cadFre.split("-")

        self.histo = []
        for f in frec:
            self.histo.append(int(f))

        cadProm = fh.readline()
        prom = cadProm.split("|")
        
        for i in range(len(prom)-1):
            self.listaPromedios.append((float(prom[i]),4))

        self.listaPromedios.append((float(prom[len(prom)-1]),tamBloque))
        fh.close()

    def guardarCodigos(self):
        fh = open(self.rutaFile,'w')
        fh.write(str(self.largo)+"\n")
        fh.write(str(self.ancho)+"\n")
        fh.write(str(self.listaPromedios[len(self.listaPromedios)-1][1])+"\n")

        cadAux = ""
        for f in self.histo:
            cadAux += str(f)+"-"
        
        #Se guardar las frecuencias de los niveles de gris 
        fh.write(cadAux[0:len(cadAux)-1]+"\n")
        
        cadAux = ""
        #Se guarda la probabilidades
        for pro in self.listaPromedios:
            cadAux += str(pro[0])+"|"
        
        fh.write(cadAux[0:len(cadAux)-1])
        fh.close()

img = Image.open("/home/miguel/Documentos/PDI/Imagenes/cat.jpg")
#img.show()
#x = np.asarray(img)
#ca = Aritmetica(x,img.histogram(),x.shape[0],x.shape[1],'/home/miguel/Documentos/PDI/Proyecto/Procesamiento Digital de Imagenes/Compresion/prueba.arit')
#ca.comprimir()

ca = Aritmetica(None,None,None,None,'/home/miguel/Documentos/PDI/Proyecto/Procesamiento Digital de Imagenes/Compresion/prueba.arit')
ca.descomprimir()
Image.fromarray(ca.img).show()
