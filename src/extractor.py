# -*- coding: utf-8 -*-

import re
import sys
import urllib.request
from pprint import pprint

import requests
from bs4 import BeautifulSoup

#******************************************************************
#------- Inicialización de variables y métodos auxiliares ---------
#******************************************************************

URL_CLASIFICACION = 'https://www.eduardolosilla.es/quiniela/ayudas/clasificacion'

URL_RACHAS = 'https://www.eduardolosilla.es/quiniela/ayudas/rachas'

URL_PRESUPUESTOS = 'https://www.resultados-futbol.com/primera/grupo1/equipos'

TIPOS_RACHAS = [['ganando', 'empatando', 'perdiendo'],
                ['sin_ganar', 'sin_empatar', 'sin_perder']]

# Compilamos los patrones para un numero y para el nombre de un equipo
NUM = re.compile(r'\d+')
NOMBRE = re.compile(r'[\w\.]+[\w\. ]*')

#Función para reemplazar tildes
def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ç", "celon"), #Esta regla de reemplazo esta hecha  únicamente para el F.C Barcelona
        ("Á", "A"),
        ("É", "E"),
        ("Í", "I"),
        ("Ó", "O"),
        ("Ú", "U"),
        ("Ç", "CELON")
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

#*****************************************************
#--------- Métodos utilizables de la clase -----------
#*****************************************************

def get_clasificacion():
    # La clasificacion la representamos como diccionario
    clasificacion = {}
    html_page = requests.get(URL_CLASIFICACION)
    soup = BeautifulSoup(html_page.content, features='html.parser')
    # Buscamos la tabla html de la clasificacion
    tabla = soup.find('table', {'class': 'c-clasificacion__tabla ng-star-inserted'})
    for fila in tabla.tbody:
        if (fila.name is not None) and ('c-clasificacion__tabla__categoria' in fila['class']):
            # Recogemos de cada fila todas las columnas
            columnas = fila.find_all('td')
            posicion = int(NUM.match(columnas[0].text).group(0))
            equipo = normalize(NOMBRE.search(columnas[1].text).group(0)).upper()
            puntos = int(NUM.match(columnas[2].text).group(0))
            ganados = int(NUM.match(columnas[4].text).group(0))
            empatados = int(NUM.match(columnas[5].text).group(0))
            perdidos = int(NUM.match(columnas[6].text).group(0))
            golesFavor = int(NUM.match(columnas[7].text).group(0))
            golesContra = int(NUM.match(columnas[8].text).group(0))
            clasificacion[equipo] = {'posicion': posicion,
                                     'puntos': puntos,
                                     'p_ganados': ganados,
                                     'p_empatados': empatados,
                                     'p_perdidos': perdidos,
                                     'golesFavor': golesFavor,
                                     'golesContra': golesContra}

    return clasificacion

def get_presupuestos():
    # El presupuesto de cada equipo lo representamos como diccionario
    presupuestos = {}
    #Utilizamos la libreria urllib para obtener un html decodificado en utf-8 debido a los
    #problemas que surgen con otras librerías al no detectar ciertos caracteres
    html_page = urllib.request.urlopen(URL_PRESUPUESTOS).read().decode('utf-8')
    soup = BeautifulSoup(html_page, features='html.parser')

    # Buscamos la tabla html de la clasificacion
    tablas_equipo = soup.find_all('table', {'id': 'tabla1'})
    for tabla in tablas_equipo:
        #Tenemos que declarar una variable con un valor por defecto, debido
        #a que hasta que no nos adentremos en la tabla no podemos saber en que
        #tabla nos encontramos
        equipo = 'Default'
        for fila in tabla.tbody:
            if fila.name is not None:
                columnas = fila.find_all('td')
                if columnas[0].text == 'Nombre':
                    equipo = normalize(columnas[1].getText()).upper()
                if columnas[0].text == 'Presupuesto anual':
                    presupuesto = int(columnas[1].getText())
                    presupuestos[equipo] = presupuesto


    return presupuestos

def get_rachas():
    # Las rachas las representamos como diccionario
    rachas = {'ganando':{},
             'empatando': {},
             'perdiendo': {},
             'sin_ganar': {},
             'sin_empatar': {},
             'sin_perder': {}}
    # Buscamos la tabla html de las rachas
    html_page = requests.get(URL_RACHAS)
    soup = BeautifulSoup(html_page.content, features='html.parser')
    tabla = soup.find_all('tr', {'class': 'c-rachas__contenido__fila-inferior__table__row'})
    for i, fila in enumerate(tabla):
        columnas = fila.find_all('td', recursive=False)
        for j, columna in enumerate(columnas):
            #Ya que cada celda tiene en si misma una tabla interior que contiene la información
            #debemos buscar en ella los datos
            tabla_interior = columna.find('table')
            filas_interior = tabla_interior.find_all('tr', {'class': 'fila-racha'})
            for fila_interior in filas_interior:
                    columnas_interior = fila_interior.find_all('td')
                    if columnas_interior:
                        partidos = int(NUM.search(columnas_interior[0].text).group(0))
                        equipo = normalize(NOMBRE.match(columnas_interior[1].text).group(0)).upper()
                        rachas[TIPOS_RACHAS[i][j]][equipo]= partidos
    return rachas

def main():
    print('-------- CLASIFICACIÓN -------')
    pprint(get_clasificacion())
    print('-------- RACHAS -------')
    pprint(get_rachas())
    print('-------- PRESUPUESTOS -------')
    pprint(get_presupuestos())



if __name__ == '__main__':
    sys.exit(main())

