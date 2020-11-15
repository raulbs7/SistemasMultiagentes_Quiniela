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

Clasificacion_Local = ctrl.Antecedent(np.arange(1, 20, 1), 'Clasificación Local')
Clasificacion_Visitante = ctrl.Antecedent(np.arange(1, 20, 1), 'Clasificación Visitante')
Result= ctrl.Consequent(np.arange(1,9,1), 'Result')

Presupuesto_Local = ctrl.Antecedent(np.arange(1, 950, 1), 'Presupuesto Local')
Presupuesto_Visitante = ctrl.Antecedent(np.arange(1, 950, 1), 'Presupuesto Visitante')

RachaG_Local = ctrl.Antecedent(np.arange(0, 38, 0), 'Racha ganando Local')
RachaG_Visitante = ctrl.Antecedent(np.arange(0, 38, 0), 'Racha ganando Visitante')

RachaE_Local = ctrl.Antecedent(np.arange(0, 38, 0), 'Racha empatando Local')
RachaE_Visitante = ctrl.Antecedent(np.arange(0, 38, 0), 'Racha empatando Visitante')

RachaP_Local = ctrl.Antecedent(np.arange(0, 38, 0), 'Racha perdiendo Local')
RachaP_Visitante = ctrl.Antecedent(np.arange(0, 38, 0), 'Racha perdiendo Visitante')

RachaNG_Local = ctrl.Antecedent(np.arange(0, 38, 0), 'Racha sin ganar  Local')
RachaNG_Visitante = ctrl.Antecedent(np.arange(0, 38, 0), 'Racha sin ganar Visitante')

RachaNE_Local = ctrl.Antecedent(np.arange(0, 38, 0), 'Racha sin empatar Local')
RachaNE_Visitante = ctrl.Antecedent(np.arange(0, 38, 0), 'Racha sin empatar Visitante')

RachaNP_Local = ctrl.Antecedent(np.arange(0, 38, 0), 'Racha sin perder Local')
RachaNP_Visitante = ctrl.Antecedent(np.arange(0, 38, 0), 'Racha sin perder Visitante')

#CREACIÓN AUTOMÁTICA DE LOS SOPORTES DE LAS ETIQUETAS

names = ['Muy Arriba', 'Arriba', 'Mitad', 'Abajo', 'Muy Abajo']

Clasificacion_Local['Muy_Arriba'] = Muy_Arriba
Clasificacion_Local['Arriba'] = Arriba
Clasificacion_Local['Mitad'] = Mitad
Clasificacion_Local['Abajo'] = Abajo
Clasificacion_Local['Muy_Abajo'] = Muy_Abajo

Clasificacion_Visitante['Muy_Arriba'] = Muy_Arriba
Clasificacion_Visitante['Arriba'] = Arriba
Clasificacion_Visitante['Mitad'] = Mitad
Clasificacion_Visitante['Abajo'] = Abajo
Clasificacion_Visitante['Muy_Abajo'] = Muy_Abajo

names2= ['1','X','2'] 

Result.automf(names=names2)

namesP = ['Presupuesto_Minimo', 'Presupuesto_Bajo', 'Presupuesto_Normal', 'Presupuesto_Alto', 'Presupuesto_Enorme'] 

Presupuesto_Local['Presupuesto_Minimo'] = Presupuesto_Minimo
Presupuesto_Local['Presupuesto_Bajo'] = Presupuesto_Bajo
Presupuesto_Local['Presupuesto_Normal'] = Presupuesto_Normal
Presupuesto_Local['Presupuesto_Alto'] = Presupuesto_Alto
Presupuesto_Local['Presupuesto_Enorme'] = Presupuesto_Enorme

Presupuesto_Visitante['Presupuesto_Minimo'] = Presupuesto_Minimo
Presupuesto_Visitante['Presupuesto_Bajo'] = Presupuesto_Bajo
Presupuesto_Visitante['Presupuesto_Normal'] = Presupuesto_Normal
Presupuesto_Visitante['Presupuesto_Alto'] = Presupuesto_Alto
Presupuesto_Visitante['Presupuesto_Enorme'] = Presupuesto_Enorme

