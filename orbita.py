""""
orbita.py


Este script grafica dos orbitas alrededor de la tierra y describe el resultado
de un cierto impulso y transferencia a otra orbita.

Modulos requeridos:
    - orbita_eliptica_foco: Genera los puntos de una órbita elíptica con un 
    foco en el origen (Tierra).

Autor: Eduardo Kunysz
Fecha: 17/09/24
"""

import numpy as np
import matplotlib.pyplot as plt
from orbital_func import *

# Constantes
G = 6.67430e-11      # Constante gravitacional (m^3 kg^-1 s^-2)
M_TIERRA = 5.972e24  # Masa de la Tierra (kg)
R_TIERRA = 6371e3    # Radio de la Tierra (m)

# Parámetros de la órbita inicial
R_p = 7000e3   # Distancia del periapsis (m)
R_a = 42164e3  # Distancia del apoapsis (m)

# Parámetros de la nueva órbita después del impulso
R_p_nueva = 8000e3   # Supongamos que el periapsis aumentó
R_a_nueva = 50000e3  # Supongamos que el apoapsis también cambió

# Generar los puntos de la órbita inicial
x_orbita, y_orbita = orbita_eliptica_foco(R_p, R_a)

# Generar los puntos de la nueva órbita
x_orbita_nueva, y_orbita_nueva = orbita_eliptica_foco(R_p_nueva, R_a_nueva)

# Puntos importantes en la órbita
periapsis = (R_p, 0)  # Periapsis correcto
apoapsis = (-R_a, 0)  # Apoapsis correcto

# Puntos para comenzar y terminar el impulso
# Ajustamos el impulso para que empiece en -5° y termine en 5°
theta_inicio = np.deg2rad(-5)  # Ángulo del inicio del impulso
theta_fin = np.deg2rad(5)      # Ángulo del fin del impulso

# Calcular los puntos en la órbita para el inicio y fin del impulso
x_inicio = (R_p + R_a) / 2 * np.cos(theta_inicio) - (R_p + R_a) / 2 + R_p
y_inicio = np.sqrt(R_p * R_a) * np.sin(theta_inicio)

x_fin = (R_p + R_a) / 2 * np.cos(theta_fin) - (R_p + R_a) / 2 + R_p
y_fin = np.sqrt(R_p * R_a) * np.sin(theta_fin)

# Graficar la órbita y los puntos de impulso
plt.figure(figsize=(6, 6))

# Dibujar la órbita inicial
plt.plot(x_orbita / 1e3, y_orbita / 1e3, label='Órbita inicial', color='blue')

# Dibujar la nueva órbita (después del impulso)
plt.plot(x_orbita_nueva / 1e3, y_orbita_nueva / 1e3, 
         label='Órbita después del impulso', linestyle='--', color='orange')

# Dibujar la Tierra (en el foco)
tierra = plt.Circle((0, 0), R_TIERRA / 1e3, color='blue', label='Tierra', 
                    alpha=0.5)
plt.gca().add_patch(tierra)

# Marcar el periapsis y apoapsis
plt.scatter([periapsis[0] / 1e3, apoapsis[0] / 1e3], 
            [periapsis[1] / 1e3, apoapsis[1] / 1e3], 
            color='red', zorder=5, label='Periapsis/Apoapsis')

# Marcar el inicio y fin del impulso
plt.scatter([x_inicio / 1e3, x_fin / 1e3], [y_inicio / 1e3, y_fin / 1e3], 
            color='green', zorder=5, label='Inicio/Fin del impulso')

# Etiquetas y leyenda
plt.title('Órbita inicial y después del impulso (Efecto Oberth)')
plt.xlabel('Distancia en X (km)')
plt.ylabel('Distancia en Y (km)')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()

# Mostrar la gráfica
plt.show()
