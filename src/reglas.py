import sys

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

# Se tiene que definir un dominio para cada uno de las etiquetas lingüísticas.

Rango_Equipos = np.arange(1, 20, 1)
Rango_Presupuestos = np.arange(1, 950, 1) # Los presupuestos estan representados en millones
Rango_Rachas = np.arange(0, 38, 1)

# A continuación se define manualmente el soporte de cada un de las etiquetas, en este caso trapezoidales.

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

# ANTECEDENTES Y CONSECUENTES DE LAS REGLAS

Clasificacion_Local = ctrl.Antecedent(Rango_Equipos, 'Clasificacion_Local')
Clasificacion_Visitante = ctrl.Antecedent(Rango_Equipos, 'Clasificacion_Visitante')

Presupuesto_Local = ctrl.Antecedent(Rango_Presupuestos, 'Presupuesto_Local')
Presupuesto_Visitante = ctrl.Antecedent(Rango_Presupuestos, 'Presupuesto_Visitante')

RachaG_Local = ctrl.Antecedent(Rango_Rachas, 'RachaG_Local')
RachaG_Visitante = ctrl.Antecedent(Rango_Rachas, 'RachaG_Visitante')

RachaE_Local = ctrl.Antecedent(Rango_Rachas, 'RachaE_Local')
RachaE_Visitante = ctrl.Antecedent(Rango_Rachas, 'RachaE_Visitante')

RachaP_Local = ctrl.Antecedent(Rango_Rachas, 'RachaP_Local')
RachaP_Visitante = ctrl.Antecedent(Rango_Rachas, 'RachaP_Visitante')

RachaNG_Local = ctrl.Antecedent(Rango_Rachas, 'RachaNG_Local')
RachaNG_Visitante = ctrl.Antecedent(Rango_Rachas, 'RachaNG_Visitante')

RachaNP_Local = ctrl.Antecedent(Rango_Rachas, 'RachaNP_Local')
RachaNP_Visitante = ctrl.Antecedent(Rango_Rachas, 'RachaNP_Visitante')

Result = ctrl.Consequent(np.arange(1, 9, 1), 'Result')

# CREACIÓN DE LOS SOPORTES DE LAS ETIQUETAS

names_result = ['1', 'X', '2']

Result.automf(names=names_result)

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

Presupuesto_Local['Presupuesto_Minimo'] = Minimo_Presupuesto
Presupuesto_Local['Presupuesto_Bajo'] = Bajo_Presupuesto
Presupuesto_Local['Presupuesto_Normal'] = Normal_Presupuesto
Presupuesto_Local['Presupuesto_Alto'] = Alto_Presupuesto
Presupuesto_Local['Presupuesto_Enorme'] = Enorme_Presupuesto

Presupuesto_Visitante['Presupuesto_Minimo'] = Minimo_Presupuesto
Presupuesto_Visitante['Presupuesto_Bajo'] = Bajo_Presupuesto
Presupuesto_Visitante['Presupuesto_Normal'] = Normal_Presupuesto
Presupuesto_Visitante['Presupuesto_Alto'] = Alto_Presupuesto
Presupuesto_Visitante['Presupuesto_Enorme'] = Enorme_Presupuesto

namesRG = ['Racha_Ninguna', 'Racha_Corta', 'Racha_Normal', 'Racha_Buena', 'Racha_Enorme']

RachaG_Local['Racha_Ninguna'] = No_Racha_Ganando
RachaG_Local['Racha_Corta'] = Corta_Racha_Ganando
RachaG_Local['Racha_Normal'] = Normal_Racha_Ganando
RachaG_Local['Racha_Buena'] = Buena_Racha_Ganando
RachaG_Local['Racha_Enorme'] = Enorme_Racha_Ganando

RachaG_Visitante['Racha_Ninguna'] = No_Racha_Ganando
RachaG_Visitante['Racha_Corta'] = Corta_Racha_Ganando
RachaG_Visitante['Racha_Normal'] = Normal_Racha_Ganando
RachaG_Visitante['Racha_Buena'] = Buena_Racha_Ganando
RachaG_Visitante['Racha_Enorme'] = Enorme_Racha_Ganando

