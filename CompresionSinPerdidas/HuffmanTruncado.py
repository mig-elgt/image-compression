from PIL import Image
import Huffman as H
import numpy as np
import Simbolo as S

class HuffmanTruncado(H.Huffman):
    
    def __init__(self,img,hist,L,A,V,rutaArch):
        super(HuffmanTruncado,self).__init__(img,hist,L,A,rutaArch)
        self.rango = V        
        
    def comprimir(self):
        self.obtenerFrecuencias()
        sumaPro = self.sumarProba(self.rango,self.getTablaSimbolo())        
        T = self.getTablaSimbolo()[:self.rango]
        simboloX = S.Simbolo('X',sumaPro)
        self.insertOrd(simboloX,T)
        self.generaCodigo(T)
        self.crearCodigosConPrefijo(simboloX.getCodigo(),self.getTablaSimbolo())
        self.crearCadenaCodigo()
        self.escribirCodigo()          

    def crearCodigosConPrefijo(self,prefijo,tablaSimbo):
        nBits = len(np.binary_repr(256-self.rango))
        for i in range(self.rango,256):
            codigo = prefijo+ np.binary_repr(i-self.rango,nBits)
            self.tablaSimb[i].setCodigo(codigo)
    

img = Image.open("/home/miguel/Documentos/PDI/Imagenes/cameraman.jpg")
img.show()
x = np.asarray(img)
h = HuffmanTruncado(x,img.histogram(),x.shape[0],x.shape[1],150,'/home/miguel/Documentos/PDI/Proyecto/Procesamiento Digital de Imagenes/Compresion/prueba.hT')
h.comprimir()
#h.descomprimir('/home/miguel/Documentos/PDI/Proyecto/Procesamiento Digital de Imagenes/Compresion/prueba.hT')
#Image.fromarray(h.img).show()
h.muestraTablaSim(h.tablaSimb)