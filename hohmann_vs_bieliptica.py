""""
hohmann_vs_bieliptica.py


Este script grafica la relacion de Hohmann para distintas relaciones de 
orbitas.

Modulos requeridos:
    - delta_v_hohmann: Calcula el delta-v total para una transferencia de 
      Hohmann.
    - delta_v_bieliptica: Calcula los delta-v totales de una trnasferencia bieliptica

Autor: Eduardo Kunysz
Fecha: 20/09/24
"""


import numpy as np
import matplotlib.pyplot as plt
from orbital_func import *

# Constantes
G = 6.67430e-11  # Constante gravitacional (m^3 kg^-1 s^-2)
M_TIERRA = 5.972e24  # Masa de la Tierra (kg)
R_TIERRA = 6371e3  # Radio de la Tierra (m)

R_inicial = np.linspace(7000e3, 44000e3)
R_final = np.linspace(44000e3, 1000005)

# Valores de R (relación entre radios final e inicial)
R = np.logspace(0, 2, 1000)  # Genera valores de R en escala logarítmica

# Calculo de Parametro gravitacional
MU = G * M_TIERRA
# Calcular delta-v para cada valor de R
delta_v_hohmann_values = delta_v_hohmann(R, 1, MU)     # Suponiendo r_inicial = 1
delta_v_bielipt_values = delta_v_bieliptica(R, 1, MU)  # Suponiendo r_inicial = 1

# Calcular la velocidad circular inicial
Vcl = np.sqrt(MU / 1)  # Asumiendo r_inicial = 1

# Normalizo el delta-v
delta_v_hohmann_norm = delta_v_hohmann_values / Vcl
delta_v_bielipt_norm = delta_v_bielipt_values / Vcl


## Crear la gráfica
plt.semilogx(R, delta_v_hohmann_norm, label='Hohmann', color='b')  # Usar semilogx para una escala logarítmica en el eje x
plt.semilogx(R, delta_v_bielipt_norm, label='Bieliptica', color='r')  # Usar semilogx para una escala logarítmica en el eje x
plt.xlabel('R = R_final / R_inicial (escala logarítmica)')
plt.ylabel('Delta-v / Vcl')
plt.title('Transferencia de Hohmann vs Bieliptica: Delta-v vs. R')
plt.legend()
plt.grid(True)
plt.show()
