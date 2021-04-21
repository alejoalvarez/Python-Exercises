# This is an example about functions variable arguments


def add_numbers(value1, value2, *several):
    result = value1 + value2
    for x in range(len(several)):
        result = result + several[x]
    return result


def show_message():
    print("Add two numbers")
    print(add_numbers(1, 2))
    print("Add n numbers")
    print(add_numbers(2, 5, 8, 3))


if __name__ == '__main__':
    show_message()
