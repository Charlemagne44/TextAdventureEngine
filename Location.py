class Location:

    def __init__(self, name):
        self.name = name
        self.neighbors = self.assign_neighbors(name)
        self.visited = False
        
    def assign_neighbors(self, name):
        if name == "Castle Yard":
            return {'n': "Graveyard",
                    's': "Tunnel"
            }
        elif name == "Graveyard":
            return {'s': 'Castle Yard'}

        elif name == "Tunnel":
            return {'n': 'Castle Yard'}

