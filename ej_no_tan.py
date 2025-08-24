""""
ej_no_tan.py


Este script resuelve el ejercicio 6.3 del libro de Vallado.

Modulos requeridos:
    - delta_v_one_tangent_burn: Calcula el delta-v total para una maniobra 
    no tangencial.

Autor: Eduardo Kunysz
Fecha: 16/10/24
"""

import math as op
import matplotlib.pyplot as plt
import orbital_func as astro

# Defino valores iniciales del ejercicio

altitud_inicial = 191.34411e3
altitud_final = 35781.34857e3
nu_trans_b = 160

# Constantes
G = 6.67430e-11      # Constante gravitacional (m^3 kg^-1 s^-2)
M_TIERRA = 5.972e24  # Masa de la Tierra (kg)
R_TIERRA = 6371e3    # Radio de la Tierra (m)

# Calculo de Parametro gravitacional
mu = G * M_TIERRA

r_i = (altitud_inicial + R_TIERRA) 
r_f = (altitud_final + R_TIERRA) 

Delta_v = astro.delta_v_one_tangent_burn(r_f, r_i, mu, nu_trans_b)

print(Delta_v)