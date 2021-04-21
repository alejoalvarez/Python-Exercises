# This is an example about functions with optional parameters


def put_percent(title, character="%"):
    print(title)
    print(character * len(title))
    print("Goodbye")


if __name__ == '__main__':
    put_percent("Test functions wih optional parameter")
