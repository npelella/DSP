"""
@author: Nicolas pelella, Paula Ortega Riera
"""

import numpy as np
import matplotlib.pyplot as plt

# Se generan señales aleatorias de media cero y valores distintos de desvío:

señal1 = np.array(np.random.normal(0,0.1,22050))   # Ruido de media 0 y desvío 0.1

señal2 = np.array(np.random.normal(0,1,22050))     # Ruido de media 0 y desvío 1

señal3 = np.array(np.random.normal(0,3,22050))     # Ruido de media 0 y desvío 3

# Señal generada en el punto 1:

    
f=10000  # Frecuencia [Hz]
t=np.linspace(0,0.5,44100*0.5)              # Tiempo de duración [s]
x = 2 + np.sin(2*np.pi*f*t)        # Señal senoidal pedida

#Se suma cada señal con la señal generada en el punto número 1 y se las normaliza.

x01 = (x + señal1)/(np.max(x+señal1))
x1 = (x + señal2)/(np.max(x+señal2))
x3 = (x + señal3)/(np.max(x+señal3))

#Gráfico de las señales:
plt.subplot(3,1,1)
plt.plot(x01[100:400],label='x01')
plt.legend(loc=0, shadow=True, fontsize='x-large')
plt.title('Suma de señal original y Ruido 1')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.show()
plt.subplot(3,1,2)
plt.plot(x1[100:400],label='x1')
plt.legend(loc=0, shadow=True, fontsize='x-large')
plt.title('Suma de señal original y Ruido 2')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.show()
plt.subplot(3,1,3)
plt.plot(x3[100:400],label='x3')
plt.legend(loc=0, shadow=True, fontsize='x-large')
plt.title('Suma de señal original y Ruido 3')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.tight_layout(0.926,0.121,0.117)
plt.show()


#Se calcula la SNR de las 3 señales de suma:

SNR1 = np.max(x)/0.1
print('La relación señal ruido de la señal 1 es:', SNR1)
SNR2 = np.max(x)
print('La relación señal ruido de la señal 2 es:', SNR2)
SNR3 = np.max(x)/3
print('La relación señal ruido de la señal 3 es:', SNR3)
