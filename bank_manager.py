balance = 100.00

def deposit(amount):
  global balance
  balance += amount
  print(f"Deposited N{amount} successfully")
  
def withdraw(amount):
  global balance
  if balance >= amount:
    balance = balance - amount
    print(f"Withdrew N{amount} successfully")
  else:
    print("Insufficient balance!")
    
def check_balance():
  print(f"\nAvailable balance: N{balance}")

while True:
  print("\nBANK MANAGER SYSTEM")
  print("1. Deposit money")
  print("2. Withdraw money")
  print("3. Check balance")
  print("4. Exit")
  choice = input("Choose an option (1-4): ")
  
  if choice == "1":
    amount = int(input("\nEnter amount to deposit: "))
    deposit(amount)
  elif choice == "2":
    amount = int(input("\nEnter amount to withdraw: "))
    withdraw(amount)
  elif choice == "3":
    check_balance()
  elif choice == "4":
    print("\nThanks for using our service")
    break
  else:
    print("\nInvalid option. Try again!")