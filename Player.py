from Location import *
from World import *
class Player:
    def __init__(self):
        self.name = "change later"
        self.current_location = Location("Castle Yard")

    '''
    given a string indicating direction, change the players location to the location object
    indicated in that particular direction. Returns new Location and True if originally unvisited, False otherwise
    '''
    def move_location(self, direction, world):
        print('current loc neighors:', self.current_location.neighbors)
        if direction in self.current_location.neighbors:
            #print('doin the move')
            new_loc_name = self.current_location.neighbors[direction]
            #print('old current location:', self.current_location)
            self.current_location = world.locations[new_loc_name]
            #print('new current location:', self.current_location)
            # change the status of new location to visited
            #print('\ndebugging, visited status before: ', self.current_location.visited, ' \n')
            if self.current_location.change_visited():
                return 'first visit'
            #print('\ndebugging, visited status after: ', self.current_location.visited, ' \n')
            return 'revisit'
