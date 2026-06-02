fruits = ["apple", "orange", "mango", "pawpaw"]

list(fruits[1]) # converts a string to list
len(fruits) # finds the length of a list
del fruits[3] # deletes the elements at an index
"mango" in fruits # checks if an element exists"

# Unpacking values from a list
user = ["Incognito", 19, "SEN/25/1497"]
name, age, matric = user
print(name, age, matric)

# Collecting remaining values
name, *rest = user
print(rest) # prints a list of the remainder

# NB: List slicing works the same way as string slicing


numbers = [1, 2, 3, 4, 5]
remaining = [7, 8, 9]; idx = 3
numbers.append(6) # adds an element to the end
numbers.extend(remaining) # joins two lists
numbers.insert(idx, 10) # adds element at an index
numbers.remove(10) # removes a particular element
numbers.pop(-1) # removes ekement at an index

print(numbers)