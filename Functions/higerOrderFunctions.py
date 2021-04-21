def operate(value1, value2, fn):
    return fn(value1, value2)


def add(x1, x2):
    return x1 + x2


def subtract(x1, x2):
    return x1 - x2


def multiply(x1, x2):
    return x1 * x2


def divide(x1, x2):
    return x1 / x2


result1 = operate(10, 3, add)
print(result1)

result2 = operate(8, 30, subtract)
print(result2)

print(operate(30, 10, multiply))
print(operate(10, 2, divide))
