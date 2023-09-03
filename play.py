import random
import pandas as pd

df = pd.read_csv('flip_tricks.csv')
tricks = df.values.tolist()

game_player = []
game_opponent = []
letters = ['S', 'K', 'A', 'T', 'E']
attempt = ['land', 'bail']


def question():
    '''Ask the Player to play and terminate the program if no(n)'''
    ask_player = input('Wanna play a game of SKATE? (y/n)\n')
    if ask_player.lower() == 'y':
        print('Sick!')
    else:
        print('Ok maybe next time!')
        exit()


def action():
    '''Who starts the game?'''
    if random.choice(attempt) == 'land':
        return True  # Player starts
    else:
        return False  # Computer starts



def play():
    
    question()

    while len(game_player) < len(letters) and len(game_opponent) < len(letters):

        player_action = action()
        cpu_action = action()

        if player_action:
            input("Set the Trick: (Type Trick)   \n")
            if player_action:
                print("Stomped it! \nCPU tries the trick")
                if cpu_action:
                    print("CPU Lands your trick")
                else:
                    print("CPU gets a letter")
                    game_opponent.append(letters[len(game_opponent)])
                    print(f'CPU Score: {game_opponent}')
            else:
                print("You bailed")
        
        else:

            print("CPU sets the Trick:  \n")

            if cpu_action:
                print(f"CPU lands a {random.choice(tricks)}")
                input("( Type trick CPU does to attempt ) ...\n")
                if player_action:
                    print("You Landed it")
                else:
                    print("You get a letter")
                    game_player.append(letters[len(game_player)])
                    print(game_player)
            else:
                print("CPU bails trick")
            
                        

    if len(game_player) == len(letters):
        print("You Lose")
        exit()

    if len(game_opponent) == len(letters):
        print("You Win!")
        exit()
        

play()
