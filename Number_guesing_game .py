from random import randint

lower_number, higher_number = 1, 10  

random_number = randint(lower_number, higher_number)

print(f"Guess the number between {lower_number} and {higher_number}") 

while True:

  try:
    guess = int(input("Guess the number: "))
  
  except ValueError:
    print("Enter a valid number")
    continue

  if guess > random_number:
    print("Too high!")
  elif guess < random_number: 
    print("Too low!")
  else:
    print("You guessed correctly!")
    break # Breaks out of the while loop

print("Done!")