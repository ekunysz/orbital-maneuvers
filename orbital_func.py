"""
orbital_func
============


Esta librería contiene funciones para generar puntos de orbitas elipticas, 
velocidad orbital y energia cinetica.

Funciones incluidas
-------------------
-orbita_eliptica_foco
    Genera los puntos de una órbita elíptica con un foco en el origen (Tierra)
-velocidad_orbital
    Calcula la velocidad orbital en un punto de la órbita elíptica.
-energia_cinetica
    Calcula la energía cinética de una nave en función de su velocidad.
-delta_v_hohmann
    Calcula los delta-v totales de una transferencia de hohmann
-delta_v_bieliptica
    Calcula los delta-v totales de una trnasferencia bieliptica

Changelog: 
---------
|Fecha      | Autor |   Descripción
+-----------+-------+---------------------------------------------------------
|14/10/24   |   EK  |   Se agrega la función delta_v_bieliptica
|17/09/24   |   EK  |   Versión inicial de la librería

Autor: Eduardo Kunysz

Fecha: 14/10/24
"""

import numpy as np
import math as op

def orbita_eliptica_foco(R_p, R_a, num_puntos=1000):
    """
    Genera los puntos de una órbita elíptica con un foco en el origen (Tierra).

    Esta función calcula los puntos de una órbita elíptica basándose en las 
    distancias del periapsis y apoapsis, y asume que el foco de la elipse está 
    en el origen. La órbita se describe en coordenadas cartesianas (x, y).

    Parámetros:
    -----------
    R_p : float
        Distancia del periapsis (el punto más cercano al cuerpo central) en 
        metros.
    R_a : float
        Distancia del apoapsis (el punto más lejano del cuerpo central) en 
        metros.
    num_puntos : int, opcional
        Número de puntos que definen la órbita (por defecto 1000).

    Retorna:
    --------
    x_orbita : numpy.ndarray
        Coordenadas x de la órbita en metros.
    y_orbita : numpy.ndarray
        Coordenadas y de la órbita en metros.

    Notas:
    ------
    - El foco de la órbita elíptica, que representa la posición de la Tierra, 
      se encuentra en el origen (0,0).
    - El semi-eje mayor y el semi-eje menor se calculan usando las distancias 
      del periapsis y apoapsis.
    - Los puntos generados describen una órbita completa (0 a 360 grados) en 
      un plano 2D.

    Ejemplo:
    --------
    >>> x_orbita, y_orbita = orbita_eliptica_foco(7000e3, 42164e3)
    >>> plt.plot(x_orbita, y_orbita)
    >>> plt.show()
    """
    
    a = (R_p + R_a) / 2  # Semi-eje mayor
    c = a - R_p  # Distancia desde el centro de la elipse al foco (Tierra)
    b = np.sqrt(a**2 - c**2)  # Semi-eje menor
    theta = np.linspace(0, 2 * np.pi, num_puntos)
    x_orbita = a * np.cos(theta) - c  # Ajustar la elipse para que el foco esté en el origen
    y_orbita = b * np.sin(theta)
    
    return x_orbita, y_orbita


def velocidad_orbital(r, G, a, M_tierra):
    """
    Calcula la velocidad orbital en un punto de la órbita elíptica.

    Parámetros:
    ----------
    r : float
        La distancia radial desde el centro de la Tierra al punto en la órbita 
        (en metros).
    G: float
        Constante gravitatoria (en m^3 kg^-1 s^-2)
    a: float
        Semieje mayor (en m)
    M_tierra: float
        Masa de la tierra (en Kg)

    Retorna:
    -------
    float
        La velocidad orbital en ese punto (en metros por segundo).

    Fórmula utilizada:
    v = sqrt(G * M_tierra * (2 / r - 1 / a))
    """
    return np.sqrt(G * M_tierra * (2 / r - 1 / a))


def energia_cinetica(v, m_nave):
    """
    Calcula la energía cinética de una nave en función de su velocidad.

    Parámetros:
    ----------
    v : float
        Velocidad de la nave (en metros por segundo).
    m_nave : float
        Masa de la nave (en Kg)

    Retorna:
    -------
    float
        Energía cinética de la nave (en julios).

    Fórmula utilizada:
    E_k = 0.5 * m_nave * v**2
    """
    return 0.5 * m_nave * v**2

