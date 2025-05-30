import re as re
import random as rn
import time

def main():
    play_game()
        
def play_game():
    player = record_player_name()
    board = start_game(player)
    someone_won = False
    turn = 0

    while turn < 9 and someone_won == False:
        if turn % 2 == 0:
            board = prompt_player_turn(board)
        else:
            board = prompt_computer_turn(board)
            # pass
        someone_won = check_for_win(board)
        if turn == 8:
            print("Draw. Nobody won.")
        turn += 1
    play_again()
    

def start_game(player):
    print("The game has started!!!")
    print("")

    board = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]
    print_board(board)
    print(f"{player}, make the first move!")
    return board

def record_player_name():
    player = input("Greetings! What is your name, player? ")
    return player

def print_board(board):
    count = 0
    for row in board:
        print("   |   |   ")
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if count < 2:
            print("___|___|___")
        else:
            print("   |   |   ")
        count += 1
    print("")

def prompt_player_turn(board):
    good_move = False
    x = ""
    y = ""
    while good_move == False:
        xy = input("Player turn (x,y): ")
        print("")
        if re.fullmatch(r'\d+,\d+?', xy):
            xy = xy.split(",")
            x = int(xy[0])
            y = int(xy[1])
            if x in range(0,3) and y in range(0,3):
                if board[y][x] == " ":
                    board[y][x] = "X"
                    good_move = True
                    print_board(board)
                    return board
                else:
                    print("The position is already taken. Try again.")
            else:
                print("Coordinates are out of range. Try again.")
        else:
            print("Invalid coordinates pattern. Try again.")

def prompt_computer_turn(board):
    time.sleep(1)
    print("Computer turn: ")
    print("")
    time.sleep(1)
    x = None
    y = None

    good_move = False
    while good_move == False:
        x = rn.randint(0,2)
        y = rn.randint(0,2)
        if board[y][x] == " ":
            board[y][x] = "O"
            good_move = True
            print_board(board)
            return board
        else:
            pass
            # print("Computer tried an existing position. It will try again")
    print()

def check_for_win(board):
    winner_combos = [
        # horizontal lines
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # vertical lines
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # diagonal lines
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    test_response = False

    for combo in winner_combos:
        if combo[0] == combo[1] == combo[2] == "X":
            print(f"Congrats, you won!")
            test_response = True
        elif combo[0] == combo[1] == combo[2] == "O":
            print("Computer won, you lost.")
            test_response = True
        else:
            pass
    return test_response

def play_again():
    play_again = ""
    while play_again != "Y" and play_again != "N":
        play_again = input("Play again? (Y/N): ").title()
        if  play_again == "Y":
            play_game()
        elif play_again == "N":
            print("Bye Bye")
        else:
            print("Bad Input")

if __name__ == "__main__":
    main()