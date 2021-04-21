# Define several tuples
tuple1 = (1, 2, 3)
print(tuple1)


tuple2 = (25, "December", 1000)
print(tuple2)


def load_date():
    day = int(input("Enter the day: "))
    month = int(input("Enter the month: "))
    year = int(input("Enter the year: "))
    return day, month, year


def print_date(date):
    print(date[0], date[1], date[2], sep="/")


# main block
date1 = load_date()
print_date(date1)
