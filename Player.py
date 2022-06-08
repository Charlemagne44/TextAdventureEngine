from Location import *
from World import *
class Player:
    def __init__(self):
        self.name = "change later"
        self.current_location = Location("Castle Yard")

    '''
    given a string indicating direction, change the players location to the location object
    indicated in that particular direction. Returns new Location
    '''
    def move_location(self, direction, world):
        if direction in self.current_location.neighbors:
            new_loc_name = self.current_location.neighbors[direction]
            self.current_location = world.locations[new_loc_name]
            # change the status of new location to visited
            self.current_location.visited = True
            return self.current_location
