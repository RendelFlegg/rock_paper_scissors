import random

dictionary = {'rock': {'win': 'scissors', 'lose': 'paper'},
              'paper': {'win': 'rock', 'lose': 'scissors'},
              'scissors': {'win': 'paper', 'lose': 'rock'}}

user_move = input()
computer_move = random.choice(list(dictionary.keys()))

if user_move == computer_move:
    print(f'There is a draw ({user_move})')
else:
    if dictionary[user_move]['lose'] == computer_move:
        print('Sorry, but the computer chose', computer_move)
    else:
        print(f'Well done. The computer chose {computer_move} and failed')
