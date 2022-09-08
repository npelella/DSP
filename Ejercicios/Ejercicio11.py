"""
@author: Nicolas pelella, Paula Ortega Riera
"""

import numpy as np
import librosa as lb
import matplotlib.pyplot as plt

# Se importan los audios respectivos al ejercicio 8

x,f1 = lb.core.load("Midi69.wav",sr=None) # Importa la señal "Midi69".

Ri,f2 = lb.core.load("RIR.wav",sr=None) # Importa la respuesta al impulso "RIR".

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

	return y1,Len

ConvCZ,Len = ConvCZ(x,Ri)

m3 = np.linspace(0,len(ConvCZ)-1,len(ConvCZ))	 # Vector de muestras
t3 = m3/f2                                   # Vector de tiempo [s]
ConvCZ = ConvCZ/max(ConvCZ)                     # Normalización 

# Largo necesario

print('Largo necesario para la condición de equivalencia de la convolución circular y la convolución lineal es:', Len)

# Ploteo de la señal 

plt.plot(t3,ConvCZ)
plt.title('Convolución Circular')
plt.ylabel('Amplitud')
plt.xlabel('Tiempo (s)')
plt.tight_layout(0.926,0.121,0.117)
plt.show()

#Vector resultante de muestras

print('Vector resultante de la convolución:',ConvCZ)