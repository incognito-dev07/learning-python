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
      print("Too high. Try again")
    elif user_input < answer:
      print("Too low. Try again")
    print(f"{5 - attempts} attempts left)\n")
  