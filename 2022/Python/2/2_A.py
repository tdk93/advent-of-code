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

    def __init__(self, my_move, opponent_move):
        self.my_move = my_move 
        self.opponent_move = opponent_move

    def get_winner(self):
        if self.opponent_move == self.my_move:
            return Player.NIL
        elif self.my_move ==  Move.ROCK and self.opponent_move == Move.SCISSOR:
            return Player.ME
        elif self.my_move ==  Move.SCISSOR and self.opponent_move == Move.PAPER:
            return Player.ME
        elif self.my_move ==  Move.PAPER and self.opponent_move == Move.ROCK:
            return Player.ME 
        else:
            return Player.OPPONENT


    def get_score(self)-> (int,int) :
        my_score = 0
        opponent_score = 0

        if self.get_winner() == Player.ME:
            my_score += 6 
        elif self.get_winner() == Player.OPPONENT:
            opponent_score += 6 
        else:
            my_score += 3 
            opponent_score += 3  

        if self.my_move == Move.ROCK:
            my_score += 1 
        elif self.my_move == Move.PAPER:
            my_score += 2 
        else:
            my_score += 3

        if self.opponent_move == Move.ROCK:
            opponent_score += 1 
        elif self.opponent_move == Move.PAPER:
            opponent_score += 2 
        else:
            opponent_score += 3

        return (my_score, opponent_score) 

def transform(x,y):
    return (player_moves_to_canonical_moves(x),player_moves_to_canonical_moves(y))

def player_moves_to_canonical_moves(x):
    if x == 'X' or x == 'A':
        return Move.ROCK
    elif x == 'Y' or x == 'B':
        return Move.PAPER
    else:
        return Move.SCISSOR


def main():
    ip = open('2_a.txt','r') 
    my_score =  0
    opponent_score = 0
    for line in ip:
        l = line.strip()
        l = l.split()
        if (len(l) > 0):
            tx = transform(l[0],l[1])
            print(tx[1],tx[0])
            tt = TakeTurn(tx[1],tx[0])
            a,b = tt.get_score()
            my_score += a
            opponent_score += b
    print(my_score)

if __name__=="__main__":
    main()

