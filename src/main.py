import re
import sys
from bs4 import BeautifulSoup
from twill.commands import *

URL_CLASIFICACION = 'https://www.eduardolosilla.es/quiniela/ayudas/clasificacion'


def get_clasificacion():
    # La clasificacion la representamos como diccionario
    clasificacion = {}
    # Compilamos los patrones para un numero y para el nombre de un equipo
    num = re.compile(r'[1-9][0-9]*')
    nombre = re.compile(r'[\w\.]+[\w\. ]*')
    go(URL_CLASIFICACION)
    html = show()
    soup = BeautifulSoup(html, features='html.parser')
    # Buscamos la tabla html de la clasificacion
    tabla = soup.find('table', {'class': 'c-clasificacion__tabla ng-star-inserted'})
    for fila in tabla.tbody:
        if (fila.name is not None) and ('c-clasificacion__tabla__categoria' in fila['class']):
            # Recogemos de cada fila todas las columnas
            columnas = fila.find_all('td')
            posicion = int(num.match(columnas[0].text).group(0))
            equipo = nombre.search(columnas[1].text).group(0)
            puntos = int(num.match(columnas[2].text).group(0))
            clasificacion[equipo] = {'posicion': posicion, 'puntos': puntos}

    return clasificacion


def main():
    clasificacion = get_clasificacion()
    print(clasificacion)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sys.exit(main())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
