import random
import pandas as pd

tricks = pd.read_csv('flip_tricks.csv').values.tolist()
success = open('board.txt').read()
failure = open('broken_brd.txt').read()
ask_to_play = open('opponent.txt').read()


game_player = []
game_opponent = []
letters = ['S', 'K', 'A', 'T', 'E']
attempt = ['land', 'bail']

def question():
    '''Ask to play, terminate the program if no (n)'''
    ask_player = input('(y/n)\n')
    if ask_player.lower() == 'y':
        print('Sick!')
    else:
        print('Ok maybe next time!')
        exit()

def action():
    if random.choice(attempt) == 'land':
        return True  
    else:
        return False  


def play():
    '''Main Program'''
    print(ask_to_play)
    question()
    
    current_turn = action()  # Who sets, True for Player

    while len(game_player) < len(letters) and len(game_opponent) < len(letters): 
        
        if current_turn:  # Player turn
            input("Set the Trick: (Type Trick)   \n")
            player_action = action()
            if player_action:
                print(success)
                print("Stomped it! \nCPU tries the trick")
                cpu_action = action()
                if cpu_action:
                    print("CPU Lands your trick")
                else:
                    print("CPU gets a letter")
                    game_opponent.append(letters[len(game_opponent)])
                    print(f'CPU Score: {game_opponent}')
            else:
                print(failure)
                print("You bailed")
                current_turn = not current_turn
            
        else:  # CPU turn

            print("CPU sets the Trick:  \n")
            cpu_action = action()
            if cpu_action:
                print(f"CPU lands a {random.choice(tricks)}")
                input("( Type trick CPU does to attempt ) ...\n")
                player_action = action()
                if player_action:
                    print("You Landed it")
                else:
                    print("You get a letter")
                    game_player.append(letters[len(game_player)])
                    print(game_player)
            else:
                print("CPU bails trick")
                current_turn = not current_turn  # Change turn to Player


    if len(game_player) == len(letters):
        print("You Lose")
        exit()

    if len(game_opponent) == len(letters):
        print("You Win!")
        exit()

play()
