def get_hello_message():
    name = input("What's your name? ")
    if not name:
        name = "World"
    return f'Hello, {name}!'


def say_hello():
    message = get_hello_message()
    print(message)


say_hello()