namesRE = ['Racha_Buena', 'Racha_Normal', 'Racha_Mala', 'Racha_Pesima']

RachaE_Local['Racha_Buena'] = Buena_Racha_Empatando
RachaE_Local['Racha_Normal'] = Normal_Racha_Empatando
RachaE_Local['Racha_Mala'] = Mala_Racha_Empatando
RachaE_Local['Racha_Pesima'] = Pesima_Racha_Empatando

RachaE_Visitante['Racha_Buena'] = Buena_Racha_Empatando
RachaE_Visitante['Racha_Normal'] = Normal_Racha_Empatando
RachaE_Visitante['Racha_Mala'] = Mala_Racha_Empatando
RachaE_Visitante['Racha_Pesima'] = Pesima_Racha_Empatando

namesRP = ['Racha_Buena', 'Racha_Normal', 'Racha_Mala', 'Racha_Pesima']

RachaP_Local['Racha_Buena'] = Buena_Racha_Perdiendo
RachaP_Local['Racha_Normal'] = Normal_Racha_Perdiendo
RachaP_Local['Racha_Mala'] = Mala_Racha_Perdiendo
RachaP_Local['Racha_Pesima'] = Pesima_Racha_Perdiendo

RachaP_Visitante['Racha_Buena'] = Buena_Racha_Perdiendo
RachaP_Visitante['Racha_Normal'] = Normal_Racha_Perdiendo
RachaP_Visitante['Racha_Mala'] = Mala_Racha_Perdiendo
RachaP_Visitante['Racha_Pesima'] = Pesima_Racha_Perdiendo

namesRNG = ['Racha_Buena', 'Racha_Normal', 'Racha_Mala', 'Racha_Pesima']

RachaNG_Local['Racha_Buena'] = Buena_Racha_Sin_Ganar
RachaNG_Local['Racha_Normal'] = Normal_Racha_Sin_Ganar
RachaNG_Local['Racha_Mala'] = Mala_Racha_Sin_Ganar
RachaNG_Local['Racha_Pesima'] = Pesima_Racha_Sin_Ganar

RachaNG_Visitante['Racha_Buena'] = Buena_Racha_Sin_Ganar
RachaNG_Visitante['Racha_Normal'] = Normal_Racha_Sin_Ganar
RachaNG_Visitante['Racha_Mala'] = Mala_Racha_Sin_Ganar
RachaNG_Visitante['Racha_Pesima'] = Pesima_Racha_Sin_Ganar

namesRNP = ['Racha_Ninguna', 'Racha_Corta', 'Racha_Normal', 'Racha_Buena', 'Racha_Enorme']

RachaNP_Local['Racha_Ninguna'] = No_Racha_Sin_Perder
RachaNP_Local['Racha_Corta'] = Corta_Racha_Sin_Perder
RachaNP_Local['Racha_Normal'] = Normal_Racha_Sin_Perder
RachaNP_Local['Racha_Buena'] = Buena_Racha_Sin_Perder
RachaNP_Local['Racha_Enorme'] = Enorme_Racha_Sin_Perder

RachaNP_Visitante['Racha_Ninguna'] = No_Racha_Sin_Perder
RachaNP_Visitante['Racha_Corta'] = Corta_Racha_Sin_Perder
RachaNP_Visitante['Racha_Normal'] = Normal_Racha_Sin_Perder
RachaNP_Visitante['Racha_Buena'] = Buena_Racha_Sin_Perder
RachaNP_Visitante['Racha_Enorme'] = Enorme_Racha_Sin_Perder

# REGLAS

