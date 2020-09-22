def get_hello_message(name):
    if not name:
        name = "World"
    return f'Hello, {name}!'


def get_user_name():
    entered_name = input("What's your name? ")
    return entered_name.capitalize()


def say_hello():
    user_name = get_user_name()
    message = get_hello_message(user_name)
    print(message)


say_hello()
