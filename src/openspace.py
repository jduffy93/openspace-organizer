from src.table import Table, Seat
import random


class OpenSpace:
    '''
    The OpenSpace object creates a space in which Tables and Seats can be created.
    It has methods to:
        1 - assign a list of people to a seat
        2 - display the tables and who is sitting at them
        3 - store the displayed information externally in a text file

    Parameters
    ----------
    number_of_tables : int
        number_of_tables is the amount of tables present.
        Set to 6 as default. 

    Attributes
    ----------
    number_of_tables : int
        This is where we store number_of_tables.
    tables : list[object]
        A list of all the tables.
    counter_table : int
        A counter to count which table we are at.
    counter_seat : int
        A counter to count which seat we are at.
    display_str : str
        A string in which we save all the display outputs (who is at what seat at which table)
    '''

    def __init__(self, number_of_tables: int = 6):
        self.number_of_tables = number_of_tables
        self.tables = [Table() for i in range(number_of_tables)]
        self.counter_table = 0
        self.counter_seat = 0
        self.display_str = ''


    def organize(self,names: list):
        '''Randomly assign people to the Seat objects in the different Table objects'''
        
        self.names = random.shuffle(names) # Takes sequence names and randomises the order

        for name in names:
            for table in range(self.number_of_tables):
                if self.tables[table].assign_seat(name):
                    break


    def display(self):
        '''
        Save and display the different tables and their occupant names as well as specifying
        the table and seat numbers in a string.
        '''

        for table in self.tables:
            self.counter_table += 1
            self.display_str += (f'Table number {self.counter_table} \n')
            for chair in table.seats:
                self.counter_seat += 1
                self.display_str += (f'   {self.counter_seat} - {chair.occupant} \n')

        print(self.display_str)


    def store(self,filename: str = 'openspace_output.txt'):
        '''
        Create file 'openspace_output.txt' (as default) and write self.display_string to it
        (if the file already exists, rewrite it).
        '''
        
        try:
            output_file = open(filename, 'x') # Creates output file
        except:
            print(f'{filename} already exists, therefore overwriting it.')
        finally:
            output_file = open(filename, 'w') # Creates output file

        output_file.write(self.display_str)
        output_file.close()