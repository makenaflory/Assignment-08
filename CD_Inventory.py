#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# MMezistrano, 2020-Mar-16, Reviewed pseudocode, drafted code
# MMezistrano, 2020-Mar-17, Class 8. Rewrote code according to class instructions
#------------------------------------------#

# -- DATA -- #
strChoice = ''
strFileName = 'cdInventory.txt'

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods: 
        append cd data to list of objects #need to format differently?

    """
    # TODO/done Add Code to the CD class
    
    # -- Constructor -- #
    def __init__ (self, cd_id, cd_title, cd_artist):
        # -- Attributes -- #
        try: #Because we're casting, need error handling
            self.__cd_id = int(cd_id)
            self.__cd_title = cd_title
            self.__cd_artist = cd_artist
        except Exception as e:
            raise Exception('Error setting initial values:\n' + str(e))
        
    # -- Properties -- #
    
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter 
    def cd_id(self, value):
        self.__cd_id = value
    
    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, value):
        self.__cd_title = str(value)
    
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self, value):
        self.__cd_artist = str(value)
    
    # -- Methods -- #
    def print_neat(self): # Looks at the CD object we called on - looks at one CD 
        #and uses this function to print out a formatted string with info about this one CD. 
        return '{}\t{} (by:{})'.format(self.cd_id, self.cd_title, self.cd_artist)
    
    def print_file(self): # function for writing to file, CD object will now be formatted how we want to see it on the file
        return '{},{},{}\n'.format(self.cd_id, self.cd_title, self.cd_artist)
   

# -- PROCESSING -- #

class FileIO:
    """Processes data to and from file:

    properties: 

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODO/done Add code to process data from a file
    @staticmethod
    def load_inventory(file_name): #can't reuse what we did in mod 7 because there we were pickling, don't need that here.
        """ Function to load data from file to a list of CD objects
        
        Reads the data from a file identified by file_name into a 2D table
        
        Args:
            file_name(string): name of file used to read data from
            
        Returns:
            2D list: list of CD Objects.
        """
        table = [] #table as list
        try: # error handling to make sure file exists
            with open(file_name, 'r') as f:
                for line in f:
                    data = line.strip().split(',')
                    row = CD(data[0], data[1], data[2]) #each row ingested, each index refers to ID, title, artist
                    table.append(row)
                return table
        
        except FileNotFoundError as e: #trying to open a file that doesn't exist, or if they type the file name wrong
            print('Error: File {} could not be loaded'.format(file_name))
            print('Error info:')
            print(type(e), e, sep='\n')
    
    # TODO Add code to process data to a file
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
    
        """ Function to save CD inventory (list of CD Objects) to file
        
        Saves data from table to file with each on its own line, values are comma separated
        
        Args: 
            file_name: name of file used to write the data to
            lst_Inventory: list of CD Objects
        Returns:
            none
        """
        objFile = open(file_name, 'w')
        for row in lst_Inventory: # list of references to CD objects, goes through each individual reference
            objFile.write(row.print_file()) # each row is a reference to a CD object. This exevutes the function print_file
        objFile.close()

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output""" # TODO/done add docstring
    
    # TODO/done add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[i] Display Current Inventory\n[a] Add CD\n[s] Save Inventory to file\n[l] load Inventory from file\n[x] exit\n')

    @staticmethod
    def menu_choice(): # TODO/done add code to captures user's choice
        """Gets user input for menu selection, returns ValueError if choice not in menu.

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' ' 
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Extra space for layout
        return choice
    
    # TODO add code to display the current data on screen
    @staticmethod
    def show_inventory(table): 
        """Displays current inventory table

        Args:
            table (list of CDObjects): 2D data structure (list of CDObjects) that holds the data during runtime.

        Returns:
            None.
            
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row.print_neat()) #cycling through each CD object and print_neat shows the individual values of each object
        print('======================================')
    
    # TODO/drafted add code to get CD data from user 
    @staticmethod
    def get_user_input(): 
        """Allows user to input new CD into the inventory.
        
        Args:
            None.
        
        Returns:
            cd_id (int): CD ID to add to the database
            cd_title (string): Title of CD to add to the database
            cd_artist (string): Artist of CD to add to the database
            
        """
        cd_id = input('Enter ID: ').strip()
        cd_title = input('What is the CD\'s title? ').strip()
        cd_artist = input('What is the Artist\'s name? ').strip()
        return cd_id, cd_title, cd_artist  
    
class DataProcessor:
    """ Appends data to list of objects """

    @staticmethod
    def add_cd(CDInfo, table):
        """ Function to add CD to the inventory

        Args:
            CDInfo (tuple): Holds information to be added to inventory
        Returns:
            table (list of CDObjects): 2D data structure, list of dicts, holds cd inventory information

        """
        cdId, title, artist = CDInfo 
        try:
            cdId = int(cdId)
        except ValueError as e: # error handling to make sure ID is an integer
            print('ID is not an integer!')
            print(e.__doc__)
        row = CD(cdId, title, artist) #creates a CD object
        table.append(row) # appends the object to a table
        return table
    
# -- Main Body of Script -- #
# TODO/done Add Code to the main body
        
# Load data from file into a list of CD objects on script start
lstOfCDObjects = FileIO.load_inventory(strFileName)

while True:
    # Display menu to user
    IO.print_menu() 
    strChoice = IO.menu_choice()    
    # let user exit program/done
    if strChoice == 'x': 
        break
    # show user current inventory
    elif strChoice == 'i': 
        IO.show_inventory(lstOfCDObjects)
        continue
    # let user add data to the inventory
    elif strChoice == 'a': 
        tplCdInfo = IO.get_user_input()
        DataProcessor.add_cd(tplCdInfo, lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)
        continue
    # let user save inventory to file
    elif strChoice == 's': 
        IO.show_inventory(lstOfCDObjects) # Display current inventory; ask user for confirmation to save
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y': # Process choice
            FileIO.save_inventory(strFileName, lstOfCDObjects) # save data
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  
    # let user load inventory from file
    if strChoice == 'l':
       print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
       strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
       if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName) #must use defined method name of load_inventory (used to be read_inventory)
            IO.show_inventory(lstOfCDObjects)
       else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
       continue  
       # catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
    else:
        print('General Error')