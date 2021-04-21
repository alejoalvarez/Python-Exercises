# This is a basic example with list
# find the biggest element and least element


list = []
for number in range(5):
    try:
        value = int(input("Enter number: "))
        list.append(value)
    except:
        print("*******ERROR*******")
        print("Only enter numbers")

# Find the biggest_number
biggest_number = list[0]
for x in range(1, 5):
    if list[x] > biggest_number:
        biggest_number = list[x]

# Find the least_number
least_number = list[0]
for y in range(1, 5):
    if list[y] < least_number:
        least_number = list[y]


# Sort the list
for z in range(4):
    for x in range(4):
        if list[x] > list[x+1]:
            temp_number = list[x]
            list[x] = list[x+1]
            list[x+1] = temp_number

print("Complete list")
print(list)
print(f"The biggest number is: {biggest_number}")
print(f"The least number is: {least_number}")
print(f"The sorted list: {list}")

