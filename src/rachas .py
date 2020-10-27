import re
import sys
from bs4 import BeautifulSoup
from twill.commands import *

URL_RACHAS = 'https://www.eduardolosilla.es/quiniela/ayudas/rachas'


def get_rachaW():
    # La racha la representamos como diccionario
    racha = {}
    # Compilamos los patrones para un numero y para el nombre de un equipo
    num = re.compile(r'[1-9][0-9]*')
    nombre = re.compile(r'[\w\.]+[\w\. ]*')
    go(URL_RACHAS)
    html = show()
    soup = BeautifulSoup(html, features='html.parser')
    # Buscamos la tabla html de las rachas
    tabla = soup.find('table', {'class': 'c-rachas__contenido_fila-superior_table'})
    for fila in tabla.tbody:
        if (fila.name is not None) and ('c-rachas__tabla__categoria' in fila['class']):
            # Recogemos de cada fila todas las columnas
            columnas = fila.find_all('td')
            partidos = int(num.match(columnas[0].text).group(0))
            equipo = nombre.search(columnas[1].text).group(0)
            racha[equipo] = {'partidos ganados': partidos, }

    return racha
	
def get_rachaT():
    # La racha la representamos como diccionario
    racha = {}
    # Compilamos los patrones para un numero y para el nombre de un equipo
    num = re.compile(r'[1-9][0-9]*')
    nombre = re.compile(r'[\w\.]+[\w\. ]*')
    go(URL_RACHAS)
    html = show()
    soup = BeautifulSoup(html, features='html.parser')
    # Buscamos la tabla html de las rachas
    tabla = soup.find('table', {'class': 'c-rachas__contenido_fila-superior_table'})
    for fila in tabla.tbody:
        if (fila.name is not None) and ('c-rachas__tabla__categoria' in fila['class']):
            # Recogemos de cada fila todas las columnas
            columnas = fila.find_all('td')
            partidos = int(num.match(columnas[2].text).group(0))
            equipo = nombre.search(columnas[3].text).group(0)
            racha[equipo] = {'partidos empatados': partidos, }

    return racha
	
def get_rachaL():
    # La racha la representamos como diccionario
    racha = {}
    # Compilamos los patrones para un numero y para el nombre de un equipo
    num = re.compile(r'[1-9][0-9]*')
    nombre = re.compile(r'[\w\.]+[\w\. ]*')
    go(URL_RACHAS)
    html = show()
    soup = BeautifulSoup(html, features='html.parser')
    # Buscamos la tabla html de las rachas
    tabla = soup.find('table', {'class': 'c-rachas__contenido_fila-superior_table'})
    for fila in tabla.tbody:
        if (fila.name is not None) and ('c-rachas__tabla__categoria' in fila['class']):
            # Recogemos de cada fila todas las columnas
            columnas = fila.find_all('td')
            partidos = int(num.match(columnas[4].text).group(0))
            equipo = nombre.search(columnas[5].text).group(0)
            racha[equipo] = {'partidos perdidos': partidos, }

    return racha
	
def get_rachanW():
    # La racha la representamos como diccionario
    racha = {}
    # Compilamos los patrones para un numero y para el nombre de un equipo
    num = re.compile(r'[1-9][0-9]*')
    nombre = re.compile(r'[\w\.]+[\w\. ]*')
    go(URL_RACHAS)
    html = show()
    soup = BeautifulSoup(html, features='html.parser')
    # Buscamos la tabla html de las rachas
    tabla = soup.find('table', {'class': 'c-rachas__contenido_fila-inferior_table'})
    for fila in tabla.tbody:
        if (fila.name is not None) and ('c-rachas__tabla__categoria' in fila['class']):
            # Recogemos de cada fila todas las columnas
            columnas = fila.find_all('td')
            partidos = int(num.match(columnas[0].text).group(0))
            equipo = nombre.search(columnas[1].text).group(0)
            racha[equipo] = {'partidos sin ganar': partidos, }

    return racha

def get_rachanT():
    # La racha la representamos como diccionario
    racha = {}
    # Compilamos los patrones para un numero y para el nombre de un equipo
    num = re.compile(r'[1-9][0-9]*')
    nombre = re.compile(r'[\w\.]+[\w\. ]*')
    go(URL_RACHAS)
    html = show()
    soup = BeautifulSoup(html, features='html.parser')
    # Buscamos la tabla html de las rachas
    tabla = soup.find('table', {'class': 'c-rachas__contenido_fila-inferior_table'})
    for fila in tabla.tbody:
        if (fila.name is not None) and ('c-rachas__tabla__categoria' in fila['class']):
            # Recogemos de cada fila todas las columnas
            columnas = fila.find_all('td')
            partidos = int(num.match(columnas[2].text).group(0))
            equipo = nombre.search(columnas[3].text).group(0)
            racha[equipo] = {'partidos sin empatar': partidos, }

    return racha

def get_rachanL():
    # La racha la representamos como diccionario
    racha = {}
    # Compilamos los patrones para un numero y para el nombre de un equipo
    num = re.compile(r'[1-9][0-9]*')
    nombre = re.compile(r'[\w\.]+[\w\. ]*')
    go(URL_RACHAS)
    html = show()
    soup = BeautifulSoup(html, features='html.parser')
    # Buscamos la tabla html de las rachas
    tabla = soup.find('table', {'class': 'c-rachas__contenido_fila-inferior_table'})
    for fila in tabla.tbody:
        if (fila.name is not None) and ('c-rachas__tabla__categoria' in fila['class']):
            # Recogemos de cada fila todas las columnas
            columnas = fila.find_all('td')
            partidos = int(num.match(columnas[4].text).group(0))
            equipo = nombre.search(columnas[5].text).group(0)
            racha[equipo] = {'partidos sin perder': partidos, }

    return racha



def main():
    rachaw = get_rachaW()
	rachanw = get_rachanW()
	rachat = get_rachaT()
	rachant = get_rachanT()
	rachal = get_rachaL()
	rachanl = get_rachanL()
    print(rachaw,rachanw,rachat,rachant,rachal,rachanl)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.exit(main())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

