# This is an example about functions with return


def add_numbers():
    try:
        number1 = int(input("Enter the first number to add: "))
        surface = calculate_area_square(number1)
        print(f"The square's surface is: {surface}")
    except:
        print("Only can introduce numbers")


def calculate_area_square(size):
    surface = size * size
    return surface


if __name__ == '__main__':
    add_numbers()

