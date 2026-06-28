import random
from colorama import Fore, Style, init
init(autoreset = True)

print(f"\n{Fore.GREEN}{Style.BRIGHT}Welcome to the Number Guessing Game!")
print("-" * 45, "\nI have selected a number between 1 and 100.\nTry to guess it!", "\n" + ("-" * 45))

attempts = 0
answer = random.randint(1, 101)
while attempts < 7:
  guess = int(input(f"{Fore.CYAN}Enter your guess (1 - 100): {Fore.YELLOW}"))
  if 0 < guess < 101:
    if guess < answer:
      attempts += 1
      print(f"{Fore.RED}Too Low. Try Again! ({7 - attempts} attempts left).")
    elif guess > answer:
      attempts += 1
      print(f"{Fore.RED}Too High. Try Again! ({7 - attempts} attempts left).")
    else:
      print(f"{Fore.GREEN}Correct! You guessed the number {answer} {Fore.YELLOW}in {attempts} {Fore.GREEN}attempts")
      print("-" * 45, "\nThanks for playing!")
      break
  else:
    print(f"{Fore.RED}Invalid Input. Try Again")
