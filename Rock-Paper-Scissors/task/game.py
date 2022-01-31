import random


def get_ratings(file_name):
    dictionary = {}
    with open(file_name, 'r') as ratings_file:
        temp = ratings_file.read().splitlines()
        for record in temp:
            dictionary[record.split()[0]] = int(record.split()[1])
    return dictionary


options_dictionary = {'rock': {'win': 'scissors', 'lose': 'paper'},
                      'paper': {'win': 'rock', 'lose': 'scissors'},
                      'scissors': {'win': 'paper', 'lose': 'rock'}}

ratings_dictionary = get_ratings('rating.txt')

username = input('Enter your name: ')
print(f'Hello, {username}')
user_score = 0
if username in ratings_dictionary:
    user_score = ratings_dictionary[username]

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
        if options_dictionary[user_move]['lose'] == computer_move:
            print('Sorry, but the computer chose', computer_move)
        else:
            print(f'Well done. The computer chose {computer_move} and failed')
            user_score += 100
