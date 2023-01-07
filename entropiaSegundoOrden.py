
from PIL import Image
import numpy as np

class EstimacionSO():
	
	def __init__(self,img,L,A):
		self.img = img
		self.estimacion = 0
		self.pares = []
		self.largo = L
		self.ancho = A
		self.creaTableOfFrec()

	def creaTableOfFrec(self):
		self.tablaFrec = []
		
		for i in range(256):
			self.tablaFrec.append(np.zeros(256))

	def obtenerEstimacion(self):
		self.generarPares()
		self.obtenerFrecuencias()
		self.calculaEstimacion()
		print self.estimacion
	
	def calculaEstimacion(self):
		suma = 0
		numSimbolos = self.largo*self.ancho

		for T in self.tablaFrec:
			for v in T:
				if v != 0:
					pA = v/float(numSimbolos)
					suma = suma + (pA * np.log2(pA))
					
		self.estimacion = (suma * -1)/2

	def obtenerFrecuencias(self):
		for par in self.pares:
			self.tablaFrec[par[0]][par[1]] += 1

	def generarPares(self):
		array = self.img.flatten()
		for i in range(len(array)):
			if (i+1) < len(array):
				self.pares.append((array[i],array[i+1]))
			else:
				self.pares.append((array[i],array[0]))
		

img = Image.open("/home/miguel/Documentos/PDI/Imagenes/cat.jpg")
#img.show()
x = np.asarray(img)
"""
x = np.asarray([[10,1,8,15,11,4,13,12],
     [6,1,1,2,3,13,4,10],
     [5,8,4,3,11,14,4,3],
     [15,14,11,4,9,0,14,1],
     [1,2,13,10,15,12,2,0],
     [6,1,6,7,14,8,0,4],
     [10,0,13,15,7,1,0,0],
     [11,4,5,13,12,8,15,6]])
"""
est = EstimacionSO(x,x.shape[0],x.shape[1])
est.obtenerEstimacion()
