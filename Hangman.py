from random import choice 

def run_game():
    # Choose a random word
    word: str = choice(['apple', 'orange', 'banana'])
    
    # Get the username from the user
    username: str = input("What username do you want to keep? ")
    print("Welcome to Hangman, " + username)

    # Setup 
    guessed: str = " "
    tries: int = 3 

    while tries > 0 :
        blanks: int = 0
         
        print("Word:", end=' ')
        # Display the word with guessed letters or underscores
        for char in word:
            if char in guessed: 
                print(char, end=" ")
            else:
                print("_", end=" ")
                blanks += 1 

        print()  # Adds a blank line at the end 

        # Check if the word is fully guessed
        if blanks == 0:
            print("Congratulations! You have guessed the word.")
            break 

        guess: str = input("Enter a letter:")
        # Check if the letter has already been guessed
        if guess in guessed:
            print("You have already used " + guess + ". Please try with another letter.")
            continue 

        guessed += guess
        # Check if the guessed letter is not in the word
        if guess not in word:
            tries -= 1
            print("Sorry, that was wrong. Tries remaining: " + str(tries))
            if tries == 0:
                print("No more tries remaining. You lose.")
            break

if __name__ == "__main__":
    run_game()
