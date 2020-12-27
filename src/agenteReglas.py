import time
import json
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.message import Message
from spade.template import Template
import reglas

class AgenteReglas(Agent):
    class ReglasBehaviour(OneShotBehaviour):

        async def on_start(self):
            print("Starting ReglasBehaviour . . .")
            self.quiniela = reglas.sis_quiniela()
        
        async def run(self):
            print("ReglasBehaviour running")
            msgLocal = await self.receive(timeout=10)  # wait for a message for 10 seconds
            msgVisitante = await self.receive(timeout=10)  # wait for a message for 10 seconds
            if msgLocal and msgVisitante:    
                print('Mensajes recibidos de los agentes recolectores')
            else:
                raise TimeoutError('Mensaje perdido o no recibido')

            equipoLocal = json.loads(msgLocal.body)
            equipoVisitante = json.loads(msgVisitante.body)

            print(equipoLocal)
            print(equipoVisitante)

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

            self.quiniela.compute()
            reglas.consequent().view(sim=self.sistema_quiniela)
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
            
            pertenencias = {'pertenencia1': pertenencia_1,
                    'pertenenciaX': pertenencia_x,
                    'pertenencia2': pertenencia_2}
            pertenencias_ord = sorted(pertenencias.items(), key=operator.itemgetter(1))

            print(f'Etiqueta resultado: {pertenencias_ord[0][0]}')
            print(f'Máximo grado de pertencia: {pertenencias_ord[0][1]}')

            await self.agent.stop()

    async def setup(self):
        print(f"[{self.jid}] Agente Reglas started")
        b = self.ReglasBehaviour()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)


if __name__ == "__main__":
    receiveragent = AgenteReglas("agente_reglas@localhost", "receiver_password")
    future = receiveragent.start()
    future.result()  # wait for receiver agent to be prepared.

    while receiveragent.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            receiveragent.stop()
            break
    print("Agents finished")
