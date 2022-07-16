# print('Quiz program!')
# answer = input('What is the capital of Wisconsin? ')  # It's Madison
# if answer != 'Madison':
#     print('Sorry, the answer is Madison.')
# else:
#     print('Correct!')

# number_of_credits = int(input('How many credits are you taking this semester? '))
# # This loop repeats while the input is invalid - the number of credits is less than 0
# while number_of_credits < 0:
#     print('Error - please enter 0 or a positive number.')
#     number_of_credits = int(input('How many credits are you taking this semester? '))
# if number_of_credits >= 6:
#     print('You are a half time student.')
# elif number_of_credits >= 12:
#     print('You are a full time student.')
# else:
#     print('You are less than a half time student.')

# quiz_score = float(input('Please enter the quiz score, out of 100: '))
# # Convert quiz score to a letter grade
# if quiz_score >= 90:
#     print('Your letter grade is an A')
# elif quiz_score >= 80:
#     print('Your letter grade is an B')
# elif quiz_score >= 70:
#     print('Your letter grade is an C')
# # Can you add another elif to check if the grade is >= 60 and print a message saying that the grade is a D
#
# else:
#     print('Sorry, you failed the quiz')

# star_id = input('Please enter your StarID: ')
# if len(star_id) == 8:
#     print('Your StarID is the correct length')
# elif len(star_id) > 8:
#     print('Your StarID is too long')
# else:
#     print('Your StarID is too short')

star_id = input('Please enter your StarID: ')
while len(star_id) != 8:
    print('Error - a valid StarID has 8 characters.')
    star_id = input('Please enter your StarID: ')
print(f'Thank you, your StarID is {star_id}')
