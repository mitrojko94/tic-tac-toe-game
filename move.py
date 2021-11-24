class Move:

    def __init__(self, value) -> None:
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    def is_valid(self):
        return 1 <=self._value <= 9  # Proveravamo da li je vrednost izmedju 1 i 9

    def get_row(self):
        if self._value in (1, 2, 3):
            return 0  # First row
        elif self._value in (4, 5, 6):
            return 1  # Second row
        else:
            return 2  # Threed row

    def get_column(self):
        if self._value in (1, 4, 7):
            return 0  # First column
        elif self._value in (2, 5, 8):
            return 1  # Second column    
        else:
            return 2  # Threed column


#my_move = Move(0)
#print(my_move.value)
#print(my_move.is_valid())
#print(my_move.get_row())
#print(my_move.get_column())