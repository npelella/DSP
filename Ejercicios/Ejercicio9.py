"""
@author: Nicolas pelella, Paula Ortega Riera
"""

import numpy as np
import matplotlib.pyplot as plt

M=50
t=np.arange(0,np.pi,2*np.pi/(M*10))

# Genero el pulso rectangular de longuitud M

amplitud = 1/(M)
pulso=np.ones((M))
h_n=amplitud*pulso
h_ejw=np.fft.rfft(h_n,M*10) # le aplico la dft al pulso
h_ejw=abs(h_ejw)
h_ejw=h_ejw[0:len(h_ejw)-1]

# Grafico

plt.plot(t,h_ejw)
plt.title('Respuesta en frecuencia del FMM')
plt.xlabel('Frecuencia [rad]')
plt.ylabel('Magnitud')
plt.show()