namesRG= ['Racha_Ninguna', 'Racha_Corta', 'Racha_Normal', 'Racha_Buena', 'Racha_Enorme'] 

RachaG_Local['Racha_Ninguna'] = Racha_Ninguna
RachaG_Local['Racha_Corta'] = Racha_Corta
RachaG_Local['Racha_Normal'] = Racha_Normal
RachaG_Local['Racha_Buena'] = Racha_Buena
RachaG_Local['Racha_Enorme'] = Racha_Enorme

RachaG_Visitante['Racha_Ninguna'] = Racha_Ninguna
RachaG_Visitante['Racha_Corta'] = Racha_Corta
RachaG_Visitante['Racha_Normal'] = Racha_Normal
RachaG_Visitante['Racha_Buena'] = Racha_Buena
RachaG_Visitante['Racha_Enorme'] = Racha_Enorme


namesRE= ['Racha_Buena', 'Racha_Normal', 'Racha_Mala', 'Racha_Pesima'] 

RachaE_Local['Racha_Buena'] = Racha_Buena
RachaE_Local['Racha_Normal'] = Racha_Normal
RachaE_Local['Racha_Mala'] = Racha_Mala
RachaE_Local['Racha_Pesima'] = Racha_Pesima

RachaE_Visitante['Racha_Buena'] = Racha_Buena
RachaE_Visitante['Racha_Normal'] = Racha_Normal
RachaE_Visitante['Racha_Mala'] = Racha_Mala
RachaE_Visitante['Racha_Pesima'] = Racha_Pesima

namesRP= ['Racha_Buena', 'Racha_Normal', 'Racha_Mala', 'Racha_Pesima'] 

RachaP_Local['Racha_Buena'] = Racha_Buena
RachaP_Local['Racha_Normal'] = Racha_Normal
RachaP_Local['Racha_Mala'] = Racha_Mala
RachaP_Local['Racha_Pesima'] = Racha_Pesima

RachaP_Visitante['Racha_Buena'] = Racha_Buena
RachaP_Visitante['Racha_Normal'] = Racha_Normal
RachaP_Visitante['Racha_Mala'] = Racha_Mala
RachaP_Visitante['Racha_Pesima'] = Racha_Pesima


namesRNG= ['Racha_Buena', 'Racha_Normal', 'Racha_Mala', 'Racha_Pesima'] 

RachaNG_Local['Racha_Buena'] = Racha_Buena
RachaNG_Local['Racha_Normal'] = Racha_Normal
RachaNG_Local['Racha_Mala'] = Racha_Mala
RachaNG_Local['Racha_Pesima'] = Racha_Pesima

RachaNG_Visitante['Racha_Buena'] = Racha_Buena
RachaNG_Visitante['Racha_Normal'] = Racha_Normal
RachaNG_Visitante['Racha_Mala'] = Racha_Mala
RachaNG_Visitante['Racha_Pesima'] = Racha_Pesima

namesRNP= ['Racha_Ninguna', 'Racha_Corta', 'Racha_Normal', 'Racha_Buena', 'Racha_Enorme'] 

RachaNP_Local['Racha_Ninguna'] = Racha_Ninguna
RachaNP_Local['Racha_Corta'] = Racha_Corta
RachaNP_Local['Racha_Normal'] = Racha_Normal
RachaNP_Local['Racha_Buena'] = Racha_Buena
RachaNP_Local['Racha_Enorme'] = Racha_Enorme

RachaNP_Visitante['Racha_Ninguna'] = Racha_Ninguna
RachaNP_Visitante['Racha_Corta'] = Racha_Corta
RachaNP_Visitante['Racha_Normal'] = Racha_Normal
RachaNP_Visitante['Racha_Buena'] = Racha_Buena
RachaNP_Visitante['Racha_Enorme'] = Racha_Enorme

