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
        }
        self.view_commands = {
            'where': 'where',
            'where am i': 'where',
            'look': 'where',
            'look around': 'here',
            'help': 'help',
            'h': 'help',
            'help me': 'help',
            'help please': 'help'
        }
        self.advanced_command_list = [
            'move',
            'take'
        ]
 
    '''
    take user input from the terminal and return the given command as a string, separates basic
    from the argument consuming commands
    '''
    def take_input(self):
        command = input()
        commands = command.split(' ')
        if command in self.simple_command_dict: # basic command
            #print('basic command from dict:', self.simple_command_dict[command])
            return self.simple_command_dict[command], 'basic'
        elif command in self.view_commands:
            return self.view_commands[command], 'view'
        elif len(commands) >= 2: #advanced command
            for arg in commands:
                #print('advanced command check, arg: ', arg)
                if arg in self.advanced_command_list:
                    return command, 'advanced'
            #invalid command, must catch as it won't jump to last check
            return command, False
        else: #invalid command
            #print('invalid command is: ', command)
            return command, False
    
    '''
    take the command string, and parse to determine which action will be taken.
    commands that will trigger the view model must return the as a parse object to 
    be handled within the controller. No model to view communication
    '''
    def parse_input_basic(self, command):
        print('parse input:', command)
        if command == 'north' or command == 'south' or command == 'east' or command == 'west':
            print('moving:')
            return self.player.move_location(command, self.world)
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


        

    