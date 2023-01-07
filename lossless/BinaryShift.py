from PIL import Image
import Huffman as H
import numpy as np

class BinaryShift(H.Huffman):
    
    def __init__(self,img,hist,L,A,B,rutaFile):
        super(BinaryShift,self).__init__(img,hist,L,A,rutaFile)
        self.numBloques = B
        self.rango = 0
    
    def comprimir(self):
        self.creaBloques(self.numBloques)
        self.obtenerFrecuencias()
        self.muestraTablaSim(self.getTablaSimbolo())
        self.crearCodigo(self.getTablaSimbolo())
        self.crearCadenaCodigo()
        self.escribirCodigo()         
    
    def crearCodigo(self,tablaSimbo):
        numBits = len(np.binary_repr(self.listaBloques[0]))   
        prefijo =  '1'* numBits
        
        j = 0
        for i in range(len(self.listaBloques)):
            nuevoPre = prefijo * i
            for w in range(self.listaBloques[i]):
                cod = nuevoPre + np.binary_repr(w,numBits)
                self.getTablaSimbolo()[j].setCodigo(cod)
                j = j+1

img = Image.open("/home/miguel/Documentos/PDI/Imagenes/cameraman.jpg")
img.show()
x = np.asarray(img)
h = BinaryShift(x,img.histogram(),x.shape[0],x.shape[1],3,'/home/miguel/Documentos/PDI/Proyecto/Procesamiento Digital de Imagenes/Compresion/prueba.bS')
#h.comprimir()
h.descomprimir('/home/miguel/Documentos/PDI/Proyecto/Procesamiento Digital de Imagenes/Compresion/prueba.bS')
Image.fromarray(h.img).show()