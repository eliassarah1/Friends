from data import deck_one, deck_two, logo
import random
import os

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False



print('\nWellcome To Cups..............')
print(logo)

full_deck = deck_one + deck_two
plyr_one = [0, 1]
plyr_two = [0, 1]
plyr_one_total = 0
plyr_two_total = 0
bid = 0

game_on = True
while game_on:
    # Continue to play
    for i in range(2):

        x = input('how much you want to bid? Use Whole Numbers Only:\n')
        os.system('cls')
        print(logo)
        while not x.isdigit():
            x = input('Pls use whole numbers only:\n')
        bid += int(x)
        # Deal the cards
        # first guy
        card11 = random.choice(full_deck)
        plyr_one[0] = card11
        full_deck.remove(card11)
        card12 = random.choice(full_deck)
        plyr_one[1] = card12
        full_deck.remove(card12)
        card11_name = card11['card_name']
        card12_name = card12['card_name']
        card11_type = card11['card_type']
        card12_type = card12['card_type']
        print((f'Your cards are:  \n{card11_name} of {card11_type} ...and... {card12_name} of {card12_type}'))

        # second guy
        card21 = random.choice(full_deck)
        plyr_two[0] = card21
        full_deck.remove(card21)
        card22 = random.choice(full_deck)
        plyr_two[1] = card22
        full_deck.remove(card22)
        card21_name = card21['card_name']
        card22_name = card22['card_name']
        card21_type = card21['card_type']
        card22_type = card22['card_type']
        print((f'Opponent cards are:  \n{card21_name} of {card21_type} ...and... {card22_name} of {card22_type}'))

        plyr_one_total = plyr_one[0]['value'] + plyr_one[1]['value']
        plyr_two_total = plyr_two[0]['value'] + plyr_two[1]['value']

       # D-cup and Full-cup check
        def d_cup_1():
            if plyr_one[0]['value'] == 11 and plyr_one[1]['value'] == 8 or plyr_one[1]['value'] == 11 and plyr_one[0][
                'value'] == 8:
                return True
        def d_cup_2():
            if plyr_two[0]['value'] == 11 and plyr_two[1]['value'] == 8 or plyr_two[1]['value'] == 11 and plyr_two[0][
                'value'] == 8:
                return True
        def full_cup_1():
            if plyr_one[0]['value'] == 10 and plyr_one[1]['value'] == 5 or plyr_one[1]['value'] == 10 and plyr_one[0][
                'value'] == 5:
                return True
        def full_cup_2():
            if plyr_two[0]['value'] == 10 and plyr_two[1]['value'] == 5 or plyr_two[1]['value'] == 10 and plyr_two[0][
                'value'] == 5:
                return True

        if  plyr_one_total == plyr_two_total:
            print('stiting down bounace....')
        elif d_cup_1() == True and d_cup_2() != True:
            print('player 1 wins with D-Cup')
        elif d_cup_1() != True and d_cup_2() == True:
            print('player 2 wins with D-Cup')
        elif full_cup_1() == True and full_cup_2() != True:
            print('player 1 wins with full-Cup')
        elif full_cup_1() != True and full_cup_2() == True:
            print('player 2 wins with full-Cup')
        else:
            if plyr_one_total > plyr_two_total:
                print('player 1 win ...')
            else:
                print('player 2 wins...')
        if len(full_deck) == 0:
            game_on = False