#number guessing using while loop


import random
num = random.randint(1,100)
guess = 0
count=0
while guess!=num:
    guess = int(input("guess the number: "))
    count+=1
    if guess<num:
        print("too low")
    elif guess>num:
        print("too high")
print("you guessed it right")
print("you took",count,"guesses")