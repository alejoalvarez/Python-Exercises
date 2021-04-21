# This is an example about functions with optional parameters


def calculate_salary(name, cost_hour, amount_hour):
    salary = cost_hour * amount_hour
    print(name, " worked ", amount_hour, "and the salary was", salary)


if __name__ == '__main__':
    calculate_salary("Alejo", 1000, 8)
    calculate_salary(cost_hour=1000, amount_hour=8, name="Alejo")
    calculate_salary(amount_hour=8, name="Alejo", cost_hour=1000)
