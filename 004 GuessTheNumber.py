#guess the number, with hints
import random

noToGuess = random.randint(1,20)
print("Try to guess which number I am thinking of? From 1 to 20")

userGuess = 0

while userGuess != noToGuess:
    try:
        print("Your guess: ", end="")
        userGuess = int(input())
    except ValueError:
        print("not a number")
        continue

    if userGuess > noToGuess:
        print("too high")
    elif userGuess == noToGuess:
        continue
    else:
        print("too low")
print("Correct! The number is "+str(noToGuess))    