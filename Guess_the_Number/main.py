import random


random_number = random.randint(1, 100)
print("Guess a number between 1 and 100:")
while True:
    user_guess = (input("Guess the number or Quit (Q): "))
    if user_guess == 'Q' or user_guess == 'q':
        print("You chose to quit the game.")
        break
    user_guess = int(user_guess)
    if user_guess == random_number:
        print("Congratulations! You guessed the correct number.")
        break
    
    elif user_guess < random_number:
        print("Too low! Try again.")
        
    else:
        print(f"Your guess is too high! Try again.") 
        
        
print("Thank you for playing!")
    