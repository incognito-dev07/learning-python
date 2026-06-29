import random
from colorama import Fore, Style, init
init(autoreset = True)

GR = Fore.GREEN; RD = Fore.RED
BOLD = Style.BRIGHT
CY = Fore.CYAN; YL = Fore.YELLOW

print(f"\n{GR}{BOLD}Welcome to the Number Guessing Game!")
print("-" * 45, "\nI have selected a number between 1 and 100.\nTry to guess it!", "\n" + ("-" * 45))

attempts = 0
answer = random.randint(1, 101)
while attempts < 7:
  guess = int(input(f"{CY}Enter your guess (1 - 100): {YL}"))
  if 0 < guess < 101:
    if guess < answer:
      attempts += 1
      print(f"{RD}Too Low. Try Again! ({7 - attempts} attempts left).")
    elif guess > answer:
      attempts += 1
      print(f"{RD}Too High. Try Again! ({7 - attempts} attempts left).")
    else:
      print(f"{GR}Correct! You guessed the number {answer} {YL}in {attempts} {GR}attempts")
      print("-" * 45, "\nThanks for playing!")
      break
  else:
    print(f"{RD}Invalid Input. Try Again")
