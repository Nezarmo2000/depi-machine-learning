import random

random_number = random.randint(1, 9)

print("Guess a number between 1 and 9:")

while True:
    guess = int(input("Enter your guess: "))
    
    if guess == random_number:
        print("Congratulations! You guessed it right!")
        break
    else:
        print("Wrong guess! Try again.")