rule1 = ctrl.Rule(Clasificacion_Local['Muy_Arriba'] & Clasificacion_Visitante['Muy_Arriba'], Result['X'])
rule2 = ctrl.Rule(Clasificacion_Local['Muy_Arriba'] & Clasificacion_Visitante['Arriba'], Result['1'])
rule3 = ctrl.Rule(Clasificacion_Local['Muy_Arriba'] & Clasificacion_Visitante['Mitad'], Result['1'])
rule4 = ctrl.Rule(Clasificacion_Local['Muy_Arriba'] & Clasificacion_Visitante['Abajo'], Result['1'])
rule5 = ctrl.Rule(Clasificacion_Local['Muy_Arriba'] & Clasificacion_Visitante['Muy_Abajo'], Result['1'])
rule6 = ctrl.Rule(Clasificacion_Local['Arriba'] & Clasificacion_Visitante['Muy_Arriba'], Result['2'])
rule7 = ctrl.Rule(Clasificacion_Local['Arriba'] & Clasificacion_Visitante['Arriba'], Result['X'])
rule8 = ctrl.Rule(Clasificacion_Local['Arriba'] & Clasificacion_Visitante['Mitad'], Result['1'])
rule9 = ctrl.Rule(Clasificacion_Local['Arriba'] & Clasificacion_Visitante['Abajo'], Result['1'])
rule10 = ctrl.Rule(Clasificacion_Local['Arriba'] & Clasificacion_Visitante['Muy_Abajo'], Result['1'])
rule11 = ctrl.Rule(Clasificacion_Local['Mitad'] & Clasificacion_Visitante['Muy_Arriba'], Result['2'])
rule12 = ctrl.Rule(Clasificacion_Local['Mitad'] & Clasificacion_Visitante['Arriba'], Result['2'])
rule13 = ctrl.Rule(Clasificacion_Local['Mitad'] & Clasificacion_Visitante['Mitad'], Result['X'])
rule14 = ctrl.Rule(Clasificacion_Local['Mitad'] & Clasificacion_Visitante['Abajo'], Result['1'])
rule15 = ctrl.Rule(Clasificacion_Local['Mitad'] & Clasificacion_Visitante['Muy_Abajo'], Result['1'])
rule16 = ctrl.Rule(Clasificacion_Local['Abajo'] & Clasificacion_Visitante['Muy_Arriba'], Result['2'])
rule17 = ctrl.Rule(Clasificacion_Local['Abajo'] & Clasificacion_Visitante['Arriba'], Result['2'])
rule18 = ctrl.Rule(Clasificacion_Local['Abajo'] & Clasificacion_Visitante['Mitad'], Result['2'])
rule19 = ctrl.Rule(Clasificacion_Local['Abajo'] & Clasificacion_Visitante['Abajo'], Result['X'])
rule20 = ctrl.Rule(Clasificacion_Local['Abajo'] & Clasificacion_Visitante['Muy_Abajo'], Result['1'])
rule21 = ctrl.Rule(Clasificacion_Local['Muy_Abajo'] & Clasificacion_Visitante['Muy_Arriba'], Result['2'])
rule22 = ctrl.Rule(Clasificacion_Local['Muy_Abajo'] & Clasificacion_Visitante['Arriba'], Result['2'])
rule23 = ctrl.Rule(Clasificacion_Local['Muy_Abajo'] & Clasificacion_Visitante['Mitad'], Result['2'])
rule24 = ctrl.Rule(Clasificacion_Local['Muy_Abajo'] & Clasificacion_Visitante['Abajo'], Result['2'])
rule25 = ctrl.Rule(Clasificacion_Local['Muy_Abajo'] & Clasificacion_Visitante['Muy_Abajo'], Result['X'])

