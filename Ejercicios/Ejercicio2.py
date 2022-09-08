"""
@author: Nicolas pelella, Paula Ortega Riera
"""

import numpy as np
import Funciones_1 as Fx

# creo una funcion que me genere una señal con media 0 y desvio estandar 1 para distinta cantidad de muestras

def funcion_normal(n):
    mu, sigma = 0, 1 # media y desvio estandar
    valores = np.random.normal(mu, sigma, n) #creando muestra de datos
    x = Fx.desvioestandar(valores) # llamo a la funcion de Funciones_1.py
    dif_porcentual = 100 - (x*100)
    
    return print('Para n =',n, 'el desvio estandar de la señal es:',Fx.desvioestandar(valores), 'y la diferencia porcentual es de:', dif_porcentual, '%' )

# hago la cuenta para distintos n
    
n=[5,10,100,1000,10000,100000]
m=[]
for i in n:
    m=funcion_normal(i)
    
    