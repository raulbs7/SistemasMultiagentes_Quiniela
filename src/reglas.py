import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

#Se tiene que definir un dominio para cada uno de las etiquetas lingüísticas.

Rango_Equipos  = np.arange(1, 20, 1)
Rango_Presupuestos = np.arange (1,950,1)
Rango_Rachas = np.arange (0,38,1)

#A continuación se define manualmente el soporte de cada un de las etiquetas, en este caso trapezoidales.

Muy_Arriba = fuzz.trapmf(Rango_Equipos, [1, 1, 3, 5])
Arriba = fuzz.trapmf(Rango_Equipos, [3, 5, 7, 9])
Mitad = fuzz.trapmf(Rango_Equipos, [7, 9, 11, 13])
Abajo = fuzz.trapmf(Rango_Equipos, [11, 13, 15, 17])
Muy_Abajo = fuzz.trapmf(Rango_Equipos, [15, 17, 20, 20])


Minimo_Presupuesto = fuzz.trapmf(Rango_Presupuestos, [1, 1, 10, 20])
Bajo_Presupuesto = fuzz.trapmf(Rango_Presupuestos, [10, 30, 50, 70])
Normal_Presupuesto = fuzz.trapmf(Rango_Presupuestos, [50, 80, 110, 140])
Alto_Presupuesto = fuzz.trapmf(Rango_Presupuestos, [100, 200, 400, 500])
Enorme_Presupuesto = fuzz.trapmf(Rango_Presupuestos, [400, 700, 950, 950])

No_Racha_Ganando = fuzz.trimf(Rango_Rachas, [0, 0, 3])
Corta_Racha_Ganando = fuzz.trapmf(Rango_Rachas, [2, 3, 4, 5])
Normal_Racha_Ganando = fuzz.trapmf(Rango_Rachas, [3, 4, 5, 6])
Buena_Racha_Ganando = fuzz.trapmf(Rango_Rachas, [5, 7, 9, 11])
Enorme_Racha_Ganando = fuzz.trapmf(Rango_Rachas, [7, 18, 38, 38])

Buena_Racha_Perdiendo = fuzz.trimf(Rango_Rachas, [0, 0, 3])
Normal_Racha_Perdiendo = fuzz.trapmf(Rango_Rachas, [2, 4, 6, 8])
Mala_Racha_Perdiendo = fuzz.trapmf(Rango_Rachas, [6, 8, 10, 12])
Pesima_Racha_Perdiendo = fuzz.trapmf(Rango_Rachas, [8, 15, 38, 38])

Buena_Racha_Empatando = fuzz.trimf(Rango_Rachas, [0, 0, 4])
Normal_Racha_Empatando = fuzz.trapmf(Rango_Rachas, [3, 5, 7, 9])
Mala_Racha_Empatando = fuzz.trapmf(Rango_Rachas, [6, 8, 10, 12])
Pesima_Racha_Empatando = fuzz.trapmf(Rango_Rachas, [8, 15, 38, 38])

Buena_Racha_Sin_Ganar = fuzz.trimf(Rango_Rachas, [0, 0, 3])
Normal_Racha_Sin_Ganar = fuzz.trapmf(Rango_Rachas, [2, 4, 6, 8])
Mala_Racha_Sin_Ganar = fuzz.trapmf(Rango_Rachas, [5, 7, 9, 11])
Pesima_Racha_Sin_Ganar = fuzz.trapmf(Rango_Rachas, [8, 12, 38, 38])

No_Racha_Sin_Perder = fuzz.trimf(Rango_Rachas, [0, 0, 3])
Corta_Racha_Sin_Perder = fuzz.trapmf(Rango_Rachas, [2, 3, 4, 5])
Normal_Racha_Sin_Perder = fuzz.trapmf(Rango_Rachas, [3, 4, 5, 6])
Buena_Racha_Sin_Perder = fuzz.trapmf(Rango_Rachas, [5, 7, 9, 11])
Enorme_Racha_Sin_Perder = fuzz.trapmf(Rango_Rachas, [7, 18, 38, 38])

fig0, (ax0) = plt.subplots(nrows=1, figsize=(8, 9))
fig1, (ax1) = plt.subplots(nrows=1, figsize=(8, 9))
#fig, (ax2) = plt.subplots(nrows=1, figsize=(8, 9))

ax0.plot(Rango_Equipos, Muy_Arriba, 'b', linewidth=1.5, label='Muy Arriba')
ax0.plot(Rango_Equipos, Arriba, 'g', linewidth=1.5, label='Arriba')
ax0.plot(Rango_Equipos, Mitad, 'r', linewidth=1.5, label='Mitad')
ax0.plot(Rango_Equipos, Abajo, 'y', linewidth=1.5, label='Abajo')
ax0.plot(Rango_Equipos, Muy_Abajo, 'c', linewidth=1.5, label='Muy Abajo')


ax1.plot(Rango_Presupuestos, Minimo_Presupuesto, 'b', linewidth=1.5, label='Presupuesto Minimo')
ax1.plot(Rango_Presupuestos, Bajo_Presupuesto, 'g', linewidth=1.5, label='Presupuesto Bajo')
ax1.plot(Rango_Presupuestos, Normal_Presupuesto, 'r', linewidth=1.5, label='Presupuesto Normal')
ax1.plot(Rango_Presupuestos, Alto_Presupuesto, 'y', linewidth=1.5, label='Presupuesto Alto')
ax1.plot(Rango_Presupuestos, Enorme_Presupuesto, 'c', linewidth=1.5, label='Presupuesto Enorme')


#ax2.plot(Rango_rachas, No_Racha, 'b', linewidth=1.5, label='Sin racha')
#ax2.plot(Rango_rachas, Corta_Racha, 'b', linewidth=1.5, label='Racha corta')
#ax2.plot(Rango_rachas, Decente_Racha, 'b', linewidth=1.5, label='Racha decente')
#ax2.plot(Rango_rachas, Grande_Racha, 'b', linewidth=1.5, label='Racha grande')
#ax2.plot(Rango_rachas, Enorme_Racha, 'b', linewidth=1.5, label='Racha enorme')

ax0.set_title('Clasificación')
ax0.legend()

ax1.set_title('Presupuesto')
ax1.legend()

fig0.show()
fig1.show()
#ax2.set_title('Racha')
#ax2.legend()

# ANTECEDENTES Y CONSECUENTES DE LAS REGLAS



#CREACIÓN AUTOMÁTICA DE LOS SOPORTES DE LAS ETIQUETAS



# Crunch the numbers


#Simulación de la ruleta

