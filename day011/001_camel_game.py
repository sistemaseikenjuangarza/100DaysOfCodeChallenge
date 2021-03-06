# -*- coding: utf-8 -*-

import random

def run():
    done = False
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_distance = -20
    drinks_in_canteen = 5
    random_number = 0

    print('''
    Welcome to Camel!

    You have stolen a camel to make your way across the great Mobi desert.
    The natives want their camel back and are chasing you down! Survive your
    desert trek and out run the natives.''')

    while done == False:
        print('''
        [A.] Drink from your canteen.
        [B.] Ahead moderate speed.
        [C.] Ahead full speed.
        [D.] Stop for the night.
        [E.] Status check.
        [Q.] Quit.
        ''')

        if thirst > 4:
            print('You\'re thirsty!')
        elif thirst > 6:
            print('You died of thirst :(')
            print('G A M E  O V E R')
            done = True

        if camel_tiredness > 5:
            print('The camel is getting tired!')
        elif camel_tiredness > 8:
            print('Your camel is dead!...')
            print('G A M E  O V E R')
            done = True

        if natives_distance >= miles_traveled:
            print('You were caugth by the natives!')
            print('G A M E  O V E R')
            done = True
        elif natives_distance >= miles_traveled - 15:
            print('The natives are getting close!')

        if miles_traveled >= 250 and camel_tiredness <= 8 and thirst <= 6:
            print('You escaped from the natives!')
            print('A WINNER YOU ARE!')
            done = True

        user_choice = str(raw_input('\nChoose an option: '))
        print('')

        if user_choice.upper() == 'Q':
            done = True
            print('You just quit the game')
        elif user_choice.upper() == 'E':
            print('''
            Miles traveled:  {}
            Drinks in canteen:  {}
            The natives are {} miles behind you.
            '''.format(miles_traveled, drinks_in_canteen, natives_distance))
        elif user_choice.upper() == 'D':
            camel_tiredness = 0
            random_number = random.randrange(7, 15)
            natives_distance += random_number
            print('The camel is happy!')
        elif user_choice.upper() == 'C':
            random_number = random.randrange(10, 21)
            miles_traveled += random_number
            thirst += 1
            camel_tiredness += random.randrange(1, 4)
            natives_distance += random.randrange(7, 15)
            print('You traveled {} miles at full speed!'.format(random_number))
        elif user_choice.upper() == 'B':
            random_number = random.randrange(5, 13)
            miles_traveled += random_number
            thirst += 1
            camel_tiredness += 1
            natives_distance += random.randrange(7, 15)
            print('You traveled {} miles at moderate speed'.format(random_number))
        elif user_choice.upper() == 'A':
            if drinks_in_canteen > 0:
                drinks_in_canteen -= 1
                thirst = 0
                print('You took a drink from the canteen...')
            else:
                print('You dont have anymore drinks...')

if __name__ == '__main__':
    run()