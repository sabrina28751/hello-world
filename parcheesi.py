# import random
# #
# # number_of_dice = int(input('How many dice to roll? '))
# # print(f'About to roll {number_of_dice} dice...')
# # for dice in range(number_of_dice):
# #     dice_value = random.randint(1,6)
# #     print(dice_value)

import random

# want_to_quit = ''
# doubles = 1
# while not want_to_quit:
#     number_of_dice = 2
#     # dice_value1 = random.randint(1, 6)
#     # dice_value2 = random.randint(1, 6)
#     dice_value1 = 1
#     dice_value2 = 1
#     print(f'You rolled a {dice_value1} and a {dice_value2}')
#     if dice_value1 == dice_value2 and doubles != 3:
#         want_to_quit = input('Both dice are the same. You get another turn. ')
#         doubles = doubles + 1
#         print('')
#         if doubles == 3:
#             print('')
#             print('Return your farthest player back to home!')
#
#     else:
#         want_to_quit = input('Next player\'s turn to roll. Please press enter to roll again. ')
#         print('')
#         doubles = 1


# want_to_quit = ''
# doubles = 1
# underline = '-------------------------'
# while not want_to_quit:
#     number_of_dice = 2
#     # dice_value1 = random.randint(1, 6)
#     # dice_value2 = random.randint(1, 6)
#     dice_value1 = 1
#     dice_value2 = 1
#     print('')
#     print(f'You rolled a {dice_value1} and a {dice_value2}')
#     print('')
#     if dice_value1 == dice_value2 and doubles != 3:
#         want_to_quit = input('Both dice are the same. You get another turn. ')
#         print(underline)
#         doubles = doubles + 1
#         print('')
#         if doubles == 3:
#             print('')
#
#     else:
#         print('Return your farthest player back to home!')
#         want_to_quit = input('Next player\'s turn to roll. Please press enter to roll again. ')
#         print(underline)
#         doubles = 1


# want_to_quit = ''
# doubles = 1
# underline = '-------------------------'
# snake_eyes = 1
# while not want_to_quit:
#     number_of_dice = 2
#     dice_value1 = random.randint(1, 6)
#     dice_value2 = random.randint(1, 6)
#     # dice_value1 = 2
#     # dice_value2 = 2
#     print('')
#     print(f'You rolled a {dice_value1} and a {dice_value2}')
#     print('')
#     if dice_value1 == 1 and dice_value2 == 1:
#         snake_eyes = snake_eyes + 1
#         if doubles == 3:
#             print('CONGRATULATIONS, YOU JUST WON THE GAME!!' )
#
#     if dice_value1 == dice_value2 and doubles != 3:
#         want_to_quit = input('Both dice are the same. You get another turn. ')
#         print(underline)
#         doubles = doubles + 1
#         print('')
#         if doubles == 3:
#             print('')
#             print(f'You rolled a {dice_value1} and a {dice_value2}')
#             print('')
#             print('Return your farthest player back to home!')
#             want_to_quit = input('Next player\'s turn to roll. Please press enter to roll again. ')
#             print(underline)
#             doubles = 1

# want_to_quit = ''
# doubles = 1
# underline = '-------------------------------------------------'
# while not want_to_quit:
#     number_of_dice = 2
#     dice_value1 = random.randint(1, 6)
#     dice_value2 = random.randint(1, 6)
#     # dice_value1 = 2
#     # dice_value2 = 2
#     print(f'You rolled a {dice_value1} and a {dice_value2}')
#     print('')
#     if dice_value1 == dice_value2 and doubles != 3:
#         want_to_quit = input('Both dice are the same. You get another turn. ')
#         print(underline)
#         doubles = doubles + 1
#         print('')
#     elif doubles == 3:
#         print('Return your farthest player back to home!')
#         print('Next player\'s turn to roll. ')
#         print('')
#         print(underline)
#         want_to_quit = input('Please press enter to roll. ')
#         print(underline)
#         print('')
#         doubles = 1
#
#     else:
#         doubles = 1


want_to_quit = ''
doubles = 0
underline = '-------------------------------------------------'
while not want_to_quit:
    # dice_value1 = random.randint(1, 6)
    # dice_value2 = random.randint(1, 6)
    dice_value1 = 1
    dice_value2 = 1
    print(underline)
    print(f'You rolled a {dice_value1} and a {dice_value2}')
    if dice_value1 == dice_value2:
        doubles = doubles + 1
        print(f'double count: {doubles}')
        print('')
        if doubles == 3:
            print('')
            print('Return your farthest player back to home!')
            print('')
            want_to_quit = input('Next player\'s turn to roll. Please press enter to roll again. ')
            print('')
            doubles = 0
        else:
            want_to_quit = input('Both dice are the same. You get another roll. ')
            print('')


    else:
        # want_to_quit = input('Next player\'s turn to roll. Please press enter to roll again. ')
        print('')
        want_to_quit = input('Please press enter to roll. ')
        print('')
        doubles = 0
