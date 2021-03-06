#Function used to display the Board
from IPython.display import clear_output
def display_board(board):
    clear_output() # Remember, this only works in jupyter!
    print("      |"+"      |")
    print(board[7]+"     |"+board[8]+"     |"+board[9])
    print("      |"+"      |")
    print("-------------------")
    print("      |"+"      |")
    print(board[4]+"     |"+board[5]+"     |"+board[6])
    print("      |"+"      |")
    print("-------------------")
    print("      |"+"      |")
    print(board[1]+"     |"+board[2]+"     |"+board[3])
    print("      |"+"      |")


#Function used to check  win or tie
def win_check(board,mark):
     return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


#Function used to take input marker "X" or "O"
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


#Function used to place the marker into the selected position in Board list
def place_marker(board, marker, position):
    board[position] = marker


#Function used to generate random turn of the players
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


#Function used to check selected position is empty or not
def space_check(board, position):
        return board[position]==' '


#Function used to check the board is full or not
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


#Funtion used to take input position
def player_choice(board):
    choise="wrong"
    space=False
    new_board=['1','2','3','4','5','6','7','8','9']
    while choise not in new_board or choise.isdigit()==False or space==False:
        choise=input("Enter a the position between 1 to 9: ")
        if choise not in new_board:
            print("Please enter valid position between 1 to 9: ")
        space=space_check(theBoard,int(choise))
        if space==False:
            print(f"Entered position {choise} is already choosen")
        else:
            space==True
            
    return int(choise) 


#Funtion used to ask for replay
def replay():
    play=input("Want to play again press [Y/N]: ")
    if play.upper()=='Y':
        return True
    else:
        return False




print('Welcome to Tic Tac Toe!')
#Using While loop to call all this funtions 
while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    print(f"Player 1's marker is: { player1_marker}\nPlayer 2's marker is: {player2_marker}")
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! Player 1 have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations! Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
