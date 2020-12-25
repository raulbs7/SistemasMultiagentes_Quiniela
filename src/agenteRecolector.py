import sys
import time

from spade import agent
from prosody.prosody_api import Client
from prosody.voice_item import Voice

cli = Client("your_jid@your_xmpp_server", "your_password")

class DummyAgent(agent.Agent):
    def setup(self):
        print("Hello World! I'm agent {}".format(str(self.jid)))

def main():
    dummy = DummyAgent("your_jid@your_xmpp_server", "your_password")
    dummy.start()
    time.sleep(1)
    dummy.stop()

if __name__ == '__main__':
    sys.exit(main())
