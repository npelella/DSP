"""
@author: Nicolas pelella, Paula Ortega Riera
"""

import numpy as np
import Funciones_1 as Fx

# Generar x(t)= 2 + sen(2πft), siendo f= 10
#kHz, que debe ser muestreada a Fs = 44.1 kHz y de duración 0.5 segundos
   
    
f=10000  # Frecuencia [Hz]
t=np.linspace(0,0.5,44100*0.5)              # Tiempo de duración [s]
x = 2 + np.sin(2*np.pi*f*t)        # Señal senoidal pedida

# Cálculo del Valor medio de la señal

print('El valor medio de la señal es:', Fx.valormedio(x))

# Cálculo del desvío medio de la señal

print('El desvío medio de la señal es:', Fx.desviomedio(x))

# Cálculo del desvío estándar de la señal

print ('El desvío estándar de la señal es:', Fx.desvioestandar(x))

# Cálculo del valor eficaz de la señal

print ('El valor eficaz de la señal es:', Fx.valoreficaz(x))

