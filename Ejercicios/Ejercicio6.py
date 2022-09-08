"""
@author: Nicolas pelella, Paula Ortega Riera
"""

import numpy as np
import matplotlib.pyplot as plt

# generacion de la señal

f=10000  # Frecuencia [Hz]
t=np.linspace(0,0.5,44100*0.5)              # Tiempo de duración [s]
x = 2 + np.sin(2*np.pi*f*t)        # Señal senoidal pedida

# funcion filtro de media movil metodo por convolucion

def mediamovil(x):
    M=round(0.01*len(x))
    amplitud = 1/(M)
    pulso=np.ones((M))
    h_n=amplitud*pulso
    y_n1=np.convolve(x,h_n,'valid')
    return y_n1

# graficos

plt.subplot(2,1,1)    
plt.plot(x,label='Señal original')
plt.legend(loc=0, shadow=True, fontsize='x-large')
plt.title('Señal')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.xlim([0,100])
plt.show() 

plt.subplot(2,1,2)
plt.plot(mediamovil(x),label='Media movil "C"')
plt.legend(loc=0, shadow=True, fontsize='x-large')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.xlim([0,100])
plt.tight_layout(0.926,0.121,0.117)
plt.show() 