import time
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour
from spade.message import Message
from spade.template import Template

class AgenteReglas(Agent):
    class ReglasBehaviour(OneShotBehaviour):
        async def run(self):
            print("ReglasBehaviour running")

            msg = await self.receive(timeout=10) # wait for a message for 10 seconds
            if msg:
                print("Message received with content: {}".format(msg.body))
            else:
                print("Did not received any message after 10 seconds")

            # stop agent from behaviour
            await self.agent.stop()

    async def setup(self):
        print("Agente Reglas started")
        b = self.ReglasBehaviour()
        template = Template()
        template.set_metadata("performative", "inform")
        self.add_behaviour(b, template)

if __name__ == "__main__":
    receiveragent = AgenteReglas("agente_reglas@localhost", "receiver_password")
    future = receiveragent.start()
    future.result() # wait for receiver agent to be prepared.
    
    while receiveragent.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            receiveragent.stop()
            break
    print("Agents finished")