namesRNE= ['Racha_Ninguna', 'Racha_Corta', 'Racha_Normal', 'Racha_Buena', 'Racha_Enorme'] 

RachaNE_Local['Racha_Ninguna'] = Racha_Ninguna
RachaNE_Local['Racha_Corta'] = Racha_Corta
RachaNE_Local['Racha_Normal'] = Racha_Normal
RachaNE_Local['Racha_Buena'] = Racha_Buena
RachaNE_Local['Racha_Enorme'] = Racha_Enorme

RachaNE_Visitante['Racha_Ninguna'] = Racha_Ninguna
RachaNE_Visitante['Racha_Corta'] = Racha_Corta
RachaNE_Visitante['Racha_Normal'] = Racha_Normal
RachaNE_Visitante['Racha_Buena'] = Racha_Buena
RachaNE_Visitante['Racha_Enorme'] = Racha_Enorme



# Reglas

rule1 = ctrl.Rule(Clasificacion_Local['Muy_Arriba'] and Clasificacion_Visitante['Muy_Arriba'], Result['X'])
rule2 = ctrl.Rule(Clasificacion_Local['Muy_Arriba'] and Clasificacion_Visitante['Arriba'], Result['1'])
rule3 = ctrl.Rule(Clasificacion_Local['Muy_Arriba'] and Clasificacion_Visitante['Mitad'], Result['1'])
rule4 = ctrl.Rule(Clasificacion_Local['Muy_Arriba'] and Clasificacion_Visitante['Abajo'], Result['1'])
rule5 = ctrl.Rule(Clasificacion_Local['Muy_Arriba'] and Clasificacion_Visitante['Muy_Abajo'], Result['1'])
rule6 = ctrl.Rule(Clasificacion_Local['Arriba'] and Clasificacion_Visitante['Muy_Arriba'], Result['2'])
rule7 = ctrl.Rule(Clasificacion_Local['Arriba'] and Clasificacion_Visitante['Arriba'], Result['X'])
rule8 = ctrl.Rule(Clasificacion_Local['Arriba'] and Clasificacion_Visitante['Mitad'], Result['1'])
rule9 = ctrl.Rule(Clasificacion_Local['Arriba'] and Clasificacion_Visitante['Abajo'], Result['1'])
rule10 = ctrl.Rule(Clasificacion_Local['Arriba'] and Clasificacion_Visitante['Muy_Abajo'], Result['1'])
rule11 = ctrl.Rule(Clasificacion_Local['Mitad'] and Clasificacion_Visitante['Muy_Arriba'], Result['2'])
rule12 = ctrl.Rule(Clasificacion_Local['Mitad'] and Clasificacion_Visitante['Arriba'], Result['2'])
rule13 = ctrl.Rule(Clasificacion_Local['Mitad'] and Clasificacion_Visitante['Mitad'], Result['X'])
rule14 = ctrl.Rule(Clasificacion_Local['Mitad'] and Clasificacion_Visitante['Abajo'], Result['1'])
rule15 = ctrl.Rule(Clasificacion_Local['Mitad'] and Clasificacion_Visitante['Muy_Abajo'], Result['1'])
rule16 = ctrl.Rule(Clasificacion_Local['Abajo'] and Clasificacion_Visitante['Muy_Arriba'], Result['2'])
rule17 = ctrl.Rule(Clasificacion_Local['Abajo'] and Clasificacion_Visitante['Arriba'], Result['2'])
rule18 = ctrl.Rule(Clasificacion_Local['Abajo'] and Clasificacion_Visitante['Mitad'], Result['2'])
rule19 = ctrl.Rule(Clasificacion_Local['Abajo'] and Clasificacion_Visitante['Abajo'], Result['X'])
rule20 = ctrl.Rule(Clasificacion_Local['Abajo'] and Clasificacion_Visitante['Muy_Abajo'], Result['1'])
rule21 = ctrl.Rule(Clasificacion_Local['Muy_Abajo'] and Clasificacion_Visitante['Muy_Arriba'], Result['2'])
rule22 = ctrl.Rule(Clasificacion_Local['Muy_Abajo'] and Clasificacion_Visitante['Arriba'], Result['2'])
rule23 = ctrl.Rule(Clasificacion_Local['Muy_Abajo'] and Clasificacion_Visitante['Mitad'], Result['2'])
rule24 = ctrl.Rule(Clasificacion_Local['Muy_Abajo'] and Clasificacion_Visitante['Abajo'], Result['2'])
rule25 = ctrl.Rule(Clasificacion_Local['Muy_Abajo'] and Clasificacion_Visitante['Muy_Abajo'], Result['X'])

