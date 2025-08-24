""""
no_tangencial.py


Este script grafica la orbita inicial, final e intermedias para una 
transferencia no tangencial.

Modulos requeridos:
    - orbita_eliptica_foco: Genera los puntos de una órbita elíptica con un 
    foco en el origen (Tierra).

Autor: Eduardo Kunysz
Fecha: 14/10/24
"""

import numpy as np
import sys
import math as op
import matplotlib.pyplot as plt
import orbital_func as astro

# Constantes
G = 6.67430e-11      # Constante gravitacional (m^3 kg^-1 s^-2)
M_TIERRA = 5.972e24  # Masa de la Tierra (kg)
R_TIERRA = 6371e3    # Radio de la Tierra (m)
Rel_r_inicial_r_final = 10
nu = 145
# Calculo de Parametro gravitacional
mu = G * M_TIERRA

# Parámetros de la órbita inicial circular
R_i = 7000e3   # Orbita Leo (m)

# Parámetros de la nueva órbita circular después de la transferencia
R_f = R_i * Rel_r_inicial_r_final  # Multiplicador

# Generar los puntos de la órbita inicial
x_orbita_i, y_orbita_i = astro.orbita_eliptica_foco(R_i, R_i)



# Generar los puntos de la orbita de transferencia
# x_orbita_t1, y_orbita_t1 = orbita_eliptica_foco(R_i, r_intermedia)

# Generar los puntos de la orbita final
x_orbita_f, y_orbita_f = astro.orbita_eliptica_foco(R_f, R_f)


#Relacion inversa de r_final /r_inicial (uso Q en lugar de R^-1)
Q = R_i / R_f    


# Valores limites de nu para distintos Q
nu_inf = op.degrees(op.acos(2 * Q - 1))
excent_min = (Q - 1) / (-1 - Q) 
nu_sup = op.degrees(op.acos((Q * (1 + excent_min) -1) / excent_min))

if nu > nu_sup:
    print ("nu debe ser menos a ", nu_sup)
    sys.exit()
elif nu < nu_inf:
    print ("nu debe ser mayor a ", nu_inf)
    sys.exit()


# Calculo de excentricidad
e_trans = (Q - 1) / (op.cos(op.radians(nu)) - Q)

# Calculo de semiejes mayores de las transferencias
a_trans = R_i / (1 - e_trans)

#Calculo de r apoappsis de orbita trans

r_a = (a_trans * (1 - e_trans ** 2)) / (1 - e_trans)
# Generar los puntos de la orbita de transferencia
x_orbita_t1, y_orbita_t1 = astro.orbita_eliptica_foco(R_i, r_a)


# Velocidades en cada fase circular 
v_i = op.sqrt(mu / R_i)
v_f = op.sqrt(mu / R_f)

# Velocidad en cada etapa de transferencia
v_trans_a  = op.sqrt(mu * (2 / R_i - 1 / a_trans))
v_trans_b  = op.sqrt(mu * (2 / R_f - 1 / a_trans))

# Calcular de Delta-Va
delta_va = v_trans_a - v_i        # Cambio en r_inicial

# Calculo de Fligth Path Angle
tan_fi = e_trans * op.sin(op.radians(nu)) / (1 + e_trans * op.cos(op.radians(nu)))
fi_fpa = op.degrees(op.atan(tan_fi))

# Calculo de Delta-Vb
delta_vb = op.sqrt(v_f ** 2 + v_trans_b ** 2 - 2 * v_f * v_trans_b * 
                    op.cos(op.radians(fi_fpa)))

# Suma de todos los delta-v
delta_v_total = abs(delta_va) + abs(delta_vb)

informe = f"""
Resultados de la transferencia No Tangencial:
-------------------------------------------
Radio inicial: {R_i / 1000} [Km]
Radio final:   {R_f / 1000} [Km]
excentricidad: {e_trans}
Anomalia Verdadera Nu:  {nu} [grados]

Velocidad Inicial: {v_i / 1000 * 3600} [km/h]
Velocidad Escape inicial  : {v_trans_a / 1000 * 3600} [km/h]
Flight Path Angle : {fi_fpa} [grados]

Delta-V
Delta-V1 = {delta_va / 1000 * 3600} [km/h]
Delta-V2 = {delta_vb / 1000 * 3600} [km/h]
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

# Dibujar la nueva órbita (después del impulso)
plt.plot(x_orbita_f / 1e3, y_orbita_f / 1e3, 
         label='Órbita final', linestyle='-', color='orange')

# Dibujar la Tierra (en el foco)
tierra = plt.Circle((0, 0), R_TIERRA / 1e3, color='blue', label='Tierra', 
                    alpha=0.5)
plt.gca().add_patch(tierra)

# Etiquetas y leyenda
plt.title('Órbita inicial y final (Transferencia No Tangencial)')
plt.xlabel('Distancia en X (km)')
plt.ylabel('Distancia en Y (km)')
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()

# Mostrar la gráfica
plt.show()
