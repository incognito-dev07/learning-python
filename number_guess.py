import random

answer = random.randint(0, 100)
attempts = 0

while attempts < 7:
  user_input = int(input("Guess the number (1 - 100): "))
  if user_input == answer:
    print(f"Correct: The result is {user_input}")
    break
  else:
    attempts += 1
    if user_input > answer:
      print(f"{user_input} is too high!")
    elif user_input < answer:
      print(f"{user_input} is too low!")
    print(f"Try again! {7 - attempts} attempts left\n")
print(f"The correct number is {answer}")
  