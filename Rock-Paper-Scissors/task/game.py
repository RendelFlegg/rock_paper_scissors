dictionary = {'rock': {'win': 'scissors', 'lose': 'paper'},
              'paper': {'win': 'rock', 'lose': 'scissors'},
              'scissors': {'win': 'paper', 'lose': 'rock'}}

user_input = input()
print('Sorry, but the computer chose', dictionary[user_input]['lose'])
