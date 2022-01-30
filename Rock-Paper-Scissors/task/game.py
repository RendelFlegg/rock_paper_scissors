import random

dictionary = {'rock': {'win': 'scissors', 'lose': 'paper'},
              'paper': {'win': 'rock', 'lose': 'scissors'},
              'scissors': {'win': 'paper', 'lose': 'rock'}}


while True:
    user_move = input()
    if user_move not in list(dictionary.keys()) and user_move != '!exit':
        print('Invalid input')
        continue
    if user_move == '!exit':
        print('Bye!')
        break
    computer_move = random.choice(list(dictionary.keys()))
    if user_move == computer_move:
        print(f'There is a draw ({user_move})')
    else:
        if dictionary[user_move]['lose'] == computer_move:
            print('Sorry, but the computer chose', computer_move)
        else:
            print(f'Well done. The computer chose {computer_move} and failed')
