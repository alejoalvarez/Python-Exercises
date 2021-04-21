# This is an example about dictionaries
products = {"apples": 10, "grapes": 5, "bananas": 15}
print(products)


def print_message(countries):
    for key in countries:
        print(key, countries[key])


# main block
countries = {"Colombia": 40000000, "Spain": 46000000, "Brazil": 190000000, "London": 3400000}
print_message(countries)
