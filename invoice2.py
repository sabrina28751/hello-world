name_of_person = input('Enter your name: ')
number_of_years = input('Enter how many years have you been in school: ')
print(name_of_person + ' has been at school for ' + number_of_years + ' years')
print(''
      '')
number_of_times_on_bus = int(input('Enter how many times you rode the bus last month: '))
cost_of_rides = float(input('Enter what the cost is of one bus ride: '))
total_cost = number_of_times_on_bus * cost_of_rides
print('You went on the bus ' + str(number_of_times_on_bus) + ' times last month. One bus ride costs ' + str(cost_of_rides) + '. Your total cost is ' + str(total_cost))