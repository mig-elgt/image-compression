from PIL import Image
import Huffman as H
import numpy as np
import Simbolo as S

class HuffmanShift(H.Huffman):
    
    def __init__(self,img,hist,L,A,B,rutaArchivo):
        super(HuffmanShift,self).__init__(img,hist,L,A,rutaArchivo)
        self.numBloques = B
        self.rango = 0
        
    def comprimir(self):
        self.creaBloques(self.numBloques)
        self.obtenerFrecuencias()
        self.rango = self.listaBloques[0]
        sumaPro = self.sumarProba(self.rango,self.getTablaSimbolo())
        T = self.getTablaSimbolo()[:self.rango]     
        simboloX = S.Simbolo('X',sumaPro)
        self.insertOrd(simboloX,T)
        self.generaCodigo(T)
        self.crearCodigosConPrefijo(simboloX.getCodigo(),self.getTablaSimbolo())
        self.crearCadenaCodigo()
        self.escribirCodigo()         
       
    def crearCodigosConPrefijo(self,prefijo,tablaSimbo):
        
        j = self.listaBloques[0]
        for i in range(1,len(self.listaBloques)):
            pre = prefijo*i
            print "pre",pre
            for w in range(self.listaBloques[i]):
                cod = pre + tablaSimbo[w].getCodigo()
                self.getTablaSimbolo()[j].setCodigo(cod)
                j = j+1

img = Image.open("/home/miguel/Documentos/PDI/Imagenes/f3_gs.jpg")
img.show()
x = np.asarray(img)
h = HuffmanShift(x,img.histogram(),x.shape[0],x.shape[1],4,'/home/miguel/Documentos/PDI/Proyecto/Procesamiento Digital de Imagenes/Compresion/prueba.hS')
#h.comprimir()
h.descomprimir('/home/miguel/Documentos/PDI/Proyecto/Procesamiento Digital de Imagenes/Compresion/prueba.hS')
Image.fromarray(h.img).show()