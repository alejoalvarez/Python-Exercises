# This is a basic example with for (Table for a number)


def table_number():
    try:
        number = int(input("Enter number to calculate: "))
        end = int(input("Enter the final number to calculate: "))
        number_final = range(1, end + 1)
        print(number_final)
        for counter in number_final:
            print(f'{number} * {counter} = {counter * number}')
    except:
        print("**** Error ****")
        print("Only enter numbers")


if __name__ == '__main__':
    table_number()

