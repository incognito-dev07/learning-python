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
    
  def get_player_choice(self):
    while True:
      choice = input("\nEnter your choice (r/p/s): ").lower()
      if choice in self.shortcuts:
        return self.shortcuts[choice]
      else:
        print("Invalid Input. Try again!")

  def play_round(self):
    player = self.get_player_choice()
    bot = random.choice(self.options)
    print(f"\nYour Choice: {player.capitalize()} \nBot Choice: {bot.capitalize()}")
    time.sleep(0.5)
  
    if (player, bot) in self.winning_pairs:
      self.player_wins += 1
      print("You win. Congratulations!")
    elif player == bot:
      print("It's a Tie Game")
    else:
      self.bot_wins += 1
      print("Bot Win. Try again!")

  def check_history(self):
    print("\n\033[1mSCORE HISTORY\033[0m")
    print(f"Player Wins: {self.player_wins} \nBot Wins: {self.bot_wins}")
 
  # Main Entry Point 
  def run(self):
    while True:
      print("\n\033[1mROCK PAPER SCISSORS\033[0m")
      print("1. Start Game")
      print("2. Check History")
      print("3. Exit")
      choice = input("Choose an option (1 - 3): ")
  
      if choice == "1":
        while True:
          self.play_round()
          if input("\nPlay again? (y/n): ").lower() != "y": break
      elif choice == "2":
        self.check_history()
      elif choice == "3":
        sys.exit("\nThanks for playing the game")
      else:
        print("Invalid option. Try again!")
        
if __name__ == "__main__":
  RPSGame().run()
