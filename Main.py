#global variables




#game board
board=["-","-","-",
       "-","-","-",
       "-","-","-"]

#if game is still going
game_still_going=True

#who won? or tie?
winner=None

#whos turn is it
current_player="X"


def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])




def play_game():

#display initial board
   display_board()

   while game_still_going:
       handle_turn(current_player)

       check_if_game_over()

       
       flip_player()
       


   #the game has ended
   if winner=="X" or winner=="O":
       print(winner+" won.")
   elif winner==None:
       print("Tie.")


def handle_turn(player):
    position=input("Choose a position from 1-9: ")
    position=int(position)-1
    board[position]="X"
    display_board()



def check_if_game_over():
    check_for_win()
    check_if_tie()

def check_for_win():

    return

def check_if_tie():
    return

def flip_player():
    return

play_game()