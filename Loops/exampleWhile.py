# This is a basic example with while (valid potency de 2 )


def run():
    LIMIT = 1000
    counter = 0
    potency_2 = 2**counter
    while potency_2 < LIMIT:
        print(f'2 elevated to {counter} is equal to {potency_2}')
        counter = counter + 1
        potency_2 = 2**counter


if __name__ == '__main__':
    run()
