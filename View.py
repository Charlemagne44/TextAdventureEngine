import time

class View:
    '''
    takes in the model object, prints out all the names of various locations within the world object
    '''
    def print_location_names(self, model):
        print(model.world.printLocs())

    '''
    create in intro view script for the game
    '''
    def print_introduction(self):
        directory = './Resources/Checkpoint_Scripts/intro.txt'
        file = open(directory)
        desc = file.readlines()
        self.slow_print_text(desc)

    '''
    Function to slowly release text onto the console, takes no inputs and returns none.
    could be deprecated it GUI is implemented
    '''
    def slow_print_text(self, text):
        for line in text:
            for c in line:
                if(c == '.' or c== '?' or c == '!'):
                    time.sleep(1)
                    print(c, end = "")
                else:
                    time.sleep(0.03)
                    print(c, end ="")


    '''
    takes in the model object, prints out the name of the current location object of the player
    '''
    def get_player_location_name(self, model):
        print(model.player.current_location.name)

    '''
    prints out a guide for the player to understand all possible commands in the terminal
    '''
    def print_help(self):
        print("Welcome to \"While I'm Gone\". Here is a comprehensive list of commands at your disposal\nn or north\ns or south\ne or east\nw or west\nmove [object]")

    '''
    Print out message for incorrect user input
    takes none, returns none
    '''
    def incorrect_input(self):
        print("I didn't understand that, use 'help' to get a full list of commands")

    '''
    prints out a description of the players current location, as well as their neighbors vague descriptions
    '''
    def print_location_description(self, model):
        current_loc = model.player.current_location
        name = current_loc.name
        directory = './Resources/Descriptions/' + name + '.txt'
        file = open(directory)
        desc = file.readlines()
        print("Where you stand, you look around and see ", end = ' ')
        # printing description, implement the slow print for readability later TODO()
        for line in desc:
            print(line)


        # printing the neighbors more vague descriptions
        #print(" you see ", sep='')
        for direction in current_loc.neighbors:
            if direction == 'n':
                print("Off to the north,", end = ' ')
            elif direction == "s":
                print("Towards the south,", end = ' ')
            elif direction == "e":
                print("To the east,", end = ' ')
            elif(direction == "w"):
                print("Westward,", end = ' ')
            name = current_loc.neighbors[direction]
            directory = './Resources/Distant_Descriptions/' + name + '.txt'
            file = open(directory)
            desc = file.readlines()
            for line in desc:
                print(line)
