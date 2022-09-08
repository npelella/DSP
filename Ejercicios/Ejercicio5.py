"""
@author: Nicolas pelella, Paula Ortega Riera
"""

import numpy as np
import matplotlib.pyplot as plt
import time

# generacion de la señal 

f=10000 
t=np.linspace(0,0.5,44100*0.5)              
x = 2 + np.sin(2*np.pi*f*t)       
M=220

# funcion filtro de media movil "D"

t1 = time.time()                    # Comienza el contador de tiempo de procesamiento

def mediamovild(x,M):
    y=np.zeros((22050))
    for u in range(len(x)):    
        if (len(x)-u) >= M:
            y[u]=sum(x[u:(u+(M-1))])/M     
        else:
            y[u]=sum(x[u:])/len(x[u:]) 
    return y[0:21900]

Tiempo1 = time.time()-t1            # Tiempo total de duración del procesamiento de la señal
print("El tiempo de procesamiento mediante el método de filtrado de media móvil directo fue de:",Tiempo1, "segundos")

# funcion filtro de media movil metodo recursivo

t2 = time.time()                   # Comienza el contador de tiempo de procesamiento

def mediamovilr(x,M):
    y_n=np.ones((22050))
    y1=np.ones((22050))
    for u in range(len(x)):
        if (len(x)-u) >= M and u==0:
            y_n[u]=sum(x[u:(u+(M-1))])
            y1[u]=y_n[u]/M
        elif (len(x)-u) >= M and u!=0:
            y_n[u]=y_n[u-1]-x[u-1]+x[u+(M-1)]
            y1[u]=y_n[u]/M
        else:
            y_n[u]=y_n[u-1]-x[u-1]
            y1[u]=y_n[u]/len(x[u:])
    return y1[0:21900]

Tiempo2 = time.time()-t2           # Tiempo total de duración del procesamiento de la señal
print("El tiempo de procesamiento mediante el método de filtrado de media móvil recursivo fue de:",Tiempo2, "segundos")   

# ploteo de las funciones
plt.subplot(3,1,1)
plt.plot(x,label= 'señal original')
plt.legend(loc=0, shadow=True, fontsize='x-large')
plt.title('Filtrado de señal')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.xlim([0,100])
plt.show() 

plt.subplot(3,1,2)
plt.plot(mediamovild(x,M),label='Media movil')
plt.legend(loc=0, shadow=True, fontsize='x-large')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.xlim([0,100])
plt.tight_layout(0.926,0.121,0.117)
plt.show() 

plt.subplot(3,1,3)
plt.plot(mediamovilr(x,M),label='Media movil "R"')
plt.legend(loc=0, shadow=True, fontsize='x-large')
plt.xlabel('Muestras')
plt.ylabel('Amplitud')
plt.xlim([0,100])
plt.tight_layout(0.926,0.121,0.117)
plt.show() 

