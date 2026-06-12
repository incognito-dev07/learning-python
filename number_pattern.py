def number_pattern(n):
  if not isinstance(n, int):
    return "Argument must be an integer value."
  elif n < 1:
    return "Argument must be an integer greater than 0"
  else:
    result = []
    for i in range(n):
      result.append(f"{n+1}")
    return result
    
print(number_pattern(4))