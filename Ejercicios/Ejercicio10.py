"""
@author: Nicolas pelella, Paula Ortega Riera
"""

import numpy as np
import matplotlib.pyplot as plt



M=1000 # cantidad de muestras de ambas ventanas
t=np.arange(0,np.pi,2*np.pi/(4056)) # matriz para representar a las ventanas en frecuencia [rad]

# Ventana Blackman

a0=0.42
a1=0.5
a2=0.08
n=np.arange(M)
v_n=a0-a1*np.cos((2*np.pi*n)/(M-1))+a2*np.cos((4*np.pi*n)/(M-1))
h_ejw1=np.fft.rfft(v_n,4056) # la dft de la ventana blackman
h_ejw1=abs(h_ejw1)
fblackmanabs=h_ejw1/np.max(h_ejw1)
blackman_db=20*np.log10(fblackmanabs) # pasaje a db de la dft de la ventana blackman
blackman_db=blackman_db[0:len(blackman_db)-1]

# Pulso rectangular

amplitud = 1/(M)
pulso=np.ones((M))
h_n=amplitud*pulso
h_ejw=np.fft.rfft(h_n,4056) # la dft del pulso rectangular
h_ejw=abs(h_ejw)
frectangularabs=h_ejw/np.max(h_ejw)
rect_db=20*np.log10(frectangularabs) # pasaje a db de la dft de la ventana rectangular
rect_db=rect_db[0:len(rect_db)-1]

# Graficos

plt.plot(t,rect_db, label='V. Rectangular [dB]') # Ventana rectangular
plt.plot(t,blackman_db, label='V. Blackman [dB]') # Ventana blackman
plt.legend(loc=0, shadow=True, fontsize='x-large')
plt.title('Respuesta en frecuencia de ventanas')
plt.xlabel('Frecuencia [rad]')
plt.ylabel('Magnitud [dB]')
plt.xlim([0,(np.pi)/8])
plt.show()

""" 
observaciones:
    En cuanto a los valores de atenuacion, graficamente se puede ver que la 
    ventana blackman presenta mayor atenuacion que la ventana rectangular.
    Por otro lado, el lobulo principal de la ventana rectangular es mas angosto 
    que el de la ventana blackman
    
"""