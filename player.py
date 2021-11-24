import random

from move import Move


class Player:

    PLAYER_MARKER = "X"  #Ovo je stavljeno, jer moze da bude bilo koje slovo i ono ce se odnositi na humana
    COMPUTER_MARKER = "O"

    def __init__(self, is_human=True) -> None:
        self._is_human = is_human

        if is_human:  # Moze da se napise isto is_human == True
            self._marker = Player.PLAYER_MARKER  # Dodjeljujemo markere ko je koji
        else:
            self._marker = Player.COMPUTER_MARKER

    @property
    def is_human(self):
        return self._is_human

    @property
    def marker(self):
        return self._marker    
    
    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()
    
    def get_human_move(self):
        while True:
            user_input = int(input("Please enter your move (1-9): "))
            move = Move(user_input)  #Move zahteva vrednost od 1-9 i mi stavljamo user_input, jre time biramo vrednost
            if move.is_valid():  #Proverava da li je move validan na osnovu ove funkcije is_valid koja je definisana u klasi Move
                break
            else:
                print("Please enter an integer between 1 and 9")
        return move

    def get_computer_move(self):
        random_choice = random.choice(list(range(1, 10)))
        move = Move(random_choice)
        print(f"Computer move is {move.value}")
        return move


#my_player = Player()  # Human player, jer je po defaultu 
#print(my_player.is_human)
#print(my_player.marker)
#move = my_player.get_move()
#print(move.value)
#my_player.get_computer_move()

#computer = Player(False)
#move = computer.get_computer_move()
#print(move.value)