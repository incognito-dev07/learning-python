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
text.startswith(prefix) 
text.endswith(suffix) # returns boolean
text.find(char) # returns idx of first occurence
text.count(char) # counts total char occurence
text.isupper() # checks if all char is uppercase
text.islower() # checks if all char is lowercase
text.capitalize() # makes first letter uppercase
text.title() # makes first letter of each word uppercase

print(text.capitalize())