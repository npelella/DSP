"""
@author: Nicolas pelella, Paula Ortega Riera
"""

import numpy as np
import matplotlib.pyplot as plt

# senial del punto 1

f=10000  # Frecuencia [Hz]
t=np.linspace(0,0.5,44100*0.5)              # Tiempo de duración [s]
x = 2+np.sin(2*np.pi*f*t)        # Señal senoidal pedida

# funcion de la ventana blackman

def ventanablackman(x):
    a0=0.42
    a1=0.5
    a2=0.08
    M=round(0.01*len(x))
    n=np.arange(M)
    v_n=a0-a1*np.cos((2*np.pi*n)/(M-1))+a2*np.cos((4*np.pi*n)/(M-1))
    y_n2=np.convolve(x,v_n,'valid')
    return y_n2 

# grafico

plt.subplot(2,1,1)    
plt.plot(x)
plt.title('Señal')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.xlim([0,100])
plt.show() 

plt.subplot(2,1,2)    
plt.plot(ventanablackman(x))
plt.title('Señal con ventana Blackman')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.xlim([0,100])
plt.tight_layout(0.926,0.121,0.117)
plt.show()
