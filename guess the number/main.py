import random

guesseed_number=random.randint(1,10)
print("I am thinking of a number between 1 and 100 can you guess it?")



while True:
    guess=int(input("Guess the number: "))
    if guess < guesseed_number:
        print("Too low")
    elif guess > guesseed_number:
        print("Too high")
    else:
        print("You guessed it; the number is", guesseed_number)
        break
    