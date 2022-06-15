class Location:

    def __init__(self, name):
        self.name = name
        self.neighbors = self.assign_neighbors(name)
        self.visited = False

    '''
    Simply changes the visited attribute of the location called upon to True
    Takes in location, returns True if it was originally unvisited (i.e. first visit)
    '''
    def change_visited(self):
        if self.visited == False:
            self.visited = True
            return True
        else:
            self.visited = True
            return False
        
        
    '''
    Assigns the neighboring locations of a particular location in the world,
    all are predefined. # TODO() move to CSV implementation to make this more
    user friendly
    '''
    def assign_neighbors(self, name):
        if name == "Castle Yard":
            return {'north': "Graveyard",
                    'south': "Tunnel"
            }
        elif name == "Graveyard":
            return {'south': 'Castle Yard'}
        elif name == "Tunnel":
            return {'north': 'Castle Yard'}

