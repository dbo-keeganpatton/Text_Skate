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


def start_game():
    '''Who starts the game?'''
    if random.choice(attempt) == 'land':
        return True  # Player starts
    else:
        return False  # Computer starts


def player_attempt():
    '''Player attempt action'''
    if random.choice(attempt) == 'land':
        return True  # Landed
    else:
        return False  # Got a letter


def opponent_attempt():
    '''Computer attempt action'''
    if random.choice(attempt) == 'land':
        return True  # Landed
    else:
        return False  # Got a letter


def play():
    '''Main game loop'''
    question()
    
    player_turn = start_game()
    if player_turn:
        print("You start! (1)")
    else:
        print("I'll start! (1)")
    
    while len(game_player) < len(letters) and len(game_opponent) < len(letters):
        if player_turn:
            #print('Your turn. Set the trick!')
            input('Press Enter after setting the trick...')
            if player_attempt():
                print('Nice, you landed it!')
            else:
                print('You bailed!.')
        else:
            opponent_trick = random.choice(tricks)
            print(f"My turn. I'll try the trick: {opponent_trick}")
            if opponent_attempt():
                print('I landed it! Your turn to try the same trick.')
                if not player_attempt():
                    print('You got a letter.')
                    game_player.append(letters[len(game_opponent)])
                    print(f"Your score: {''.join(game_opponent)}")
            else:
                print("I couldn't land it. Your turn.")
        
        # Switch turns
        player_turn = not player_turn

    if len(game_player) == len(letters):
        print('You lose.')
    else:
        print('You win!')

# Start the game
play()