rule26 = ctrl.Rule(Presupuesto_Local['Presupuesto_Enorme'] & Presupuesto_Visitante['Presupuesto_Enorme'], Result['X'])
rule27 = ctrl.Rule(Presupuesto_Local['Presupuesto_Enorme'] & Presupuesto_Visitante['Presupuesto_Alto'], Result['1'])
rule28 = ctrl.Rule(Presupuesto_Local['Presupuesto_Enorme'] & Presupuesto_Visitante['Presupuesto_Normal'], Result['1'])
rule29 = ctrl.Rule(Presupuesto_Local['Presupuesto_Enorme'] & Presupuesto_Visitante['Presupuesto_Bajo'], Result['1'])
rule30 = ctrl.Rule(Presupuesto_Local['Presupuesto_Enorme'] & Presupuesto_Visitante['Presupuesto_Minimo'], Result['1'])
rule31 = ctrl.Rule(Presupuesto_Local['Presupuesto_Alto'] & Presupuesto_Visitante['Presupuesto_Enorme'], Result['2'])
rule32 = ctrl.Rule(Presupuesto_Local['Presupuesto_Alto'] & Presupuesto_Visitante['Presupuesto_Alto'], Result['X'])
rule33 = ctrl.Rule(Presupuesto_Local['Presupuesto_Alto'] & Presupuesto_Visitante['Presupuesto_Normal'], Result['1'])
rule34 = ctrl.Rule(Presupuesto_Local['Presupuesto_Alto'] & Presupuesto_Visitante['Presupuesto_Bajo'], Result['1'])
rule35 = ctrl.Rule(Presupuesto_Local['Presupuesto_Alto'] & Presupuesto_Visitante['Presupuesto_Minimo'], Result['1'])
rule36 = ctrl.Rule(Presupuesto_Local['Presupuesto_Normal'] & Presupuesto_Visitante['Presupuesto_Enorme'], Result['2'])
rule37 = ctrl.Rule(Presupuesto_Local['Presupuesto_Normal'] & Presupuesto_Visitante['Presupuesto_Alto'], Result['2'])
rule38 = ctrl.Rule(Presupuesto_Local['Presupuesto_Normal'] & Presupuesto_Visitante['Presupuesto_Normal'], Result['X'])
rule39 = ctrl.Rule(Presupuesto_Local['Presupuesto_Normal'] & Presupuesto_Visitante['Presupuesto_Bajo'], Result['1'])
rule40 = ctrl.Rule(Presupuesto_Local['Presupuesto_Normal'] & Presupuesto_Visitante['Presupuesto_Minimo'], Result['1'])
rule41 = ctrl.Rule(Presupuesto_Local['Presupuesto_Bajo'] & Presupuesto_Visitante['Presupuesto_Enorme'], Result['2'])
rule42 = ctrl.Rule(Presupuesto_Local['Presupuesto_Bajo'] & Presupuesto_Visitante['Presupuesto_Alto'], Result['2'])
rule43 = ctrl.Rule(Presupuesto_Local['Presupuesto_Bajo'] & Presupuesto_Visitante['Presupuesto_Normal'], Result['2'])
rule44 = ctrl.Rule(Presupuesto_Local['Presupuesto_Bajo'] & Presupuesto_Visitante['Presupuesto_Bajo'], Result['X'])
rule45 = ctrl.Rule(Presupuesto_Local['Presupuesto_Bajo'] & Presupuesto_Visitante['Presupuesto_Minimo'], Result['1'])
rule46 = ctrl.Rule(Presupuesto_Local['Presupuesto_Minimo'] & Presupuesto_Visitante['Presupuesto_Enorme'], Result['2'])
rule47 = ctrl.Rule(Presupuesto_Local['Presupuesto_Minimo'] & Presupuesto_Visitante['Presupuesto_Alto'], Result['2'])
rule48 = ctrl.Rule(Presupuesto_Local['Presupuesto_Minimo'] & Presupuesto_Visitante['Presupuesto_Normal'], Result['2'])
rule49 = ctrl.Rule(Presupuesto_Local['Presupuesto_Minimo'] & Presupuesto_Visitante['Presupuesto_Bajo'], Result['2'])
rule50 = ctrl.Rule(Presupuesto_Local['Presupuesto_Minimo'] & Presupuesto_Visitante['Presupuesto_Minimo'], Result['X'])

