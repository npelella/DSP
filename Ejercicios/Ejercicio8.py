"""
@author: Nicolas pelella, Paula Ortega Riera
"""

import numpy as np
import librosa as lb
import matplotlib.pyplot as plt

#CONVOLUCIÓN LINEAL DE LA SEÑAL "Midi69.wav" CON LA RESPUESTA AL IMPULSO "RIR.wav" .

x,f1 = lb.core.load("Midi69.wav",sr=None) # Importa la señal "Midi69".

Ri,f2 = lb.core.load("RIR.wav",sr=None) # Importa la respuesta al impulso "RIR".

# Se define la convolución lineal de las señales:

def Convl(x,Ri):  # Función de convolución de la señal X y la respuesta al impulso Ri de forma lineal

    y_conv=np.convolve(x,Ri) # Convolución lineal entre señales

    return y_conv

conv_lineal=Convl(x,Ri)

m1 = np.linspace(0,len(conv_lineal)-1,len(conv_lineal))	# Vector de muestras
t1 = m1/f2									            # Vector de tiempo [s]
conv_lineal = conv_lineal/max(conv_lineal)		        # Normalización


#CONVOLUCIÓN CIRCULAR DE LA SEÑAL "Midi69.wav" CON LA RESPUESTA AL IMPULSO "RIR.wav" .

# Se define la convolución circular de las señales:

def ConvC(x,Ri): # Función de convolución de la señal X y la respuesta al impulso Ri de forma circular

# Compensación con ceros de la señal de menor longitud
	
	if len(Ri)> len(x): 
        
		Cx = np.zeros(len(Ri)-len(x))  # Cantidad de ceros necesarios para X
		x = np.concatenate((x,Cx))     # Compensación en X

	elif len(Ri) < len(x):
        
		CRi = np.zeros(len(x)-len(Ri)) # Cantidad de ceros necesarios para Ri
		Ri = np.concatenate((Ri,CRi))  # Compensación en Ri


	DFT_x = np.fft.fft(x)          # DFT de X
	DFT_Ri = np.fft.fft(Ri)        # DFT de Ri
	prod = DFT_x * DFT_Ri          # Multiplicación de las DFT de ambas señales

	y0=np.fft.ifft(prod) # Antitransformada del producto para obtener la Convolución circular
	y0 = y0.astype(float)
	return y0

ConvC=ConvC(x,Ri)

m2 = np.linspace(0,len(ConvC)-1,len(ConvC))	 # Vector de muestras
t2 = m2/f2                                   # Vector de tiempo [s]
ConvC = ConvC/max(ConvC)                     # Normalización 

#CONVOLUCIÓN CIRCULAR DE LA SEÑAL "Midi69.wav" CON LA RESPUESTA AL IMPULSO "RIR.wav" TAL QUE SEA EQUIVALENTE A LA CONVOLUCIÓN LINEAL DE LAS MISMAS SEÑALES.

# Se define la convolución circular de las señales utilizando la herramienta de Zero Padding:

def ConvCZ(x,Ri):  # Función de convolución de la señal X y la respuesta al impulso Ri de forma circular con Zero Padding
	
	Len = len(Ri)+len(x)-1          # Longitud necesaria para cumplir condiciones de igualdad entre convolución lineal y circular
	CRi1 = np.zeros(Len-len(Ri))    # Cantidad de ceros necesarios para Ri
	CX1 = np.zeros(Len-len(x))      # Cantidad de ceros necesarios para X
	Ri1 = np.concatenate((Ri,CRi1)) # Compensación en Ri
	x1 = np.concatenate((x,CX1))    # Compensación en X

	DFT_x1 = np.fft.fft(x1) # DFT de X
	DFT_Ri1 = np.fft.fft(Ri1) # DFT de Ri
	prod1 = DFT_x1 * DFT_Ri1 # Multiplicación de las DFT de ambas señales

	y1=np.fft.ifft(prod1) # Antitransformada del producto para obtener la Convolución circular
	y1 = y1.astype(float)

	return y1

ConvCZ= ConvCZ(x,Ri)

m3 = np.linspace(0,len(ConvCZ)-1,len(ConvCZ))	 # Vector de muestras
t3 = m3/f2                                   # Vector de tiempo [s]
ConvCZ = ConvCZ/max(ConvCZ)                     # Normalización 

#generación de archivo .wav de cada convolución

lb.output.write_wav('8-Conv. Lineal.wav', conv_lineal, f2) 
lb.output.write_wav('8-Conv. Circular.wav', ConvC, f2)
lb.output.write_wav('8-Conv. Circular ZP.wav', ConvCZ, f2)

# ploteo de las señales


plt.subplot(3,1,1)
plt.plot(t1,conv_lineal)
plt.title('Convolución Lineal')
plt.ylabel('Amplitud')
plt.xlabel('Tiempo (s)')
plt.subplot(3,1,2)
plt.plot(t2,ConvC)
plt.title('Convolución Circular')
plt.ylabel('Amplitud')
plt.xlabel('Tiempo (s)')
plt.subplot(3,1,3)
plt.plot(t3,ConvCZ)
plt.title('Convolución Circular ZP')
plt.ylabel('Amplitud')
plt.xlabel('Tiempo (s)')
plt.tight_layout(0.926,0.121,0.117)
plt.show()




