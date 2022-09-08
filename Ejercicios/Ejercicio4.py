"""
@author: Nicolas pelella, Paula Ortega Riera
"""

import numpy as np



# Señal del punto 1:
 
f=10000  # Frecuencia [Hz]
t=np.linspace(0,0.5,44100*0.5)              # Tiempo de duración [s]
x = 2 + np.sin(2*np.pi*f*t)        # Señal senoidal pedida

# Se crean 10 señales de ruido con media nula y desvío estandar igual a 3:

x_rand = list(range(0 ,10))    # Se genera el arreglo que contiene las 10 señales de ruido
x_suma    = list(range(0,10))  # Se genera el arreglo que contiene las 10 señales de ruido sumadas a la señal original
x_prom= 0 *np.array(range(0,22050))  # Promedio de todas las señales con ruido agregado

for i in range(0,10):
    x_rand[i] = np.array(np.random.normal(0,3,22050)) # Creación de señales de ruido con media nula y desvío 3
    x_suma[i] = x + x_rand[i]    # Suma de cada señal de ruido con la señal original
    if i<9:
        x_prom= x_prom + x_suma[i]   # Promediado de señales 
    else:
        x_prom= (x_prom + x_suma[i])/10
        
        
SNR_prom = np.max(x_prom)/3  # Relación señal ruido de las señales con ruido agregado promediadas.
print(' La relación señal ruido del promedio de las 10 señales con ruido es:',SNR_prom)



# Se crean 100 señales de ruido con media nula y desvío estandar igual a 3:

x_rand = list(range(0 ,100))    # Se genera el arreglo que contiene las 100 señales de ruido
x_suma    = list(range(0,100))  # Se genera el arreglo que contiene las 100 señales de ruido sumadas a la señal original
x_prom= 0 *np.array(range(0,22050))  # Promedio de todas las señales con ruido agregado

for i in range(0,100):
    x_rand[i] = np.array(np.random.normal(0,3,22050)) # Creación de señales de ruido con media nula y desvío 3
    x_suma[i] = x + x_rand[i]    # Suma de cada señal de ruido con la señal original
    if i<99:
        x_prom= x_prom + x_suma[i]   # Promediado de señales 
    else:
        x_prom= (x_prom + x_suma[i])/100
        
        
SNR_prom = np.max(x_prom)/3  # Relación señal ruido de las señales con ruido agregado promediadas.
print(' La relación señal ruido del promedio de las 100 señales con ruido es:',SNR_prom)

# Se crean 1000 señales de ruido con media nula y desvío estandar igual a 3:

x_rand = list(range(0 ,1000))    # Se genera el arreglo que contiene las 1000 señales de ruido
x_suma    = list(range(0,1000))  # Se genera el arreglo que contiene las 1000 señales de ruido sumadas a la señal original
x_prom= 0 *np.array(range(0,22050))  # Promedio de todas las señales con ruido agregado

for i in range(0,1000):
    x_rand[i] = np.array(np.random.normal(0,3,22050)) # Creación de señales de ruido con media nula y desvío 3
    x_suma[i] = x + x_rand[i]    # Suma de cada señal de ruido con la señal original
    if i<999:
        x_prom= x_prom + x_suma[i]   # Promediado de señales 
    else:
        x_prom= (x_prom + x_suma[i])/1000
        
        
SNR_prom = np.max(x_prom)/3  # Relación señal ruido de las señales con ruido agregado promediadas.
print(' La relación señal ruido del promedio de las 1000 señales con ruido es:',SNR_prom)