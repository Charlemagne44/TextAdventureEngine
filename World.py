from Location import *

class World:
    def __init__(self):
        self.locations = {
            "Castle Yard": Location("Castle Yard"),
            "Graveyard" : Location("Graveyard"),
            "Tunnel" : Location("Tunnel")
        }
