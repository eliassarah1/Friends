from data import data
from logo import logo, test
import random
import os

mod_data = data

# clear = lambda: os.system('clear')
# clear()

choosed_phrases = []
score = 0
level = 0

print('\nWelcome To FRIENDS Game......\n')

# choosing the level
# while level == 0:
#
#     print(logo)
#     difficulty = input('Please choose your difficulty, Easy / Medium / Hard:\n').lower()
#     if difficulty == 'easy' or difficulty == 'e':
#         level = 1
#     elif difficulty == 'medium' or difficulty == 'm':
#         level = 2
#     elif difficulty == 'hard' or difficulty == 'h':
#         level = 3
#     else:
#         # clear()
#         print('Difficulty level not set...')

game_on = True
while game_on:
    choosed_phrase = random.choice(mod_data)

    while choosed_phrase['number'] in choosed_phrases:
        choosed_phrase = random.choice(mod_data)
    choosed_phrases.append(choosed_phrase['number'])
    if len(choosed_phrases) >= len(mod_data) :
        game_on = False


print(choosed_phrases)
print(len(mod_data))
print('no more phrases')


    # if level == 1:
    #     print('Who Said This:...')
    #     break
    #
    #
    #
    # elif level == 2:
    #     print('Difficulty : Medium... ')
    #     break
    #
    #
    #
    # elif level == 3:
    #     print('Difficulty : Hard... ')
    #     break