rule51 = ctrl.Rule(RachaG_Local['Racha_Enorme'], Result['1'])
rule52 = ctrl.Rule(RachaG_Local['Racha_Buena'], Result['1'])
rule53 = ctrl.Rule(RachaG_Visitante['Racha_Enorme'], Result['2'])
rule54 = ctrl.Rule(RachaG_Visitante['Racha_Buena'], Result['2'])
rule55 = ctrl.Rule(RachaE_Local['Racha_Buena'], Result['X'])
rule56 = ctrl.Rule(RachaE_Local['Racha_Normal'], Result['X'])
rule57 = ctrl.Rule(RachaE_Visitante['Racha_Buena'], Result['X'])
rule58 = ctrl.Rule(RachaE_Visitante['Racha_Normal'], Result['X'])
rule59 = ctrl.Rule(RachaP_Local['Racha_Mala'], Result['2'])
rule60 = ctrl.Rule(RachaP_Local['Racha_Pesima'], Result['2'])
rule61 = ctrl.Rule(RachaP_Visitante['Racha_Mala'], Result['1'])
rule62 = ctrl.Rule(RachaP_Visitante['Racha_Pesima'], Result['1'])
rule63 = ctrl.Rule(RachaNG_Local['Racha_Mala'], Result['2'])
rule64 = ctrl.Rule(RachaNG_Local['Racha_Pesima'], Result['2'])
rule65 = ctrl.Rule(RachaNG_Visitante['Racha_Mala'], Result['1'])
rule66 = ctrl.Rule(RachaNG_Visitante['Racha_Pesima'], Result['1'])
rule67 = ctrl.Rule(RachaNP_Local['Racha_Enorme'], Result['1'])
rule68 = ctrl.Rule(RachaNP_Local['Racha_Buena'], Result['1'])
rule69 = ctrl.Rule(RachaNP_Visitante['Racha_Enorme'], Result['2'])
rule70 = ctrl.Rule(RachaNP_Visitante['Racha_Buena'], Result['2'])

# METEMOS INPUTS
quiniela_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
                                    rule11, rule2, rule3, rule14, rule15, rule16, rule17, rule18, rule19, rule20,
                                    rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30,
                                    rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40,
                                    rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50,
                                    rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60,
                                    rule61, rule62, rule63, rule64, rule65, rule66, rule67, rule68, rule69, rule70])


quiniela = ctrl.ControlSystemSimulation(quiniela_ctrl)

def sis_quiniela():
    return quiniela

def consequent():
    return Result

