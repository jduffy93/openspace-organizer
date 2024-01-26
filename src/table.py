class Seat:
    '''
    The Seat object contains methods for setting and removing an occupant from a seat.

    Parameters
    ----------
    free : bool
        free is used for assertaining if a seat is free.
        Set to True as default. 

    Attributes
    ----------
    free : bool
        This is where we store free.
    occupant : str
        This is where we store the name of the occupant of the seat.
    '''

    def __init__(self, free: bool = True):
        self.free = free
        self.occupant = None


    def set_occupant(self, name: str):
        '''If free = True, set occupant = name and set free = False'''

        self.name = name
        if self.free:
            self.occupant = name
            self.free = False
            return True
        else:
            return False


    def remove_occupant(self):
        '''If free = False, print occupant, remove occupant and set free == True'''

        if not self.free:
            print(f'{self.occupant}')
            self.occupant = None
            self.free = True
        else:
            print(f'This seat is already free')
        

class Table:
    '''
    The Table object contains methods for:
        1 - cheking if a table has a free spot
        2 - assigning a seat to a person
        3 - checking how many seats are left at a table.

    Parameters
    ----------
    capacity : int
        capacity specifies how many seats can exist around a table.
        Set to 4 as default. 

    Attributes
    ----------
    capacity : int
        This is where we store the capacity.
    seats : list[object]
        A list of all the seats around a table.
    '''

    def __init__(self, capacity: int = 4):
        self.capacity = capacity
        self.seats = [Seat() for i in range(capacity)]


    def has_free_spot(self) -> bool:
        '''Check if free = True for instance of Seat() and return bool.'''
        
        return (chair.free for chair in self.seats)


    def assign_seat(self, name: str):
        '''Assigns name to attribute occupant if method has_free_spot = True'''

        for chair in self.seats:
            if chair.set_occupant(name):
                return True


    def capacity_left(self):
        '''Outputs how many chairs are free at a table'''

        return print(sum(chair.free for chair in self.seats))
        