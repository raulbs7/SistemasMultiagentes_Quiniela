import operator
import random
import sys

from src import extractor as extr
from src import reglas
import numpy as np
import skfuzzy as fuzz
from operator import itemgetter

class Simulador:

    def __init__(self):
        try:
            self.clasificacion = extr.get_clasificacion()
            self.rachas = extr.get_rachas()
            self.presupuestos = extr.get_presupuestos()
            self.sistema_quiniela = reglas.sis_quiniela()
        except Exception as error:
            raise ValueError(f'Cannot init dictionary: {error}')

    def simular(self, local_clasificacion, local_rachas, local_presupuestos, visitante_clasificacion, visitante_rachas, visitante_presupuestos):
        try:
            clasificacion_local = self.clasificacion[local_clasificacion]['posicion']
        except KeyError as error:
            raise KeyError(f'No se puede obtener la clasificación del equipo local: {error}')
        try:
            clasificacion_visitante = self.clasificacion[visitante_clasificacion]['posicion']
        except KeyError as error:
            raise KeyError(f'No se puede obtener la clasificación del equipo visitante: {error}')
        try:
            presupuesto_local = self.presupuestos[local_presupuestos]
        except KeyError as error:
            raise KeyError(f'No se puede obtener el presupuesto del equipo local: {error}')
        try:
            presupuesto_visitante = self.presupuestos[visitante_presupuestos]
        except KeyError as error:
            raise KeyError(f'No se puede obtener el presupuesto del equipo visitante: {error}')
        try:
            if local_rachas in self.rachas['ganando'].keys():
                rachaG_local = self.rachas['ganando'][local_rachas]
            else:
                rachaG_local = 0
            if visitante_rachas in self.rachas['ganando'].keys():
                rachaG_visitante = self.rachas['ganando'][visitante_rachas]
            else:
                rachaG_visitante = 0
        except KeyError as error:
            raise KeyError(f'No se pueden obtener las rachas de partidos ganados: {error}')
        try:
            if local_rachas in self.rachas['perdiendo'].keys():
                rachaP_local = self.rachas['perdiendo'][local_rachas]
            else:
                rachaP_local = 0
            if visitante_rachas in self.rachas['perdiendo'].keys():
                rachaP_visitante = self.rachas['perdiendo'][visitante_rachas]
            else:
                rachaP_visitante = 0
        except KeyError as error:
            raise KeyError(f'No se pueden obtener las rachas de partidos perdidos: {error}')
        try:
            if local_rachas in self.rachas['empatando'].keys():
                rachaE_local = self.rachas['empatando'][local_rachas]
            else:
                rachaE_local = 0
            if visitante_rachas in self.rachas['empatando'].keys():
                rachaE_visitante = self.rachas['empatando'][visitante_rachas]
            else:
                rachaE_visitante = 0
        except KeyError as error:
            raise KeyError(f'No se pueden obtener las rachas de partidos empatados: {error}')
        try:
            if local_rachas in self.rachas['sin_ganar'].keys():
                rachaNG_local = self.rachas['sin_ganar'][local_rachas]
            else:
                rachaNG_local = 0
            if visitante_rachas in self.rachas['sin_ganar'].keys():
                rachaNG_visitante = self.rachas['sin_ganar'][visitante_rachas]
            else:
                rachaNG_visitante = 0
        except KeyError as error:
            raise KeyError(f'No se pueden obtener las rachas de partidos sin ganar: {error}')
        try:
            if local_rachas in self.rachas['sin_perder'].keys():
                rachaNP_local = self.rachas['sin_perder'][local_rachas]
            else:
                rachaNP_local = 0
            if visitante_rachas in self.rachas['sin_perder'].keys():
                rachaNP_visitante = self.rachas['sin_perder'][visitante_rachas]
            else:
                rachaNP_visitante = 0
        except KeyError as error:
            raise KeyError(f'No se pueden obtener las rachas de partidos sin ganar: {error}')
        self.sistema_quiniela.input['Clasificacion_Local'] = clasificacion_local
        self.sistema_quiniela.input['Clasificacion_Visitante'] = clasificacion_visitante
        self.sistema_quiniela.input['Presupuesto_Local'] = (presupuesto_local / 1000000)
        self.sistema_quiniela.input['Presupuesto_Visitante'] = (presupuesto_visitante / 1000000)
        self.sistema_quiniela.input['RachaG_Local'] = rachaG_local
        self.sistema_quiniela.input['RachaG_Visitante'] = rachaG_visitante
        self.sistema_quiniela.input['RachaE_Local'] = rachaE_local
        self.sistema_quiniela.input['RachaE_Visitante'] = rachaE_visitante
        self.sistema_quiniela.input['RachaP_Local'] = rachaP_local
        self.sistema_quiniela.input['RachaP_Visitante'] = rachaP_visitante
        self.sistema_quiniela.input['RachaNG_Local'] = rachaNG_local
        self.sistema_quiniela.input['RachaNG_Visitante'] = rachaNG_visitante
        self.sistema_quiniela.input['RachaNP_Local'] = rachaNP_local
        self.sistema_quiniela.input['RachaNP_Visitante'] = rachaNP_visitante

        self.sistema_quiniela.compute()
        reglas.consequent().view(sim=self.sistema_quiniela)
        range_result = np.arange(1, 9, 1)

        val = self.sistema_quiniela.output['Result']
        variable = reglas.consequent()['1']
        Pertenencia1 = fuzz.interp_membership(range_result, variable.mf, val)

        val = self.sistema_quiniela.output['Result']
        variable = reglas.consequent()['X']
        PertenenciaX = fuzz.interp_membership(range_result, variable.mf, val)

        val = self.sistema_quiniela.output['Result']
        variable = reglas.consequent()['2']
        Pertenencia2 = fuzz.interp_membership(range_result, variable.mf, val)

        return ruleta(Pertenencia1, PertenenciaX, Pertenencia2)

def ruleta(pertenencia1, pertenenciaX, pertenencia2):

    pertenencias = {'pertenencia1': pertenencia1+0.1,
                    'pertenenciaX': pertenenciaX+0.1,
                    'pertenencia2': pertenencia2+0.1}
    pertenencias_ord = sorted(pertenencias.items(), key=operator.itemgetter(1))

    prob_num = random.uniform(0, 1.1)

    if prob_num <= pertenencias_ord[0][1]:
        return pertenencias_ord[0][0]
    if prob_num <= pertenencias_ord[1][1]:
        return pertenencias_ord[1][0]
    if prob_num <= pertenencias_ord[2][1]:
        return pertenencias_ord[2][0]

def main():
    sim = Simulador()
    pertenencias1 = sim.simular('ELCHE', 'ELCHE', 'ELCHE','HUESCA','HUESCA', 'HUESCA')
    print(pertenencias1)
    sim2 = Simulador()
    pertenencias2 = sim2.simular('VALENCIA', 'VALENCIA', 'VALENCIA', 'VILLARREAL', 'VILLARREAL', 'VILLARREAL')
    print(pertenencias2)

if __name__ == '__main__':
    sys.exit(main())

