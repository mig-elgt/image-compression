# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:07:59 2013

@author: miguel
"""
from PIL import Image
import numpy as np

class RLE():
    
    def __init__(self,img,L,A,pathImg):
        self.rutaImg = pathImg  
        self.imagen = img
        self.largo = L
        self.ancho = A
        self.listPlanos = []
        self.listaPares= []
        self.listaParesPorPlano = []

    def crearListPares(self):
        for i in range(8):
            self.listaPares.append([])
            
    def comprimir(self):
        self.crearPlanosBits()
        self.crearListPares()
        self.crearPares()
        self.escribirCodigo()
        print self.listPlanos[7][255]
        self.decodoficar()
        
    def crearPlanosBits(self):
        for i in range(8):        
            self.listPlanos.append((self.imagen & (2**i))>>i)
    
    def crearPares(self):
        numPlano = 0
        for plano in self.listPlanos:
            
            pAux = plano.flatten()
            bit = pAux[0]
            cont = 0  

            for i in range(len(pAux)):
                if(pAux[i]==bit):
                    cont = cont + 1
                else:
                    par = (bit,cont)
                    self.listaPares[numPlano].append(par)
                    bit = pAux[i]
                    cont = 1
            
            if cont >= 1:
                par = (bit,cont)
                self.listaPares[numPlano].append(par)
            
            numPlano += 1

    def escribirCodigo(self):
        fh = open(self.rutaImg,'w')
        fh.write(str(self.largo)+"\n")
        fh.write(str(self.ancho)+"\n")
        
        for t in self.listaPares:
            fh.write(str(len(t))+"\n")
        
        cadAux = ""
        for pares in self.listaPares:
            for par in pares:
                cadAux += str(par[0])+","+str(par[1])+"-"
        
        fh.write(cadAux[0:len(cadAux)-1])
        fh.close()
    
    def descomprimir(self):
        self.leerCodigo()
        print self.listPlanos[7][255]
        self.decodoficar()

    def leerCodigo(self):
        fh = open(self.rutaImg,'r')
        self.largo = int(fh.readline())
        self.ancho = int(fh.readline())
        
        tamPares = []
        for i in range(8):
            tamPares.append(int(fh.readline()))

        cad = fh.readline()
        listPares = cad.split("-")
        
        self.listPlanos = []

        LI = 0
        LS = 0
        cont = 0
        for t in tamPares:
            LS += t
            pares = listPares[LI:LS]
            plano = (np.zeros((int(self.largo),int(self.ancho)))).astype(np.uint8)
            x = 0
            y = 0
            print "Pares de plano"
            print len(pares)
            print pares
            for par in pares:
                print par
                aux = par.split(",")
                for i in range(int(aux[1])):
                    plano[x,y] = par[0]
                    y += 1
                    if y == self.ancho:
                       y = 0
                       x += 1
            

            cont += 1
            LI = LS
            self.listPlanos.append(plano)

        print cont

    def decodoficar(self):
        a = self.listPlanos[0]
        for i in range(1,8):
            b = self.listPlanos[i]
            a = (b<<i)|a
        Image.fromarray(a).show()
        print a

"""
img = Image.open("/home/miguel/Documentos/PDI/Imagenes/cat.jpg")
x = np.asarray(img)
rle = RLE(x,x.shape[0],x.shape[1],'/home/miguel/Documentos/PDI/PDI-Programas/Compresion/prueba.rle')
rle.comprimir()
"""

rle2 = RLE(None,None,None,'/home/miguel/Documentos/PDI/PDI-Programas/Compresion/prueba.rle')
rle2.descomprimir()

"""
#print "Imagen ori", x
#print x.flatten()
#img.show()
"""