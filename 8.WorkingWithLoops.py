# While Loop

import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

randomNum = random.randint(1, 1000)
isGuessRight = False
Contekan = print(f'Nomor Jawabannya adalah : {randomNum}')

while isGuessRight != True:
    guess = input("Guess a number between 1 and 1000: ")
    if int(guess) == randomNum:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        

# For Loop
print("Count to 100!")
RangeNum = range(1, 101)
for x in RangeNum:
    print(x)
    
# Lets Simplify the Code
print("Count to 100!")
for x in range(1,101):
    print(x)