rule26 = ctrl.Rule(Presupuesto_Local['Presupuesto_Enorme'] and Presupuesto_Visitante['Presupuesto_Enorme'], Result['X'])
rule27 = ctrl.Rule(Presupuesto_Local['Presupuesto_Enorme'] and Presupuesto_Visitante['Presupuesto_Alto'], Result['1'])
rule28 = ctrl.Rule(Presupuesto_Local['Presupuesto_Enorme'] and Presupuesto_Visitante['Presupuesto_Normal'], Result['1'])
rule29 = ctrl.Rule(Presupuesto_Local['Presupuesto_Enorme'] and Presupuesto_Visitante['Presupuesto_Bajo'], Result['1'])
rule30 = ctrl.Rule(Presupuesto_Local['Presupuesto_Enorme'] and Presupuesto_Visitante['Presupuesto_Minimo'], Result['1'])
rule31 = ctrl.Rule(Presupuesto_Local['Presupuesto_Alto'] and Presupuesto_Visitante['Presupuesto_Enorme'], Result['2'])
rule32 = ctrl.Rule(Presupuesto_Local['Presupuesto_Alto'] and Presupuesto_Visitante['Presupuesto_Alto'], Result['X'])
rule33 = ctrl.Rule(Presupuesto_Local['Presupuesto_Alto'] and Presupuesto_Visitante['Presupuesto_Normal'], Result['1'])
rule34 = ctrl.Rule(Presupuesto_Local['Presupuesto_Alto'] and Presupuesto_Visitante['Presupuesto_Bajo'], Result['1'])
rule35 = ctrl.Rule(Presupuesto_Local['Presupuesto_Alto'] and Presupuesto_Visitante['Presupuesto_Minimo'], Result['1'])
rule36 = ctrl.Rule(Presupuesto_Local['Presupuesto_Normal'] and Presupuesto_Visitante['Presupuesto_Enorme'], Result['2'])
rule37 = ctrl.Rule(Presupuesto_Local['Presupuesto_Normal'] and Presupuesto_Visitante['Presupuesto_Alto'], Result['2'])
rule38 = ctrl.Rule(Presupuesto_Local['Presupuesto_Normal'] and Presupuesto_Visitante['Presupuesto_Normal'], Result['X'])
rule39 = ctrl.Rule(Presupuesto_Local['Presupuesto_Normal'] and Presupuesto_Visitante['Presupuesto_Bajo'], Result['1'])
rule40 = ctrl.Rule(Presupuesto_Local['Presupuesto_Normal'] and Presupuesto_Visitante['Presupuesto_Minimo'], Result['1'])
rule41 = ctrl.Rule(Presupuesto_Local['Presupuesto_Bajo'] and Presupuesto_Visitante['Presupuesto_Enorme'], Result['2'])
rule42 = ctrl.Rule(Presupuesto_Local['Presupuesto_Bajo'] and Presupuesto_Visitante['Presupuesto_Alto'], Result['2'])
rule43 = ctrl.Rule(Presupuesto_Local['Presupuesto_Bajo'] and Presupuesto_Visitante['Presupuesto_Normal'], Result['2'])
rule44 = ctrl.Rule(Presupuesto_Local['Presupuesto_Bajo'] and Presupuesto_Visitante['Presupuesto_Bajo'], Result['X'])
rule45 = ctrl.Rule(Presupuesto_Local['Presupuesto_Bajo'] and Presupuesto_Visitante['Presupuesto_Minimo'], Result['1'])
rule46 = ctrl.Rule(Presupuesto_Local['Presupuesto_Minimo'] and Presupuesto_Visitante['Presupuesto_Enorme'], Result['2'])
rule47 = ctrl.Rule(Presupuesto_Local['Presupuesto_Minimo'] and Presupuesto_Visitante['Presupuesto_Alto'], Result['2'])
rule48 = ctrl.Rule(Presupuesto_Local['Presupuesto_Minimo'] and Presupuesto_Visitante['Presupuesto_Normal'], Result['2'])
rule49 = ctrl.Rule(Presupuesto_Local['Presupuesto_Minimo'] and Presupuesto_Visitante['Presupuesto_Bajo'], Result['2'])
rule50 = ctrl.Rule(Presupuesto_Local['Presupuesto_Minimo'] and Presupuesto_Visitante['Presupuesto_Minimo'], Result['X'])

