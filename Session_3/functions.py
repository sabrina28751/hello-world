# example_class_code = 'itec 1234'
# uppercase_class_code = example_class_code.upper()
# print(f'The class code in uppercase is {uppercase_class_code}')



# email = 'SABRINAW28751@GMAIL.COM'
# lowercase_email = email.lower()
# print(f'The email in lowercase is {lowercase_email}')


# def hello_world():  
#     print('Hello')


# hello_world()
# hello_world()
# hello_world()

def secret_message():
    return 'TOP SECRET MESSAGE'

def print_secret_message():
    get_secret_message = secret_message()
    print(get_secret_message)

def greeting(name):
    message = f'Hello {name}!'
    return message
# when you call the function, you get a value back

def main():
    username = 'Zoe'
    hello_message = greeting(username)
    print(hello_message)

main()

print_secret_message()