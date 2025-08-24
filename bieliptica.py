""""
bieliptica.py


Este script grafica la orbita inicial, final e intermedias para una 
transferencia bieliptica.

Modulos requeridos:
    - orbita_eliptica_foco: Genera los puntos de una órbita elíptica con un 
    foco en el origen (Tierra).

Autor: Eduardo Kunysz
Fecha: 14/10/24
"""

import numpy as np
import matplotlib.pyplot as plt
from orbital_func import *

# Constantes
G = 6.67430e-11      # Constante gravitacional (m^3 kg^-1 s^-2)
M_TIERRA = 5.972e24  # Masa de la Tierra (kg)
R_TIERRA = 6371e3    # Radio de la Tierra (m)
Rel_r_inicial_r_final = 20
Rel_r_intermedia = 10000
# Calculo de Parametro gravitacional
mu = G * M_TIERRA

# Parámetros de la órbita inicial circular
R_i = 7000e3   # Orbita Leo (m)

# Parámetros de la nueva órbita circular después de la transferencia
R_f = R_i * Rel_r_inicial_r_final  # Multiplicador

# Generar los puntos de la órbita inicial
x_orbita_i, y_orbita_i = orbita_eliptica_foco(R_i, R_i)

r_intermedia = R_i * Rel_r_intermedia

# Generar los puntos de la primer orbita de transferencia
x_orbita_t1, y_orbita_t1 = orbita_eliptica_foco(R_i, r_intermedia)

# Generar los puntos de la segunda orbita de transferencia
x_orbita_t2, y_orbita_t2 = orbita_eliptica_foco(R_f, r_intermedia)

# Generar los puntos de la orbita final
x_orbita_f, y_orbita_f = orbita_eliptica_foco(R_f, R_f)


# Calculo de semiejes mayores de las transferencias
at1 = (R_i + r_intermedia) / 2
at2 = (r_intermedia + R_f) / 2

# Velocidades en cda fse de la transferencia bieliptica
v1  = np.sqrt(mu / R_i)
v2  = np.sqrt(mu / R_f)
va  = np.sqrt(mu * (2 / R_i - 1 / at1))
v1b = np.sqrt(mu * (2 / r_intermedia - 1 / at1))
v2b = np.sqrt(mu * (2 / r_intermedia - 1 / at2))
vc  = np.sqrt(mu * (2 / R_f - 1 / at2))

# Calcular los cambios de velocidad
delta_v1 = va - v1           # Cambio en r_inicial
delta_v2 = v2b - v1b         # Cambio en r_intermedia
delta_v3 = v2 - vc           # Cambio en r_final

# Suma de todos los delta-v
delta_v_total = abs(delta_v1) + abs(delta_v2) + abs(delta_v3)

informe = f"""
Resultados de la transferencia Bi-eliptica:
-------------------------------------------
Radio inicial: {R_i / 1000} [Km]
Radio final:   {R_f / 1000} [Km]
R intermedio:  {r_intermedia / 1000} [Km]

Velocidad Inicial: {v1 / 1000 * 3600} [km/h]
Velocidad Escape inicial  : {va / 1000 * 3600} [km/h]
Velocidad Periapsis de la primera orbita de transferencia: {v1b / 1000 * 3600} [km/h]
Velocidad Escape primera orbita de transferencia: {v2b / 1000 * 3600} [km/h]
Velocidad Arribo Segunda orbita de transferencia: {vc / 1000 * 3600} [km/h]
Velocidad Orbita final: {v2 / 1000 * 3600} [km/h]

Delta-V
Delta-V1 = {delta_v1 / 1000 * 3600} [km/h]
Delta-V2 = {delta_v2 / 1000 * 3600} [km/h]
Delta-V3 = {delta_v3 / 1000 * 3600} [km/h]
Delta-Vtotal = {delta_v_total / 1000 * 3600} [km/h]
"""

# Imprimo el informe
print(informe)

# Graficar la órbita y los puntos de impulso
plt.figure(figsize=(20, 20))

# Dibujar la órbita inicial
plt.plot(x_orbita_i / 1e3, y_orbita_i / 1e3, linestyle='-', 
         label='Órbita inicial', color='blue')

# Dibujar la primer orbita de transferencia primera mitad continua, segunda punteada
plt.plot(x_orbita_t1[:500] / 1e3, y_orbita_t1[:500] / 1e3, linestyle='-', 
         label='1er orbita transferencia', color='green')
plt.plot(x_orbita_t1[500:] / 1e3, y_orbita_t1[500:] / 1e3, linestyle='--', 
        color='green')

# Dibujar la primer orbita de transferencia primera mitad continua, segunda punteada
plt.plot(x_orbita_t2[:500] / 1e3, y_orbita_t2[:500] / 1e3, linestyle='--', 
         label='2da orbita transferencia', color='red')
plt.plot(x_orbita_t2[500:] / 1e3, y_orbita_t2[500:] / 1e3, linestyle='-', 
        color='red')

# Dibujar la nueva órbita (después del impulso)
plt.plot(x_orbita_f / 1e3, y_orbita_f / 1e3, 
         label='Órbita final', linestyle='-', color='orange')

# Dibujar la Tierra (en el foco)
tierra = plt.Circle((0, 0), R_TIERRA / 1e3, color='blue', label='Tierra', 
                    alpha=0.5)
plt.gca().add_patch(tierra)

# Etiquetas y leyenda
plt.title('Órbita inicial y final (Transferencia Bi-eliptica)')
plt.xlabel('Distancia en X (km)')
plt.ylabel('Distancia en Y (km)')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()

# Mostrar la gráfica
plt.show()
