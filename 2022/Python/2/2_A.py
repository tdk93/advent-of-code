from enum import Enum, auto

class Move(Enum):
    ROCK=auto()
    PAPER = auto()
    SCISSOR = auto()

class Player(Enum):
    NIL = auto()
    ME = auto()
    OPPONENT = auto()

class TakeTurn:

    def __init__(self, opp_move, my_move):
        self.opp_move = opp_move
        self.my_move = my_move

    def get_winner():
        if self.opp_move == self.my_move:
            return Player.NIL()
        elif self.my_move ==  Move.ROCK() && self.opp_move == Move.SCISSORS():
            RETURN Player.ME()
        elif self.my_move ==  Move.SCISSOR() && self.opp_move == Move.PAPER():
            return Player.ME()
        elif self.my_move ==  Move.PAPER() && self.opp_move == Move.SCISSOR():
            return Player.ME() 
        else:
            return Player.OPPONENT()


    def get_score(self)-> (int,int) :
        my_score = 0
        opponent_score = 0

        if get_winner() == Player.ME():
            my_score += 6 

        elif get_winner() == Player.OPPONENT():
            opponent_score += 6 
        else:
            my_score += 3 
            opponent_score += 3  

        if self.my_move == Move.ROCK():
            my_score += 1 
        elif self.my_move == Move.PAPER():
            my_score += 2 
        else:
            my_score += 3

        if self.opp_move == Move.ROCK():
            opp_score += 1 
        elif self.opp_move == Move.PAPER():
            opp_score += 2 
        else:
            opp_score += 3

        return (my_score, opponent_score) 

def main():
    print("hello world")

if __name__=="__main__":
    main()

