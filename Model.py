from World import *
from Player import *

class Model:
    
    def __init__(self):
        self.world = World()
        self.player = Player()

        '''
        simple commands are defined as commands that take no arguments i.e. north, south, look etc
        '''
        self.simple_command_dict = {
            'n': 'north',
            's': 'south',
            'w': 'west',
            'e': 'east',
            'north': 'north',
            'south': 'south',
            'west': 'west',
            'east': 'east',
            'where': 'where',
            'where am i': 'where',
            'look': 'where',
            'look around': 'look',
        }
        self.advanced_command_list = [
            'move',
            'take'
        ]

    '''
    A function that changes the visited status of a particular location within the world.
    Takes in the player to get location, and returns the Location object that it has changed the
    visited status of
    '''
    def change_visited(self, player):
        return 0
 
    '''
    take user input from the terminal and return the given command as a string, separates basic
    from the argument consuming commands
    '''
    def take_input(self):
        command = input()
        commands = command.split(' ')
        if command in self.simple_command_dict:
            return command, 'basic'
        elif len(commands) >= 1: #advanced command
            for arg in commands:
                if arg in self.advanced_command_list:
                    return command, 'advanced'
        else: #invalid command
            return False
    
    '''
    take the command string, and parse to determine which action will be taken.
    commands that will trigger the view model must return the as a parse object to 
    be handled within the controller. No model to view communication
    '''
    def parse_input_basic(self, command):
        if command == 'n' or command == 's' or command == 'w' or command == 'e':
            return self.player.move_location(command)
        if command == 'help' or command == 'h':
            return 'help'
        if command == "where" or command == "where am i":
            return "where"

    '''
    Take the command string for more advanced commands, these are defined as commands
    that take positional arguments. Move is an example of a planned command that can take descriptions of
    items to move in certain areas
    '''
    def parse_input_advanced(self, command):
        return 0
        # TODO()

    '''move an object within the world TODO()'''
    def move(self):
        return 0

    '''
    A command that returns a string to the  player indicating where they are located.
    Takes in nothing, returns the locatin object of the players current location
    '''
    def where(self):
        return (self.player.current_location)


        

    