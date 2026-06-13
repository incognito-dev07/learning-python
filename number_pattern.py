user_input = int(input("Enter a number: "))

def number_pattern(n):
  if not isinstance(n, int):
    return "Argument must be an integer value."
  elif n < 1:
    return "Argument must be an integer greater than 0."
  else:
    result = []
    for i in range(n):
      result.append(f"{i+1}")
    return " ".join(result)
    
print(number_pattern(user_input))