rule51 = ctrl.Rule(RachaG_Local['Enorme'] , Result['1'])
rule52 = ctrl.Rule(RachaG_Local['Buena'] , Result['1'])
rule53 = ctrl.Rule(RachaG_Visitante['Enorme'] , Result['2'])
rule54 = ctrl.Rule(RachaG_Visitante['Buena'] , Result['2'])
rule55 = ctrl.Rule(RachaE_Local['Buena'] , Result['X'])
rule56 = ctrl.Rule(RachaE_Local['Normal'] , Result['X'])
rule57 = ctrl.Rule(RachaE_Visitante['Buena'] , Result['X'])
rule58 = ctrl.Rule(RachaE_Visitante['Normal'] , Result['X'])
rule59 = ctrl.Rule(RachaP_Local['Mala'] , Result['2'])
rule60 = ctrl.Rule(RachaP_Local['Pesima'] , Result['2'])
rule61 = ctrl.Rule(RachaP_Visitante['Mala'] , Result['1'])
rule62 = ctrl.Rule(RachaP_Visitante['Pesimo'] , Result['1'])

#Setear ruleta
quiniela_ctrl = ctrl.ControlSystem([rule1, rule2, rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule2,rule3,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,rule26,rule27,rule28,rule29,rule30,rule31,rule32,rule33,rule34,rule35,rule36,rule37,rule38,rule39,rule40,rule41,rule42,rule43,rule44,rule45,rule46,rule47,rule48,rule49,rule50,rule51,rule52,rule53,rule54,rule55,rule56,rule57,rule58,rule59,rule60,rule61,rule62])

quiniela = ctrl.ControlSystemSimulation(quiniela_ctrl)

quiniela.input['Clasificación Local'] = 3
quiniela.input['Clasificación Visitante'] = 11
quiniela.input['Presupuesto Local'] = 703000
quiniela.input['Presupuesto Visitante'] = 50300
quiniela.input['RachaG Local'] = 5
quiniela.input['RachaG Visitante'] = 0
quiniela.input['RachaE Local'] = 0
quiniela.input['RachaG Visitante'] = 1
quiniela.input['RachaP Local'] = 0
quiniela.input['RachaP Visitante'] = 2
quiniela.input['RachaNG Local'] = 0
quiniela.input['RachaNG Visitante'] = 2
quiniela.input['RachaNE Local'] = 10
quiniela.input['RachaNE Visitante'] = 4
quiniela.input['RachaNP Local'] = 5
quiniela.input['RachaNP Visitante'] = 0


# Crunch the numbers
quiniela.compute()


#Simulación de la ruleta


