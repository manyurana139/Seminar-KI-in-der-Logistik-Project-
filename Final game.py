#Abhimanyu Rana_3164382
import random
import time
# Welcome message
print("Welcome to the Number Guessing Game!")
play_again = True
high_score = None
while play_again:
    print("Think of a number from 1 to 100")
    
    # Generating a random number and initializing variables
    secret_number = random.randint(1, 100)
    num_guesses = 0
    
    # loop until user guesses correctly or quits the game
    while True:
        # Ask user to guess the number or quit
        guess = input("Guess the number (or 'q' to quit): ")
        
        # check if user wants to quit the game
        if guess == "q":
            print("Thanks for playing!")
            play_again = False
            break
        
        # Convert user input to integer value or check if its even valid input as per this Game
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        # increment of number of guesses as user is not able to predict the correct value
        num_guesses += 1
        
        # check if user guessed correctly
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {num_guesses} guesses and {time.time()} seconds.")
    
            # update high score if new record is created
            if high_score is None or num_guesses < high_score:
                high_score = num_guesses
                print(f"You set a new high score of {high_score}!")
            
            break
        # provide feedback on whether guess was too high or too low
        elif guess < secret_number:
            print("No, Guess a little higher!")
        else:
            print("No, Guess a little lower!")
    # Showing high score to User        
    if play_again:
        print(f"Your high score is {high_score}.")
        # Ask user if intrested to play again
        play_again_input = input("Do you want to play again? (y/n) ")
        if play_again_input.lower() != 'y':
            print("Thanks for playing!")
            play_again = False

