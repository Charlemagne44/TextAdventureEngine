from Model import *
from View import *

class Controller:

    def main(self):
        model = Model()
        view = View()
        running = True
        #intialized the visited status of first location to True
        while(running):
            command, command_type = model.take_input()
            #print('command:', command)
            #print('command type', command_type)
            if command_type == 'basic':
                parse = model.parse_input_basic(command)
            elif command_type == 'advanced':
                parse = model.parse_input_advanced(command)
            elif command_type == 'view':
                if command == 'help':
                    view.print_help()
                elif command == 'where':
                    view.print_location_description(model)
            elif command_type == False:
                view.incorrect_input()
            #TODO(make these happen in the parse input within the model)
        
        # TODOs
        # A location system that only a vivid description on the first time you travel there TODO()
        return 0
    

    if __name__ == "__main__":
        main(0)