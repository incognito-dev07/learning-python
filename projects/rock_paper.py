import random
import sys
import time

player_wins = 0
bot_wins = 0
options = ["rock", "paper", "scissors"]
winning_pairs = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]

# Game Logic
def start_game():
  global player_wins; global bot_wins
  player = input("Enter your choice (rock/paper/scissors): ").lower()
  bot = random.choice(options)
  
  if player not in options:
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
def check_history():
  global player_wins; global bot_wins
  print("\nSCORE HISTORY")
  print(f"Player Wins: {player_wins} \nBot Wins: {bot_wins}")
  
# Utility Functions
def display_choices(player, bot):
  print(f"\nYour Choice: {player.capitalize()} \nBot Choice: {bot.capitalize()}")
  time.sleep(0.5)
 
# Main Entry Point 
while True:
  print("\nROCK PAPER SCISSORS")
  print("1. Start Game")
  print("2. Check History")
  print("3. Exit")
  choice = input("Choose an option (1 - 3): ")
  
  if choice == "1":
    start_game()
  elif choice == "2":
    check_history()
  elif choice == "3":
    sys.exit("\nThanks for playing the game")
  else:
    print("Invalid option. Try again!")
