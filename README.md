# SistemasMultiagentes_Quiniela

_La función de este proyecto es la extracción de datos acerca de los equipos de Primera y Segunda División de Fútbol y, con estos datos, realizar un sistema multiagente que nos permitriá predecir el resultado para una quiniela. Esto se lleva a cabo mediante la implementación de reglas lógicas difusas._

## Comenzando 🚀

_Una vez clonado el repositorio debemos realizar lo siguiente_

### Pre-requisitos 📋

_En cuanto al lenguaje será necesario la siguiente versión de Python o posterior_

```
Python 3.6.9
```

### Instalación 🔧

_Para la instalación de las dependencias necesarias, existen dos opciones:_

1. Instalación en máquina local

_Para ello, lo único que debemos hacer será:_

```
pip3 install -r requirements.txt
```

2. Instalación en entorno virtual (más recomendable)

_Primero deberemos tener instalado el paquete **virtualenv**_

```
pip3 install virtualenv
```

_Una vez ya instalado podremos crear un entorno virtual_

```
python3 -m venv venv
```

_Con esto ya tendremos el entorno virtual instalado, pero antes de instalar dependencias deberemos instalarlo._

```
source venv/bin/activate
```

_O también._

```
. ./venv/bin/activate
```
## Ejecutar ⚙️

Antes de pasar a definir la ejecución, debemos especificar cuales son los equipos actuales, para llevar a cabo la predicción del partido **(se deben pasar a los scripts tal y como se encuentran aquí escritos)**:

- **Primera división**
    - Alaves
    - Atletico
    - Athletic
    - Barcelona
    - Betis
    - Cadiz
    - Celta
    - Eibar
    - Elche
    - Getafe
    - Granada
    - Huesca
    - Levante
    - Madrid
    - Osasuna
    - Sevilla
    - Sociedad
    - Valencia
    - Valladolid
    - Villarreal
- **Segunda división**
    - Albacete
    - Alcorcon
    - Almeria
    - Castellon
    - Cartagena
    - Espanyol
    - Fuenlabrada
    - Girona
    - Las Palmas
    - Leganes
    - Logroñes
    - Lugo
    - Malaga
    - Mallorca
    - Mirandes
    - Oviedo
    - Ponferradina
    - Rayo
    - Sabadell
    - Sporting
    - Tenerife
    - Zaragoza

Estos 
_Para ejecutar tendremos también dos opciones:_

### 1. Ejecutar scripts manualmente

_Para ello primero debemos ejecutar el agente de reglas difusas, ya que es el que espera la información de los otros agentes._

```
python3 src/agenteReglas.py
```

_Rápidamente ejecutamos un scripts dos veces uno con el equipo local y otro con el equipo visitante. Debemos determinar en el primer argumento el equipo al que hacemos referencia. También es opcional en el segundo argumento poner el nombre de dicho agente en el **servidor XMPP**_

```
python3 src/agenteRecolector.py sevilla
```

```
python3 src/agenteRecolector.py cadiz agente2
```

### 2. Ejecutar script run-agents.sh

_Este script ejecuta los agentes automáticamente. En el podremos pasarle los argumentos anteriores:_

Uso: run-agents.sh -L equipo_local -V equipo_visitante [-l id_agente_local | -v id_agente_visitante]

        -L Nombre del equipo local
        -V Nombre del equipo visitante
        -l Identificador para el agente recolector del equipo local
        -v Identificador para el agente recolector del equipo visitante

```
sh run-agents.sh -L sociedad -V eibar
```

```
sh run-agents.sh -L sociedad -V eibar -l agenteLocal -v agenteVisitante
```

## Autores ✒️

* **Raúl Bernalte Sánchez** - [raulbs7](https://github.com/raulbs7)
* **Guillermo Bautista Ruíz**  - [Lhions](https://github.com/Lhions)



