balance = 100.00

def deposit(amount):
  
  print(f"Deposited N{amount} successfully")
  balance = balance + amount
  
def withdraw(amount):
  if balance > amount:
    balance -= amount
    print(f"Withdrew N{amount} successfully")
  else:
    print("Insufficient balance!")
    
def check_balance():
  print(f"\nAvailable balance: N{balance}\n")

while True:
  print("1. Deposit money")
  print("2. Withdraw money")
  print("3. Check balance")
  print("4. Exit")
  choice = input("Choose an option (1-4): ")
  
  if choice == "1":
    amount = int(input("Enter amount to deposit: "))
    deposit(amount)
  elif choice == "2":
    amount = int(input("Enter amount to withdraw: "))
    withdraw(amount)
  elif choice == "3":
    check_balance()
  elif choice == "4":
    print("\nThanks for using our service")
    break
  else:
    print("Invalid option!")