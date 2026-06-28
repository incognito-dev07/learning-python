# String Functions
text = "Incognito is Peak"
len(text) # returns the total string length
str(text) # converts any data type to string

print(text.count(""))


# String Methods
sign = " "; old = "Peak"; new = "Fire"
text.count("") # returns how often a word appears
text.split(sign) # splits a string into word list
# text.upper() # converts string to upper case
# text.lower() # converts string to lower case
# text.replace(old, new) # replaces old with new
# 
# text.startswith(pre) # checks the first char
# text.endswith(suff) # checks if it's last char
# text.find("") # returns idx of first occurence
# 
# text.isupper() # checks if all char is uppercase
# text.islower() # checks if all char is lowercase
# text.capitalize() # makes first letter uppercase
# text.title() # makes first char of each word upper
# text.strip() # removes whitespaces
# # lstrip() and rstrip() removes spaces from left and right respectively

# print(text.capitalize())





# String Slicing
# greeting = "Hello world"

# second_word = greeting[6:]
# step_slicing = greeting[0:5:2]
# print(step_slicing)

# reverse_second_word = second_word[::-1]
# print(reverse_second_word)




# 1. Clean Phone Number
phone = "+49 (176) 123-4567"
phone = phone.replace("+", "").replace("-", "")
phone = phone.replace("(", "").replace(")", "")
print(phone.replace(" ", ""))

# 2. 