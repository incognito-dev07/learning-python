greeting = "Hello world"

# string slicing
second_word = greeting[6:]
step_slicing = greeting[0:5:2]
print(step_slicing)

reverse_second_word = second_word[::-1]
print(reverse_second_word)

# string methods
text = "Hello world"
text.upper() # converts to upper case
text.lower() # converts to lower case
text.strip() # removes whitespaces
text.replace(old, new) # replaces old with new
text.split(seperator) # splits into list


print(text.split(" "))