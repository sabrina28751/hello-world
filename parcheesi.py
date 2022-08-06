import random

turn = ["Green", "Red", "Yellow", "Blue"]
line = ''
beginning_player = ''
current_player = int()

while beginning_player != 'green' and beginning_player != 'red' and beginning_player != 'yellow' and beginning_player != 'blue':
    beginning_player = input('Please enter either Yellow, Green, Red, or Blue: ').lower()

if beginning_player == 'green':
    current_player = 0
if beginning_player == 'red':
    current_player = 1
if beginning_player == 'yellow':
    current_player = 2
if beginning_player == 'blue':
    current_player = 3


want_to_quit = ''
doubles = 2
underline = '-------------------------------------------------'
snake_eyes = 0

while not want_to_quit:
    # dice_value1 = random.randint(1, 6)
    # dice_value2 = random.randint(1, 6)
    dice_value1 = 2
    dice_value2 = 2
    print('')
    print(underline)
    input(f'{turn[current_player]} press enter to roll')
    print(underline)
    print(f'You rolled a {dice_value1} and a {dice_value2}')

    if dice_value1 == 1 and dice_value2 == 1:
        snake_eyes += 1
        print(f'snake eyes count: {snake_eyes}')

        if snake_eyes == 3:
            print('you rolled 3 snake eyes, you automatically win!')
            quit('Game Over')



    if dice_value1 == dice_value2:

        doubles = doubles + 1
        print(f'double count: {doubles}')
        print('')

        if doubles == 3 and snake_eyes >= 1:
            print('Sorry, return your farthest player back home')
            print('BUT YOU CAN STILL ROLL FOR SNAKE EYES!!')
            continue

        if doubles == 3:
            print('')
            print('Return your farthest player back to home!')
            print('')
            print('Next player\'s turn to roll.')
            print('')
            doubles = 0
            current_player += 1
            if current_player > 3:
                current_player = 0

        else:
            print('Both dice are the same. You get another roll. ')
            print('')


    else:
        # want_to_quit = input('Next player\'s turn to roll. Please press enter to roll again. ')
        print('')
        # want_to_quit = input('Please press enter to roll. ')
        print('')
        doubles = 0
        snake_eyes = 0
        current_player += 1
        if current_player > 3:
            current_player = 0

