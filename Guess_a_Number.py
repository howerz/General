import random

x=random.randint(1,10)
guess=int(input("Guess a number from 1-10 : "))
guesscount=1

if x==guess:
    print("Correct! The answer was " + str(x) + "!")
    print("It took you " + str(guesscount) + " guesses to win!")
else:
    while x!=guess:
        guess=int(input("Wrong! Guess again : "))
        guesscount += 1
    print("Correct! The answer was " + str(x) + "!")
    print("It took you " + str(guesscount) + " guesses to win!")
    if guesscount <= 3:
        print("That's pretty good!")
        print("Damn Catie... Took ya long enough...")