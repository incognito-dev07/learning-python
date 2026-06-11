for i in range(1, 11):
  print(i)
  
even_nums = list(range(0, 21, 2))
print(even_nums)
print("\n")


# Enumerate Function
usernames = ["Klaus", "Elijah", "Rebeccah", "Kol", "Freya", "Finn"]
enums = list(enumerate(usernames))
print(enums)

for idx, name in enumerate(usernames, 1):
  print(f"{idx}. {name}")
print("\n")
  
# Zip Function
developers = ["Naomi", "Tom", "Jessica", "Ben"]
ages = [18, 19, 16, 21]
zipped = list(zip(developers, ages))
print(zipped)

for name, age in zip(developers, ages):
  print(f"Name: {name} — Age: {age}")
print("\n")
  
# List Comprehension
even = [num for num in range(21) if num % 2 == 0]
print(even)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_odd = [(num, "even") if num % 2 == 0 else (num, "odd") for num in numbers]
print(even_odd)

# Anonymous Functions (lambda)
letters = ["a", "b", "c", "d"]
for char in letters:
  print((lambda x: x.upper())(char))

# Filter Functions
words = ["tree", "sky", "river", "mountain", "cloud", "sun"]
short_words = list(filter(lambda x: len(x) > 4, words))
print(short_words)

# Map Function
single = [1, 2, 3, 4, 5]
tripled = list(map(lambda x: x * 3, single))
print(tripled)