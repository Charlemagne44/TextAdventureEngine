class View:
    '''
    takes in the model object, prints out all the names of various locations within the world object
    '''
    def print_location_names(self, model):
        print(model.world.printLocs())

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
    prints out a description of the players current location, as well as their neighbors vague descriptions
    '''
    def print_location_description(self, model):
        current_loc = model.player.current_location
        name = current_loc.name
        directory = './Resources/Descriptions/' + name + '.txt'
        file = open(directory)
        desc = file.readlines()
        print("Where you stand, you look around and see ", sep='')
        # printing description, implement the slow print for readability later TODO()
        for line in desc:
            print(line)


        # printing the neighbors more vague descriptions
        #print(" you see ", sep='')
        for direction in current_loc.neighbors:
            if direction == 'n':
                print("Off to the north, ")
            elif direction == "s":
                print("Towards the south, ")
            elif direction == "e":
                print("To the east, ")
            elif(direction == "w"):
                print("Westward, ")
            name = current_loc.neighbors[direction]
            directory = './Resources/Distant_Descriptions/' + name + '.txt'
            file = open(directory)
            desc = file.readlines()
            for line in desc:
                print(line)
