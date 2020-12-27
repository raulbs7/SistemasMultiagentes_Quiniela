import json
import sys
import time

import extractor as extr
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.message import Message


class AgenteRecolector(Agent):
    class RecolectarBehaviour(OneShotBehaviour):
        async def on_start(self):
            print("Starting RecolectarBehaviour . . .")
            self.clasificacion = extr.get_clasificacion()
            self.rachas = extr.get_rachas()
            self.presupuestos = extr.get_presupuestos()
            if len(sys.argv) == 2:
                self.equipo = sys.argv[1]
            else:
                raise Exception("Invalid command line arguments")

        async def run(self):
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
            msg = Message(to="agente_reglas@localhost")  # Instantiate the message
            msg.set_metadata("performative", "inform")  # Set the "inform" FIPA performative
            msg.body = json.dumps(information)  # Set the message content
            msg.sender = "agente_recolector@localhost"
            await self.send(msg)
            # await asyncio.sleep(1)

        async def on_end(self):
            print("RecolectarBehaviour finished with exit code {}.".format(self.exit_code))

    async def setup(self):
        print("Agente Recolector starting . . .")
        self.my_behav = self.RecolectarBehaviour()
        self.add_behaviour(self.my_behav)


if __name__ == "__main__":
    agente = AgenteRecolector("agente_recolector@localhost", "password")
    agente.start()
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break
    agente.stop()
