from Model import *
from View import *

class Controller:

    def main(self):
        model = Model()
        view = View()
        running = True
        while(running):
            command, command_type = model.take_input()
            if command_type == 'basic':
                parse = model.parse_input_basic(command)
            elif command_type == 'advanced':
                parse = model.parse_input_advanced(command)
            elif command_type == False:
                print("need to parse for invalid command and create statement in view")
                # TODO()
            #print('parse:', parse)
            if parse == 'help':
                view.print_help()
            if parse == "where":
                view.print_location_description(model)
        
        # TODOs
        # A location system that only a vivid description on the first time you travel there TODO()
        return 0
    

    if __name__ == "__main__":
        main(0)