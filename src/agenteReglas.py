import time
import json
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.message import Message
from spade.template import Template
import numpy as np
import skfuzzy as fuzz
import operator
from colorama import Fore, Back, Style

import reglas


class AgenteReglas(Agent):
    class ReglasBehaviour(OneShotBehaviour):

        async def on_start(self):
            print(Fore.YELLOW+"Starting ReglasBehaviour . . ."+Fore.RESET)
            # Importamos el controlador de nuestra logica difusa
            self.quiniela = reglas.sis_quiniela()
        
        async def run(self):
            msgLocal = await self.receive(timeout=10)  # wait for a message for 10 seconds
            msgVisitante = await self.receive(timeout=10)  # wait for a message for 10 seconds
            if msgLocal and msgVisitante:    
                print(Fore.GREEN+'Mensajes recibidos de los agentes recolectores'+Fore.RESET)
            else:
                raise TimeoutError('Mensaje perdido o no recibido')
            
            # Parseamos el string del body del mensaje otra vez a un diccionario
            equipoLocal = json.loads(msgLocal.body)
            equipoVisitante = json.loads(msgVisitante.body)

            # Metemos los datos en el controlador
            self.quiniela.input['Clasificacion_Local'] = equipoLocal['clasificacion']
            self.quiniela.input['Clasificacion_Visitante'] = equipoVisitante['clasificacion']
            self.quiniela.input['Presupuesto_Local'] = (equipoLocal['presupuesto'] / 1000000)
            self.quiniela.input['Presupuesto_Visitante'] = (equipoVisitante['presupuesto'] / 1000000)
            self.quiniela.input['RachaG_Local'] = equipoLocal['rachas']['ganando']
            self.quiniela.input['RachaG_Visitante'] = equipoVisitante['rachas']['ganando']
            self.quiniela.input['RachaE_Local'] = equipoLocal['rachas']['empatando']
            self.quiniela.input['RachaE_Visitante'] = equipoVisitante['rachas']['empatando']
            self.quiniela.input['RachaP_Local'] = equipoLocal['rachas']['perdiendo']
            self.quiniela.input['RachaP_Visitante'] = equipoVisitante['rachas']['perdiendo']
            self.quiniela.input['RachaNG_Local'] = equipoLocal['rachas']['sin_ganar']
            self.quiniela.input['RachaNG_Visitante'] = equipoVisitante['rachas']['sin_ganar']
            self.quiniela.input['RachaNP_Local'] = equipoLocal['rachas']['sin_perder']
            self.quiniela.input['RachaNP_Visitante'] = equipoVisitante['rachas']['sin_perder']

            # Computamos para obtener las pertenecias
            self.quiniela.compute()
            range_result = np.arange(1, 9, 1)

            val = self.quiniela.output['Result']
            variable = reglas.consequent()['1']
            pertenencia_1 = fuzz.interp_membership(range_result, variable.mf, val)

            val = self.quiniela.output['Result']
            variable = reglas.consequent()['X']
            pertenencia_x = fuzz.interp_membership(range_result, variable.mf, val)

            val = self.quiniela.output['Result']
            variable = reglas.consequent()['2']
            pertenencia_2 = fuzz.interp_membership(range_result, variable.mf, val)
            
            # Una vez obtenidasd las pertenencias de cada resultado, las ordenamos
            pertenencias = {'1': pertenencia_1,
                            'X': pertenencia_x,
                            '2': pertenencia_2}
            pertenencias_ord = sorted(pertenencias.items(), key=operator.itemgetter(1), reverse=True)
            
            # Printeamos el resultado
            print(Back.YELLOW+Style.BRIGHT+Fore.BLACK+'Etiqueta resultado:'+Back.RESET+Fore.RESET, 
                Fore.GREEN+f' {pertenencias_ord[0][0]}'+Fore.RESET+Style.RESET_ALL)
            print(Back.YELLOW+Style.BRIGHT+Fore.BLACK+'Máximo grado de pertencia:'+Back.RESET+Fore.RESET, 
                Fore.GREEN+f' {pertenencias_ord[0][1]}'+Fore.RESET+Style.RESET_ALL)

            # Paramos el agente
            await self.agent.stop()

    async def setup(self):
        print(Fore.CYAN+Style.BRIGHT+f"[{self.jid}]",
            Style.NORMAL+" AGENTE REGLAS STARTED"+Fore.RESET+Style.RESET_ALL)
        b = self.ReglasBehaviour()
        # Creamos una template con la que solo podremos recibir mensaje de con performativa inform
        template = Template()
        template.set_metadata("performative", "inform")
        # Añadimos comportamiento
        self.add_behaviour(b, template)


if __name__ == "__main__":
    #Iniciamos agente recolector
    agente = AgenteReglas("agente_reglas@localhost", "receiver_password")
    future = agente.start()
    future.result()

    # Mientras que este vivo se puede interrumpir
    while agente.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            agente.stop()
            break
    print(Fore.CYAN+Style.BRIGHT+f"[{agente.jid}]",
        Style.NORMAL+" AGENTE REGLAS FINISHED"+Fore.RESET+Style.RESET_ALL)