def delta_v_hohmann(r_final: float, r_inicial: float, mu: float):
    """
    Calcula el delta-v total para una transferencia de Hohmann.

    Parámetros:
    ----------
    r_final: float
        Radio de la órbita final.
    r_inicial: float
        Radio de la órbita inicial.
    mu: float
        Parámetro gravitacional (km^3/s^2)

    Retorna:
    --------
        Delta-v total en km/s.
    """
    a = (r_inicial + r_final) / 2
    v1 = np.sqrt(mu / r_inicial)
    v2 = np.sqrt(mu / r_final)
    va = np.sqrt(mu * (2 / r_inicial - 1 / a))
    vb = np.sqrt(mu * (2 / r_final - 1 / a))
    delta_v = abs(va - v1) + abs(v2 - vb)
    return delta_v

def delta_v_bieliptica(r_final: float, r_inicial: float, mu: float):
    """
    Calcula el delta-v total para una transferencia bieliptica.

    Parámetros:
    ----------
    r_final: float
        Radio de la órbita final.
    r_inicial: float
        Radio de la órbita inicial.
    mu: float
        Parámetro gravitacional (km^3/s^2)

    Retorna:
    --------
        Delta-v total en km/s.

    Nota:
    -----
        El valor de la r para la orbita intermedia se calcula de forma fija
        por ahora un valor grande
    """
    # Valor de r_intermedio tendiendo a infinito (caso teorico optimo)
    r_intermedia = r_final * 1000 
    
    # Calculo de semiejes mayores de las transferencias
    at1 = (r_inicial + r_intermedia) / 2
    at2 = (r_intermedia + r_final) / 2
    
    # Velocidades en cda fse de la transferencia bieliptica
    v1  = np.sqrt(mu / r_inicial)
    v2  = np.sqrt(mu / r_final)
    va  = np.sqrt(mu * (2 / r_inicial - 1 / at1))
    v1b = np.sqrt(mu * (2 / r_intermedia - 1 / at1))
    v2b = np.sqrt(mu * (2 / r_intermedia - 1 / at2))
    vc  = np.sqrt(mu * (2 / r_final - 1 / at2))
    
    # Calcular los cambios de velocidad
    delta_v1 = abs(va - v1)           # Cambio en r_inicial
    delta_v2 = abs(v2b - v1b)         # Cambio en r_intermedia
    delta_v3 = abs(v2 - vc)           # Cambio en r_final

    # Suma de todos los delta-v
    delta_v_total = delta_v1 + delta_v2 + delta_v3
    return delta_v_total

def delta_v_one_tangent_burn(r_final: float, r_inicial: float, mu: float, nu: float):
    """
    Calcula el delta-v total para una maniobra no tangencial.

    Parámetros:
    ----------
    r_final: float
        Radio de la órbita final.
    r_inicial: float
        Radio de la órbita inicial.
    mu: float
        Parámetro gravitacional (km^3/s^2)
    nu: float
        Anomalía verdadera (grados)

    Retorna:
    --------
        Delta-v total en km/s.

    """

    #Relacion inversa de r_final /r_inicial (uso Q en lugar de R^-1)
    Q = r_inicial / r_final    
  
    # Calculo de excentricidad

    e_trans = (Q - 1) / (op.cos(op.radians(nu)) - Q)
    # Calculo de semiejes mayores de las transferencias
    a_trans = r_inicial / (1 - e_trans)
  
    # Velocidades en cada fase circular 
    v_i = op.sqrt(mu / r_inicial)
    v_f = op.sqrt(mu / r_final)

    # Velocidad en cada etapa de transferencia
    v_trans_a  = op.sqrt(mu * (2 / r_inicial - 1 / a_trans))
    v_trans_b  = op.sqrt(mu * (2 / r_final - 1 / a_trans))
    
    # Calcular de Delta-Va
    delta_va = v_trans_a - v_i        # Cambio en r_inicial
    
    # Calculo de Fligth Path Angle
    tan_fi = e_trans * op.sin(op.radians(nu)) / (1 + e_trans * op.cos(op.radians(nu)))
    fi_fpa = op.degrees(op.atan(tan_fi))
    
    # Calculo de Delta-Vb
    delta_vb = op.sqrt(v_f ** + v_trans_b ** - 2 * v_f * v_trans_b * 
                       op.cos(op.radians(fi_fpa)))

    # Suma de todos los delta-v
    delta_v_total = abs(delta_va) + abs(delta_vb)
    return delta_v_total