def main():
    # MOSTRANDO VARIABLES DIFUSAS LO CUAL SE EJECUTARA SOLO DESDE ESTE MODULO

    fig0, (ax0) = plt.subplots(nrows=1, figsize=(8, 9))
    fig1, (ax1) = plt.subplots(nrows=1, figsize=(8, 9))
    fig2, (ax2) = plt.subplots(nrows=1, figsize=(8, 9))
    fig3, (ax3) = plt.subplots(nrows=1, figsize=(8, 9))
    fig4, (ax4) = plt.subplots(nrows=1, figsize=(8, 9))
    fig5, (ax5) = plt.subplots(nrows=1, figsize=(8, 9))
    fig6, (ax6) = plt.subplots(nrows=1, figsize=(8, 9))

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

    ax2.plot(Rango_Rachas, No_Racha_Ganando, 'b', linewidth=1.5, label='Sin racha')
    ax2.plot(Rango_Rachas, Corta_Racha_Ganando, 'g', linewidth=1.5, label='Racha corta')
    ax2.plot(Rango_Rachas, Normal_Racha_Ganando, 'r', linewidth=1.5, label='Racha normal')
    ax2.plot(Rango_Rachas, Buena_Racha_Ganando, 'y', linewidth=1.5, label='Racha buena')
    ax2.plot(Rango_Rachas, Enorme_Racha_Ganando, 'c', linewidth=1.5, label='Racha enorme')

    ax3.plot(Rango_Rachas, Buena_Racha_Perdiendo, 'b', linewidth=1.5, label='Buena racha')
    ax3.plot(Rango_Rachas, Normal_Racha_Perdiendo, 'g', linewidth=1.5, label='Racha normal')
    ax3.plot(Rango_Rachas, Mala_Racha_Perdiendo, 'r', linewidth=1.5, label='Racha mala')
    ax3.plot(Rango_Rachas, Pesima_Racha_Perdiendo, 'y', linewidth=1.5, label='Racha pesima')

    ax4.plot(Rango_Rachas, Buena_Racha_Empatando, 'b', linewidth=1.5, label='Buena racha')
    ax4.plot(Rango_Rachas, Normal_Racha_Empatando, 'g', linewidth=1.5, label='Racha normal')
    ax4.plot(Rango_Rachas, Mala_Racha_Empatando, 'r', linewidth=1.5, label='Racha mala')
    ax4.plot(Rango_Rachas, Pesima_Racha_Empatando, 'y', linewidth=1.5, label='Racha pesima')

    ax5.plot(Rango_Rachas, Buena_Racha_Sin_Ganar, 'b', linewidth=1.5, label='Buena racha')
    ax5.plot(Rango_Rachas, Normal_Racha_Sin_Ganar, 'g', linewidth=1.5, label='Racha normal')
    ax5.plot(Rango_Rachas, Mala_Racha_Sin_Ganar, 'r', linewidth=1.5, label='Racha mala')
    ax5.plot(Rango_Rachas, Pesima_Racha_Sin_Ganar, 'y', linewidth=1.5, label='Racha pesima')

    ax6.plot(Rango_Rachas, No_Racha_Sin_Perder, 'b', linewidth=1.5, label='Sin racha')
    ax6.plot(Rango_Rachas, Corta_Racha_Sin_Perder, 'g', linewidth=1.5, label='Racha corta')
    ax6.plot(Rango_Rachas, Normal_Racha_Sin_Perder, 'r', linewidth=1.5, label='Racha normal')
    ax6.plot(Rango_Rachas, Buena_Racha_Sin_Perder, 'y', linewidth=1.5, label='Racha buena')
    ax6.plot(Rango_Rachas, Enorme_Racha_Sin_Perder, 'c', linewidth=1.5, label='Racha enorme')

    ax0.set_title('Clasificación')
    ax0.legend()

    ax1.set_title('Presupuesto')
    ax1.legend()

    ax2.set_title('Racha Ganando')
    ax2.legend()

    ax3.set_title('Racha Perdiendo')
    ax3.legend()

    ax4.set_title('Racha Empatando')
    ax4.legend()

    ax5.set_title('Racha Sin Ganar')
    ax5.legend()

    ax6.set_title('Racha Sin Perder')
    ax6.legend()

    fig0.show()
    #fig0.savefig('clasificacion.png')
    fig1.show()
    #fig1.savefig('presupuesto.png')
    fig2.show()
    #fig2.savefig('racha_ganando.png')
    fig3.show()
    #fig3.savefig('racha_perdiendo.png')
    fig4.show()
    #fig4.savefig('racha_empatando.png')
    fig5.show()
    #fig5.savefig('racha_sin_ganar.png')
    fig6.show()
    #fig6.savefig('racha_sin_perder.png')

    quiniela.input['Clasificacion_Local'] = 3
    quiniela.input['Clasificacion_Visitante'] = 11
    quiniela.input['Presupuesto_Local'] = 500
    quiniela.input['Presupuesto_Visitante'] = 503
    quiniela.input['RachaG_Local'] = 5
    quiniela.input['RachaG_Visitante'] = 0
    quiniela.input['RachaE_Local'] = 0
    quiniela.input['RachaE_Visitante'] = 1
    quiniela.input['RachaP_Local'] = 0
    quiniela.input['RachaP_Visitante'] = 2
    quiniela.input['RachaNG_Local'] = 1
    quiniela.input['RachaNG_Visitante'] = 2
    quiniela.input['RachaNP_Local'] = 5
    quiniela.input['RachaNP_Visitante'] = 0

    # COMPUTAMOS PARA DETERMINAR NUESTRA SALIDA
    quiniela.compute()

    # CALCULAMOS EL GRADO DE PERTENENCIA A CADA RESULTADO DEL PARTIDO
    range_result = np.arange(1, 9, 1)

    val = quiniela.output['Result']
    variable = Result['1']

    Pertenencia1 = fuzz.interp_membership(range_result, variable.mf, val)

    print(Pertenencia1)

    val = quiniela.output['Result']
    variable = Result['X']

    PertenenciaX = fuzz.interp_membership(range_result, variable.mf, val)

    print(PertenenciaX)

    val = quiniela.output['Result']
    variable = Result['2']

    Pertenencia2 = fuzz.interp_membership(range_result, variable.mf, val)

    print(Pertenencia2)

if __name__ == '__main__':
    sys.exit(main())