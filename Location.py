class Location:

    def __init__(self, name):
        self.name = name
        self.neighbors = self.assign_neighbors(name)
        self.visited = False

    '''
    Simply changes the visited attribute of the location called upon to True
    Takes in location, returns none
    '''
    def change_visited(self):
        self.visited = True
        
    '''
    Assigns the neighboring locations of a particular location in the world,
    all are predefined. # TODO() move to CSV implementation to make this more
    user friendly
    '''
    def assign_neighbors(self, name):
        if name == "Castle Yard":
            return {'n': "Graveyard",
                    's': "Tunnel"
            }
        elif name == "Graveyard":
            return {'s': 'Castle Yard'}

        elif name == "Tunnel":
            return {'n': 'Castle Yard'}

