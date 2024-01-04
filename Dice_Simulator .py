import random

# Rolls random dice
def roll_dice(amount: int = 2) -> list[int]:

  if amount <= 0:
    raise ValueError
  
  rolls: list[int] = []

  for i in range(amount):
    # Generate random number from 1 to 6
    random_roll: int = random.randint(1,6) 

    rolls.append(random_roll)

  return rolls

def main():

  while True:
    try:
      # Get input from user
      user_input: str = input("How many dice to roll? (or 'exit' to quit) ")
      
      # Check for exit case  
      if user_input.lower() == "exit":
        print("Thanks for playing!")
        break
      
      # Convert to integer
    #   amount = int(user_input)

      print(*roll_dice(int(user_input)), sep = ",")

    except ValueError:
      print("Please enter a valid amount")

# Check if run as main program
if __name__ == '__main__':
  main()