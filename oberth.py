""""
oberth.py


Este script calcula y grafica la energía cinética de una nave espacial en una 
órbita elíptica alrededor de la Tierra antes y después de un impulso, mostrando 
tanto la energía cinética como el cambio en energía debido al impulso a lo 
largo de diferentes distancias en la órbita.

Modulos requeridos:
    - velocidad_orbital: Calcula la velocidad orbital en un punto de la órbita 
    elíptica.
    - energia_cinetica: Calcula la energía cinética de una nave en función de 
    su velocidad.

Autor: Eduardo Kunysz
Fecha: 17/09/24
"""

import numpy as np
import matplotlib.pyplot as plt
from orbital_func import *

# Constantes
G = 6.67430e-11      # Constante gravitacional (m^3 kg^-1 s^-2)
M_tierra = 5.972e24  # Masa de la Tierra (kg)
R_tierra = 6371e3    # Radio de la Tierra (m)
m_nave = 1000        # Masa de la nave (kg)

# Parámetros de la órbita
R_p = 7000e3   # Distancia del periapsis (m)
R_a = 42164e3  # Distancia del apoapsis (m)
delta_v = 1e3  # Impulso en m/s

# Semi-eje mayor de la órbita
a = (R_p + R_a) / 2

# Puntos de la órbita (entre periapsis y apoapsis)
distancias = np.linspace(R_p, R_a, 1000)
velocidades = velocidad_orbital(distancias, G, a, M_tierra)

# Energías cinéticas antes del impulso
energias_cineticas_iniciales = energia_cinetica(velocidades, m_nave)

# Energías cinéticas después del impulso
velocidades_con_impulso = velocidades + delta_v
energias_cineticas_finales = energia_cinetica(velocidades_con_impulso, m_nave)

# Cambio en la energía cinética
delta_energia_cinetica = energias_cineticas_finales - energias_cineticas_iniciales

# Graficar la órbita elíptica
plt.figure(figsize=(10, 5))

# Subplot 1: Gráfico de energía cinética antes y después del impulso
plt.subplot(1, 2, 1)
plt.plot(distancias / 1e3, energias_cineticas_iniciales / 1e6, label='Antes del impulso')
plt.plot(distancias / 1e3, energias_cineticas_finales / 1e6, label='Después del impulso', linestyle='--')
plt.xlabel('Distancia desde el centro de la Tierra (km)')
plt.ylabel('Energía cinética (MJ)')
plt.title('Energía cinética antes y después del impulso')
plt.legend()

# Subplot 2: Cambio en la energía cinética
plt.subplot(1, 2, 2)
plt.plot(distancias / 1e3, delta_energia_cinetica / 1e6, color='r')
plt.xlabel('Distancia desde el centro de la Tierra (km)')
plt.ylabel('Cambio en la Energía cinética (MJ)')
plt.title('Cambio en la energía cinética después del impulso')

# Mostrar las gráficas
plt.tight_layout()
plt.show()
