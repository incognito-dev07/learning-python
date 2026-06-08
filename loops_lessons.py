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

