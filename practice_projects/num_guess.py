import random
from colorama import Fore, Style

print(f"\n{Fore.GREEN}Welcome to the Number Guessing Game!")
print("-" * 45)
print("I have selected a number between 1 and 100.\nTry to guees it!")
print("-" * 45)

answer = random.randint(1, 101)
print(answer)