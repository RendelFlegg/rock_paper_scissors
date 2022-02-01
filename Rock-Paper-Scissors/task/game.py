import random


def get_ratings(file_name):
    dictionary = {}
    with open(file_name, 'r') as ratings_file:
        temp = ratings_file.read().splitlines()
        for record in temp:
            dictionary[record.split()[0]] = int(record.split()[1])
    return dictionary


def get_options(options_list):
    dictionary = {}
    number = len(options_list) // 2
    extra_options = options_list * 3
    for idx, option in enumerate(options_list):
        extra_idx = idx + len(user_options)
        win_list = extra_options[extra_idx - number:extra_idx]
        lose_list = extra_options[extra_idx + 1:extra_idx + 1 + number]
        dictionary[option] = {'win': win_list, 'lose': lose_list}
    return dictionary


options_dictionary = {'rock': {'win': ['scissors'], 'lose': ['paper']},
                      'paper': {'win': ['rock'], 'lose': ['scissors']},
                      'scissors': {'win': ['paper'], 'lose': ['rock']}}

ratings_dictionary = get_ratings('rating.txt')

username = input('Enter your name: ')
print(f'Hello, {username}')
user_score = 0
if username in ratings_dictionary:
    user_score = ratings_dictionary[username]
user_options = input().split(',')
if user_options != ['']:
    options_dictionary = get_options(user_options)
print("Okay, let's start")
while True:
    user_move = input()
    if user_move not in list(options_dictionary.keys()) and user_move not in ['!exit', '!rating']:
        print('Invalid input')
        continue
    if user_move == '!exit':
        print('Bye!')
        break
    if user_move == '!rating':
        print(f'Your rating: {user_score}')
        continue
    computer_move = random.choice(list(options_dictionary.keys()))
    if user_move == computer_move:
        print(f'There is a draw ({user_move})')
        user_score += 50
    else:
        if computer_move in options_dictionary[user_move]['lose']:
            print('Sorry, but the computer chose', computer_move)
        else:
            print(f'Well done. The computer chose {computer_move} and failed')
            user_score += 100
