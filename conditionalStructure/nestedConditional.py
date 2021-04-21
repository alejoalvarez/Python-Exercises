# This is a basic example with nested conditional
# convert the currency to dollar


def exchanges(currency, quantity):
    result = 0
    # Chilean currency
    if currency == 1:
        result = quantity * 0.0013
        print(f' The {quantity} is equivalent to {result} dollars')
    # Colombian currency
    elif currency == 2:
        result = quantity * 0.0027
        print(f'The {quantity} is equivalent to {result} dollars')
    elif currency == 3:
        result = quantity * 0.014
        print(f'The {quantity} is equivalent to {result} dollars')
    # Mexican currency
    else:
        print("Enter only the list numbers ([1],[2],[3],[4])")


if __name__ == '__main__':
    try:
        currency = int(input('''Enter the currency index you want to convert to dollar:
        [1] -> Chilean currency to dollar
        [2] -> Colombian currency to dollar
        [3] -> Argentina currency to dollar
        [4] -> Mexican currency to dollar
Choose an option: '''))
        print('************')
        quantity = int(input("Enter the amount you want to convert: "))
        exchanges(currency, quantity)
    except:
        print('****** ERROR ******')
        print('Please, only enter numeric values ')