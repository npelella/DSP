"""
@author: Nicolas pelella, Paula Ortega Riera
"""

import statistics as stats
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi

# A continuación se define la función para calcular el valor medio de la señal:
            
def valormedio(x):
    sum=0
    for i in x:                # recorro el vector de muestras de la señal
        sum = sum + i           # sumatoria de muestras
    return sum/float(len(x)) # La función devuelve como resultado la sumatoria dividida la cantidad de muestras
        
# A continuación se define la función para calcular el desvío medio de la señal:
        
            
def desviomedio(x):       # recorro el vector de muestras de la señal
    sum = 0
    for i in x:
        sum += i         # sumatoria de muestras
    media = sum /len(x)    # Divide la sumatoria por la cantidad de muestras
    total = 0               
    for i in x:
        total += (i - media) # calcula el desvío de la media calculada anteriormente
    desviacion = (total /len(x)) # divide por la longitud del vector de muestras
    return desviacion      # La función devuelve el desvío medio

# A continuación se define la función para calcular el desvío estándard de la señal:
    
def desvioestandar(x):
    sum = 0
    for i in x:
        sum += i         # sumatoria de muestras
    media = sum /len(x)    # Divide la sumatoria por la cantidad de muestras
    total = 0               
    for i in x:
        total += (i - media)**2             # calcula el desvío de la media calculada anteriormente elevado al cuadrado
    desviacion = (total / (len(x)-1)) ** 0.5        # divide por la longitud del vector de muestras y calcula la raíz
    return desviacion                               # La función devuelve el desvío medio
    

# A continuación se define la función para calcular el valor eficaz de la señal:
    
def valoreficaz(x):
    sum = 0
    for i in x:
        sum += i         # sumatoria de muestras
    cuadrado= (sum)**2    # elevo la sumatoria al cuadrado
    valoreficaz= (cuadrado/(len(x)))**0.5 #  Aplico raíz cudadrada a la sumatoria dividida la cantidad de muestras    
    return valoreficaz                               # La función devuelve el valor eficaz de la señal

