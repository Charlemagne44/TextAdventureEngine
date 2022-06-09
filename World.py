from Location import *

class World:
    def __init__(self):
        self.locations = {
            "Castle Yard": Location("Castle Yard"), #Players starting location
            "Graveyard" : Location("Graveyard"),
            "Tunnel" : Location("Tunnel")
        }
        # initialize first location to visited 
        self.locations["Castle Yard"].change_visited()
