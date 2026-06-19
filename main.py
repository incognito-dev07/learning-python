import random
import sys
import time

class RPSGame:
  def __init__(self):
    self.player_wins = 0
    self.bot_wins = 0
    self.options = ["rock", "paper", "scissors"]
    self.shortcuts = {"r": "rock", "p": "paper", "s": "scissors"}
    self.winning_pairs = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]

  # Game Logic
  def start_game(self):
  player = input("Enter your choice (r/p/s): ").lower()
  player = shortcuts.get(player)
  bot = random.choice(options)
  
  if player == None:
    print("Invalid Input. Try again!")
  elif (player, bot) in winning_pairs:
    player_wins += 1
    display_choices(player, bot)
    print("Congrats. You win!")
  elif player == bot:
    display_choices(player, bot)
    print("It's a Tie Game")
  else:
    bot_wins += 1
    display_choices(player, bot)
    print("Bot Wins. Try again!")

# Check Score History
  def check_history(self):
    print("\nSCORE HISTORY")
    print(f"Player Wins: {self.player_wins} \nBot Wins: {self.bot_wins}")
  
# Utility Functions
def display_choices(player, bot):
  print(f"\nYour Choice: {player.capitalize()} \nBot Choice: {bot.capitalize()}")
  time.sleep(0.5)
 
  # Main Entry Point 
  def run(self):
    while True:
      print("\nROCK PAPER SCISSORS")
      print("1. Start Game")
      print("2. Check History")
      print("3. Exit")
      choice = input("Choose an option (1 - 3): ")
  
      if choice == "1":
        while True:
        play_game()
        if input("\nPlay again? (y/n): ") != "y":
          break
      elif choice == "2":
        check_history()
      elif choice == "3":
        sys.exit("\nThanks for playing the game")
      else:
        print("Invalid option. Try again!")
        
if __name__ == "__main__":
  RPSGame.run()




# Ternary Operator
# name = "Incognito"
# age = 119
# print(f"Welcome, {name}") if age >= 18 else print("Access Denied")