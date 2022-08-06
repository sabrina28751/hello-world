def main():
    string = input('PLease enter a string: ')
    repeat = int(input('How many times to repeat? '))
    result = string_repeater(string, repeat) #Function call
    print(result)

def string_repeater(text, n):
    repeated_string = text * n
    return repeated_string


main()