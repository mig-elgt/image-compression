from PIL import Image
import numpy as np

def firstOrder(histo,numSimbolos):
	suma = 0
	for a in histo:
		pA = a/numSimbolos
		suma = suma + (pA * np.log2(pA))
	return (suma * -1)
    
img = Image.open("/home/miguel/Documentos/PDI/Imagenes/cat.jpg")
x = np.asarray(img)
print firstOrder(img.histogram(),float(x.shape[0]*x.shape[1]))
