import json
import sys
import time
import uuid
import extractor as extr
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.message import Message
from colorama import Fore, Back, Style
import os

class AgenteRecolector(Agent):
    class RecolectarBehaviour(OneShotBehaviour):
        async def on_start(self):
            print(Fore.YELLOW+"Starting RecolectarBehaviour . . ."+Fore.RESET)
            # Extraemos a traves del script extractor la clasificacion, las rachas y
            # los presupuestos
            self.clasificacion = extr.get_clasificacion()
            self.rachas = extr.get_rachas()
            self.presupuestos = extr.get_presupuestos()
            self.equipo = sys.argv[1].upper()

        async def run(self):
            # Cogemos la clasificacion, el presupuesto y las rachas de el equipo escogido
            try:
                clasificacion_equipo = self.clasificacion[self.equipo]['posicion']
            except KeyError as error:
                raise KeyError(f'No se puede obtener la clasificación del equipo {self.equipo}: {error}')
            try:
                if self.equipo in self.presupuestos.keys():
                    presupuesto_equipo = self.presupuestos[self.equipo]
                else:
                    presupuesto_equipo = 0
            except KeyError as error:
                raise KeyError(f'No se puede obtener el presupuesto del equipo {self.equipo}: {error}')
            try:
                if self.equipo in self.rachas['ganando'].keys():
                    rachaG_equipo = self.rachas['ganando'][self.equipo]
                else:
                    rachaG_equipo = 0
            except KeyError as error:
                raise KeyError(f'No se pueden obtener las rachas de partidos ganados por {self.equipo}: {error}')
            try:
                if self.equipo in self.rachas['perdiendo'].keys():
                    rachaP_equipo = self.rachas['perdiendo'][self.equipo]
                else:
                    rachaP_equipo = 0
            except KeyError as error:
                raise KeyError(f'No se pueden obtener las rachas de partidos perdidos por {self.equipo}: {error}')
            try:
                if self.equipo in self.rachas['empatando'].keys():
                    rachaE_equipo = self.rachas['empatando'][self.equipo]
                else:
                    rachaE_equipo = 0
            except KeyError as error:
                raise KeyError(f'No se pueden obtener las rachas de partidos empatados por {self.equipo}: {error}')
            try:
                if self.equipo in self.rachas['sin_ganar'].keys():
                    rachaNG_equipo = self.rachas['sin_ganar'][self.equipo]
                else:
                    rachaNG_equipo = 0
            except KeyError as error:
                raise KeyError(f'No se pueden obtener las rachas de partidos empatados por {self.equipo}: {error}')
            try:
                if self.equipo in self.rachas['sin_perder'].keys():
                    rachaNP_equipo = self.rachas['sin_perder'][self.equipo]
                else:
                    rachaNP_equipo = 0
            except KeyError as error:
                raise KeyError(f'No se pueden obtener las rachas de partidos empatados por {self.equipo}: {error}')

            information = {
                'clasificacion': clasificacion_equipo,
                'presupuesto': presupuesto_equipo,
                'rachas': {
                    'ganando': rachaG_equipo,
                    'empatando': rachaE_equipo,
                    'perdiendo': rachaP_equipo,
                    'sin_ganar': rachaNG_equipo,
                    'sin_perder': rachaNP_equipo
                }
            }
            # Creamos el mensaje y lo mandamos al agente de reglas difusas
            msg = Message(to="agente_reglas@localhost")  
            msg.set_metadata("performative", "inform")  # Su performativa será de tipo inform
            msg.body = json.dumps(information)  # Convertimos el diccionario con la informacion del equipo en string
            # Mandamos el mensaje
            await self.send(msg)
            # Detenemos el agente
            await self.agent.stop()

        async def on_end(self):
            print(Fore.YELLOW+"RecolectarBehaviour finished with exit code {}.".format(self.exit_code)+Fore.RESET)

    async def setup(self):
        print(Fore.CYAN+Style.BRIGHT+f"[{self.jid}]",
            Style.NORMAL+" AGENTE RECOLECTOR STARTING . . ."+Fore.RESET+Style.RESET_ALL)
        # Añadimos comportamiento
        self.my_behav = self.RecolectarBehaviour()
        self.add_behaviour(self.my_behav)


if __name__ == "__main__":
    # Obtenemos argumentos
    if len(sys.argv) == 3:
        nombre_agente = sys.argv[2]
    elif len(sys.argv) == 2:
        nombre_agente = uuid.uuid4().hex
    else:
        raise Exception("Invalid command line arguments")

    # Iniciamos agente recolector
    agente = AgenteRecolector(f"{nombre_agente}@localhost", "password")
    future = agente.start()
    future.result()  # wait for receiver agent to be prepared.

    # Mientras que este vivo se puede interrumpir
    while agente.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            agente.stop()
            break
    print(Fore.CYAN+Style.BRIGHT+f"[{agente.jid}]",
        Style.NORMAL+" AGENTE RECOLECTOR FINISHED"+Fore.RESET+Style.RESET_ALL)
