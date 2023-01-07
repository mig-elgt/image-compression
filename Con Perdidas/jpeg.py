# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 11:25:37 2013

@author: miguel
"""
from PIL import Image
import numpy
from scipy.fftpack import dct

class dc_cod:
    def __init__(self, cat, code):
        self.cat = cat
        self.code = code

    def __repr__(self):
        return repr((self.cat, self.code))

class ac_cod:
    def __init__(self, run, cat, code):
        self.run = run
        self.cat = cat
        self.code = code

    def __repr__(self):
        return repr((self.run, self.cat, self.code))

dc_codes = {0:'010',1:'011',2:'100',3:'00',4:'101',5:'110',6:'1110',7:'11110',8:'111110',9:'1111110',10:'11111110',11:'111111110'}        

ac_codes = [
ac_cod(0,1000,'1010'), 
ac_cod(0,1,'00'), 
ac_cod(0,2,'01'), 
ac_cod(0,3,'100'), 
ac_cod(0,4,'1011'), 
ac_cod(0,5,'11010'), 
ac_cod(0,6,'111000'), 
ac_cod(0,7,'1111000'), 
ac_cod(0,8,'1111110110'), 
ac_cod(0,9,'1111111110000010'), 
ac_cod(0,1,'1111111110000011'), 
ac_cod(1,10,'1100'), 
ac_cod(1,2,'111001'), 
ac_cod(1,3,'1111001'), 
ac_cod(1,4,'111110110'), 
ac_cod(1,5,'11111110110'), 
ac_cod(1,6,'1111111110000100'), 
ac_cod(1,7,'1111111110000101'), 
ac_cod(1,8,'1111111110000110'),
ac_cod(1,9,'1111111110000111'), 
ac_cod(1,10,'1111111110001000'), 
ac_cod(2,1,'11011'), 
ac_cod(2,2,'11111000'), 
ac_cod(2,3,'1111110111'), 
ac_cod(2,4,'1111111110001001'), 
ac_cod(2,5,'1111111110001010'), 
ac_cod(2,6,'1111111110001011'), 
ac_cod(2,7,'1111111110001100'), 
ac_cod(2,8,'1111111110001101'), 
ac_cod(2,9,'1111111110001110'), 
ac_cod(2,10,'1111111110001111'), 
ac_cod(3,1,'111010'), 
ac_cod(3,2,'111110111'), 
ac_cod(3,3,'11111110111'), 
ac_cod(3,4,'1111111110010000'), 
ac_cod(3,5,'1111111110010001'), 
ac_cod(3,6,'1111111110010010'),
ac_cod(3,7,'1111111110010011'), 
ac_cod(3,8,'1111111110010100'), 
ac_cod(3,9,'1111111110010101'), 
ac_cod(3,10,'1111111110010110'), 
ac_cod(4,1,'111011'), 
ac_cod(4,2,'1111111000'), 
ac_cod(4,3,'1111111110010111'), 
ac_cod(4,4,'1111111110011000'), 
ac_cod(4,5,'1111111110011001'), 
ac_cod(4,6,'1111111110011010'), 
ac_cod(4,7,'1111111110011011'), 
ac_cod(4,8,'1111111110011100'), 
ac_cod(4,9,'1111111110011101'), 
ac_cod(4,10,'1111111110011110'), 
ac_cod(5,1,'1111010'), 
ac_cod(5,2,'1111111001'), 
ac_cod(5,3,'1111111110011111'), 
ac_cod(5,4,'1111111110100000'), 
ac_cod(5,5,'1111111110100001'), 
ac_cod(5,6,'1111111110100010'), 
ac_cod(5,7,'1111111110100011'), 
ac_cod(5,8,'1111111110100100'), 
ac_cod(5,9,'1111111110100101'), 
ac_cod(5,10,'1111111110100110'), 
ac_cod(6,1,'1111011'), 
ac_cod(6,2,'11111111000'), 
ac_cod(6,3,'1111111110100111'), 
ac_cod(6,4,'1111111110101000'), 
ac_cod(6,5,'1111111110101001'), 
ac_cod(6,6,'1111111110101010'), 
ac_cod(6,7,'1111111110101011'), 
ac_cod(6,8,'1111111110101100'), 
ac_cod(6,9,'1111111110101101'), 
ac_cod(6,10,'1111111110101110'), 
ac_cod(7,1,'11111001'), 
ac_cod(7,2,'11111111001'), 
ac_cod(7,3,'1111111110101111'), 
ac_cod(7,4,'1111111110110000'), 
ac_cod(7,5,'1111111110110001'), 
ac_cod(7,6,'1111111110110010'), 
ac_cod(7,7,'1111111110110011'), 
ac_cod(7,8,'1111111110110100'), 
ac_cod(7,9,'1111111110110101'), 
ac_cod(7,10,'1111111110110110'), 
ac_cod(8,1,'11111010'), 
ac_cod(8,2,'111111111000000'), 
ac_cod(8,3,'1111111110110111'), 
ac_cod(8,4,'1111111110111000'), 
ac_cod(8,5,'1111111110111001'), 
ac_cod(8,6,'1111111110111010'), 
ac_cod(8,7,'1111111110111011'), 
ac_cod(8,8,'1111111110111100'), 
ac_cod(8,9,'1111111110111101'), 
ac_cod(8,10,'1111111110111110'), 
ac_cod(9,1,'111111000'), 
ac_cod(9,2,'1111111110111111'), 
ac_cod(9,3,'1111111111000000'), 
ac_cod(9,4,'1111111111000001'), 
ac_cod(9,5,'1111111111000010'), 
ac_cod(9,6,'1111111111000011'), 
ac_cod(9,7,'1111111111000100'), 
ac_cod(9,8,'1111111111000101'), 
ac_cod(9,9,'1111111111000110'), 
ac_cod(9,10,'1111111111000111'), 
ac_cod(10,1,'111111001'), 
ac_cod(10,2,'1111111111001000'), 
ac_cod(10,3,'1111111111001001'), 
ac_cod(10,4,'1111111111001010'), 
ac_cod(10,5,'1111111111001011'), 
ac_cod(10,6,'1111111111001100'), 
ac_cod(10,7,'1111111111001101'), 
ac_cod(10,8,'1111111111001110'), 
ac_cod(10,9,'1111111111001111'), 
ac_cod(10,10,'1111111111010000'), 
ac_cod(11,1,'111111010'), 
ac_cod(11,2,'1111111111010001'), 
ac_cod(11,3,'1111111111010010'), 
ac_cod(11,4,'1111111111010011'), 
ac_cod(11,5,'1111111111010100'), 
ac_cod(11,6,'1111111111010101'), 
ac_cod(11,7,'1111111111010110'), 
ac_cod(11,8,'1111111111010111'), 
ac_cod(11,9,'1111111111011000'), 
ac_cod(11,10,'1111111111011001'), 
ac_cod(12,1,'1111111010'), 
ac_cod(12,2,'1111111111011010'), 
ac_cod(12,3,'1111111111011011'),  
ac_cod(12,4,'1111111111011100'), 
ac_cod(12,5,'1111111111011101'),  
ac_cod(12,6,'1111111111011110'),  
ac_cod(12,7,'1111111111011111'),  
ac_cod(12,8,'1111111111100000'),  
ac_cod(12,9,'1111111111100001'),  
ac_cod(12,10,'1111111111100010'),  
ac_cod(13,1,'11111111010'), 
ac_cod(13,2,'1111111111100011'), 
ac_cod(13,3,'1111111111100100'), 
ac_cod(13,4,'1111111111100101'), 
ac_cod(13,5,'1111111111100110'), 
ac_cod(13,6,'1111111111100111'), 
ac_cod(13,7,'1111111111101000'), 
ac_cod(13,8,'1111111111101001'), 
ac_cod(13,9,'1111111111101010'), 
ac_cod(13,10,'1111111111101011'), 
ac_cod(14,1,'111111110110'), 
ac_cod(14,2,'1111111111101100'), 
ac_cod(14,3,'1111111111101101'), 
ac_cod(14,4,'1111111111101110'), 
ac_cod(14,5,'1111111111101111'), 
ac_cod(14,6,'1111111111110000'), 
ac_cod(14,7,'1111111111110001'), 
ac_cod(14,8,'1111111111110010'), 
ac_cod(14,9,'1111111111110011'), 
ac_cod(14,10,'1111111111110100'), 
ac_cod(15,0,'111111110111'), 
ac_cod(15,1,'1111111111110101'), 
ac_cod(15,2,'1111111111110110'), 
ac_cod(15,3,'1111111111110111'), 
ac_cod(15,4,'1111111111111000'), 
ac_cod(15,5,'1111111111111001'), 
ac_cod(15,6,'1111111111111010'), 
ac_cod(15,7,'1111111111111011'), 
ac_cod(15,8,'1111111111111100'), 
ac_cod(15,9,'1111111111111101'), 
ac_cod(15,10,'1111111111111110')
]

def zigzag(n,img):
	arr = numpy.zeros([64])
	
	indexorder = sorted(((x,y) for x in range(n) for y in range(n)),
		key = lambda(x,y): (x+y,-y if (x+y) % 2 else y) )
	cont = 0
    	for p in indexorder:
         i = p[0]
         j = p[1]
         arr[cont] = img[i,j]
         cont +=1
         
	return arr

def obtenerVector(array):
    arrayZigZag = zigzag(8,array)
    
    pos = len(arrayZigZag)-1;
    while(1):
        if arrayZigZag[pos] != 0:
            break;
        else:
            pos = pos-1;
    return arrayZigZag[:pos+1]

img = Image.open("/home/miguel/Documentos/PDI/Imagenes/cameraman.jpg")
x = numpy.asarray(img)

bloque = x[0:8,0:8]

cuantificacion = numpy.array(  [[16,11,10,16,24,40,51,61],
				[12,12,14,19,26,58,60,55],
				[14,13,16,24,40,57,69,56],
				[14,17,22,29,51,87,88,62],
				[18,22,37,56,68,109,103,77],
				[24,35,55,64,81,104,113,92],
				[49,64,78,87,103,121,120,101],
				[72,92,95,98,112,100,103,99]]).astype(numpy.float32)

paso1 = (bloque - 128).astype(numpy.float32)
paso2 = dct(dct(paso1, norm='ortho', axis=0), norm='ortho', axis=1)
#print "Img con DCT\n", paso2

paso3 =  numpy.round((paso2/cuantificacion)).astype(numpy.int16)
print "\nImagen transformada DCT:\n ",paso3

coeficientes = obtenerVector(paso3)
print "Vector de coeficientes ",coeficientes

def obtenerCodigoBase(run,cat):
    for ac in ac_codes:
        if run == ac.run and cat == ac.cat:
            return ac.code
    
    return ""

def creaCadenaCodigo():
    cad = ""
    for i in cadenaCodigo:
        cad += i
    
    return cad
    
def codifica(coeficientes):
    #Se define el codigo cd    
    dc = abs(int(coeficientes[0]))
    x = len(numpy.binary_repr(dc))
    base = dc_codes[x]

    if int(coeficientes[0]) < 0:
        c = numpy.binary_repr(~dc,x)
    else:
        c = numpy.binary_repr(dc,x)
    
    codDc = base + c
    cadenaCodigo.append(str(codDc))
    print codDc
    ceros = 0 
    
    for i in range(1,len(coeficientes)):
        sim = coeficientes[i]

        if(sim ==  0):
            ceros += 1
        
        cate = len(numpy.binary_repr(abs(int(sim))))
        print "Categoria : ", cate
        codBase = obtenerCodigoBase(ceros,cate)
        print "ceros ", ceros
        if sim < 0:
            c = numpy.binary_repr(~abs(int(sim)),cate)
        else:
            c = numpy.binary_repr(abs(int(sim)),cate)
        
        codAc = codBase + c
        print "Codigo base : ", codBase, "Codigo Ac :" ,c
        print codAc
        cadenaCodigo.append(str(codAc))
        
cadenaCodigo = []
codifica(coeficientes)

cadenaFinal = creaCadenaCodigo()
print "Cadena Final Codificada ->>", cadenaFinal


















