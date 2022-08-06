# If the condition is True, the code inside the block "while" repeats until the condition is False.
# Keeps on printing "Hello" because it is True, no False to stop it.
# while True:
#     print('Hello')

# import random
# want_to_quit = ''
# while not want_to_quit:
#     dice_value = random.randint(1, 6)
#     print(f'You rolled a {dice_value}')
#     want_to_quit = input('Press enter to roll again, any other key to quit: ')

# weather = 'snow'
# temperature = 29.5
# day_of_month = 20
# print(f'On January {day_of_month}, the temperature is {temperature} and the current weather is {weather}.')


# number_of_dice = 2
# print(f'About to roll {number_of_dice} dice...')
# for dice in range(number_of_dice):
#     dice_value = random.randint(1,6)
#     print(dice_value)

import random

want_to_quit = ''
while not want_to_quit:
    number_of_dice = 2
    print(f'About to roll {number_of_dice} dice...')
    dice_value1 = random.randint(1, 6)
    dice_value2 = random.randint(1, 6)
    print(f'You rolled a {dice_value1} and a {dice_value2}')
    if dice_value1 == dice_value2:
        want_to_quit = input('Congratulations, both dice are the same. You get another turn. Press enter to get your free roll. ')
    else:
        want_to_quit = input('Press enter to roll again, any other key to quit: ')
