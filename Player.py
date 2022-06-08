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
    def move_location(self, direction):
        if direction in self.current_location.neighbors:
            new_loc_name = self.current_location.neighbors[direction]
            self.current_location = Location(new_loc_name)
            return Location(new_loc_name)
