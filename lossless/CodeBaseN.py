from PIL import Image
import Huffman as H
import numpy as np

class CodeBaseN(H.Huffman):
    
    def __init__(self,img,hist,L,A,V,rutaArch,n):
        super(CodeBaseN,self).__init__(img,hist,L,A,rutaArch)
        self.rango = V
        self.base = n
        
    def comprimir(self):
        self.obtenerFrecuencias()
        self.generarCodigo()
        self.crearCadenaCodigo()
        self.escribirCodigo()

    def escribirCodigo(self):
        fh = open(self.rutaFile,'w')
        fh.write(str(self.largo)+"\n")
        fh.write(str(self.ancho)+"\n")
        fh.write(str(self.base)+"\n")
        self.escribirTablaSimbolos(fh)
        self.escribirCadenaCodigo(fh)
        fh.close()           
    
    def crearCadenaCodigo(self):
        #Se crea el diccionario de simbolos
        for simb in self.tablaSimb:
             self.diccionarioSimbolos[simb.getSimbolo()] = simb.getCodigo()
        
        #print self.diccionarioSimbolos
        cont = 1
        for i in range(self.largo):
            for j in range(self.ancho):
                cad = self.diccionarioSimbolos[self.img[i,j]]
                if cont%2 == 0:
                    codRemp = "1"
                else:
                    codRemp = "0"
                #print "Codigo ->",cad,"\n"
                
                cad = cad.replace("C",codRemp)
                #print "CadCodigo->",cad,"\n"                
                #self.diccionarioSimbolos[self.img[i,j]] = cad
                self.cadenaSimbolos += cad
                cont += 1
        
        print self.diccionarioSimbolos
        #print self.cadenaSimbolos
    
    def generarCodigo(self):
        
        nBits = self.base
        i = 0
        while i < 256:            
            LS = int("1"*nBits,2)
            j = 0
            while j < (LS+1) and i < 256:
                cod = self.modificaCodigoRec(np.binary_repr(j,nBits))
                self.getTablaSimbolo()[i].setCodigo(cod)                
                j += 1
                i += 1
                
            nBits+=self.base
        
    def modificaCodigoRec(self,cadCodigo):
        
        nuevoCodigo = ""
        
        if len(cadCodigo) == self.base:
            nuevoCodigo = "C"+cadCodigo
        else:
            n = len(cadCodigo)/self.base
            for i in range(0,n):
                LI = i*self.base
                LS = (i+1)*self.base
                nuevoCodigo += self.modificaCodigoRec(cadCodigo[LI:LS])
        
        return nuevoCodigo
    
    def descomprimir(self, urlImg):
        self.leerCogido(urlImg)
        self.decodificaImagen()                       
        
    def decodificaImagen(self):
        x,y = 0,0
        self.img = (np.zeros((int(self.largo),int(self.ancho))))
    
        LI = 0
        LS = int(self.base) + 1
        while LS < len(self.cadenaSimbolos):
            if self.cadenaSimbolos[LS] == self.cadenaSimbolos[LI]:
                LS += (int(self.base) + 1)
            else:
                palabra = self.cadenaSimbolos[LI:LS]
                LI = LS
                LS += (int(self.base) + 1)
                #print "Codigo = ",palabra,"\n"
                cad = self.convierteCodigo(palabra)
                #print "Codigo Covertido",cad
                #print "Nivel de Gris -> ", self.diccionarioSimbolos[cad]
                self.img[x,y] = self.diccionarioSimbolos[cad]
                y += 1                
            
            if y == int(self.ancho):
                y = 0
                x += 1
                
    def convierteCodigo(self,palabra):
        cad = ""
        i = 0
        while i < len(palabra):
            s = palabra[i]
            if i%(int(self.base)+1)==0:
                s = "C"
            cad += s
            i += 1
        return cad
        
    def leerCogido(self,urlImg):
        
        fh = open(urlImg,'r')
        self.largo = fh.readline()
        self.ancho = fh.readline()
        self.base = fh.readline()
        
        tablaS = fh.readline()
        
        for l in fh.readlines():
            for c in range(len(l)):
                self.cadenaSimbolos += np.binary_repr(ord(l[c]),8)
        
        self.crearDiccionarioSimbolos(tablaS)   
    
        fh.close()
        
img = Image.open("/home/miguel/Documentos/PDI/Imagenes/f3_gs.jpg")
img.show()
x = np.asarray(img)
base = 7
h = CodeBaseN(x,img.histogram(),x.shape[0],x.shape[1],150,'/home/miguel/Documentos/PDI/Proyecto/Procesamiento Digital de Imagenes/Compresion/prueba.cB',base)
#h.comprimir()
h.descomprimir('/home/miguel/Documentos/PDI/Proyecto/Procesamiento Digital de Imagenes/Compresion/prueba.cB')
Image.fromarray(h.img).show()


