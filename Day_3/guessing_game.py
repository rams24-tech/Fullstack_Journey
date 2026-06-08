import random
secret = random.randint(1, 100)   # picks a random whole number from 1 to 100
correct=0
count=0
while correct!=secret:
    guess=int(input("Guess a number between 1 and 100: "))
    if guess>secret:
        print("Too high!")
        count=count+1
    elif guess<secret:
        print("Too low!")
        count=count+1
    elif guess==secret:
        count=count+1
        print(f"correct ! you got it in {count} attempts")
        correct=secret        
