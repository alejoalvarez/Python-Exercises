# This is an example about functions with parameters


def show_message(message):
    print(message)
    print("This example add two numbers")
    print("*****************************")


def add_numbers():
    try:
        number1 = int(input("Enter the first number to add: "))
        number2 = int(input("Enter the second number to add: "))
        result = number1 + number2
        print(f"The result to add {number1} + {number2} is: {result}")
    except:
        print("Only can introduce numbers")


def say_goodbye(message):
    print(message)
    print("*********************")


if __name__ == '__main__':
    show_message("Welcome to the example with functions")
    add_numbers()
    say_goodbye("Goodbye, see you soon")