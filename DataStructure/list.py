# Concat
a = [1, 2]
b = [7, 8]
print(a + b) #-->  [1,2,7,8]

# Increase the same list
a = [1, 7]
print(a * 2) #--> [1,7,1,7]

# Add element to final list
a = [1, 2]
a.append(7)
print(a) #--> [1,2,7]

# Delete element to final list
a = [1, 7]
b = a.pop()
print(a) #--> [1]

# Delete element by position
a = [3, 7, 8]
b = a.pop(1)
print(a) # --> [3,8]

# Delete element by value
a = [4, 6, 8]
a.remove(6)
print(a) # --> [4,8]

# Sort list smallest to largest
a = [3, 8, 1]
a.sort()
print(a) #--> [1,3,8]

# List creation in a certain range
a = (list(range(0, 10, 2))) # Create a count from 0 until 10 (plus 2)
print(a) # --> [0,2,,4,6,8]

# List size value
a = [0, 2, 4, 6, 8]
print(len(a)) # --> 5

# nested list
list = [[1, 2, 3], [4, 5, 6], [10, 11, 12]]
print(list)