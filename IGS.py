# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:09:37 2013

@author: miguel
"""
from PIL import Image
import numpy as np

class IGS(object):
    
    def __init__(self,n_img,nB,ruta):
        
        self.img = n_img
        self.largo = n_img.shape[0]
        self.ancho = n_img.shape[1]
        self.numBits = nB
        self.imgCod = np.zeros((self.largo,self.ancho))
        self.cadCodigo = ""
        self.urlImg = ruta
        
    def generaCodigo(self):
        
        suma = 0
        
        for x in range(self.largo):
            for y in range(self.ancho):
                valor = self.img[x,y]
                
                if valor >= ((2**self.numBits)-1)<<(8-self.numBits):
                    suma = valor
                else:
                    suma = valor + (suma & (2**self.numBits)-1)
                
                self.imgCod[x,y] = (suma & ((2**self.numBits-1)<<(8-self.numBits)))>>(8-self.numBits)
        
        return self.imgCod
    
    def comprimir(self):
        
        self.generaCodigo()
        self.creaCadCodigo()
        self.escribeCodigo()
        
        return self.imgCod
    
    def creaCadCodigo(self):
        
        for i in range(self.largo):
           for j in range(self.ancho):
                self.cadCodigo += np.binary_repr(self.imgCod[i,j],self.numBits)
    
    def escribeCodigo(self):
        
        palabra = ""
        fh = open(self.urlImg ,'w')
        
        fh.write(str(self.largo)+"\n")
        fh.write(str(self.ancho)+"\n")
        fh.write(str(self.numBits)+"\n")
        
        for i in range(len(self.cadCodigo)):
            palabra += self.cadCodigo[i]
            if((i+1)%8 == 0):
               fh.write(chr(int(palabra,2)))
               palabra = ""
        
        fh.close()
    
    def abrirImageComprimida(self, urlImg):
        
        self.leerFile(urlImg)
        self.decodificaIGS()
        return self.imgCod
    
    def leerFile(self,img):
        
        fh = open(img,'r')
        
        self.largo = fh.readline()
        self.ancho = fh.readline()
        self.numBits = fh.readline()
        self.cadCodigo = ""      
        
        for l in fh.readlines():
            for c in range(len(l)):
                self.cadCodigo += np.binary_repr(ord(l[c]),8)
        
        fh.close()        
    
    def decodificaIGS(self):
        
        x,y = 0,0        
        cont = 0
        palabra = ""
        self.imgCod = (np.zeros((int(self.largo),int(self.ancho))))
        
        for i in self.cadCodigo:
            palabra += i
            cont += 1
            
            if cont == int(self.numBits):
                self.imgCod[x,y] = int(palabra,2)
                palabra = ""                
                cont = 0                
                y += 1
           
            if y == int(self.largo):
                y = 0
                x += 1

    
def normalizar(img_c,numBits):
    return ((img_c/float((2**numBits)-1))*255).astype(np.uint8)

img = Image.open("/home/miguel/Documentos/PDI/Imagenes/cameraman.jpg")
img.show()
numBits = 7

igc = IGS(np.asarray(img),numBits,'/home/miguel/Documentos/PDI/PDI-Programas/Compresion/montes.igs')

#imgC = igc.comprimir()
imgD = igc.abrirImageComprimida('/home/miguel/Documentos/PDI/PDI-Programas/Compresion/montes.igs')

#Image.fromarray(normalizar(imgC,numBits)).show()
Image.fromarray(normalizar(imgD,numBits)).show()




                
            
            
    