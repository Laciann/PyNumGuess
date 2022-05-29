import random

number_of_guesses = 0 
number = random.randint(1,50)

name = input("Your name? ")

print("Hello", name + "! I have selected an integer number between 1 to 50. Take a guess! What must be it?")

while number_of_guesses < 8:
    guess = input("Enter your guess :: ")
    guess = int(guess)

    number_of_guesses = number_of_guesses + 1 
    guesses_left = 8 - number_of_guesses

    if guess < number:
        guesses_left = str(guesses_left)
        print("Guess is lower! You have " + guesses_left + " guesses left.")

    elif guess > number:
        guesses_left= str(guesses_left)
        print("Guess is higher! You have " + guesses_left + " guesses left.")

    elif guess == number:
        break

if guess==number:
  number_of_guesses=str(number_of_guesses)
  print("Good job! It took " + number_of_guesses + " attempts for you to guess correctly.")

elif guess!=number:
  number=str(number)
  print("Sorry. The number actually is " + number + ".")