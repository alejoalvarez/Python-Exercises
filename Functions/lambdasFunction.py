def operate(value1, value2, fn):
    return fn(value1,value2)


result1 = operate(10, 3, lambda x1, x2: x1+x2)
print(result1)

result2 = operate(10, 3, lambda x1, x2: x1-x2)
print(result2)

print(operate(30, 10, lambda x1, x2: x1*x2))
print(operate(10, 2, lambda x1, x2: x1/x2))
