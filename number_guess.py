import random

answer = random.randint(0, 100)
attempts = 0

while attempts < 5:
  user_input = input("Guess the number: ")
  break