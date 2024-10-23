import random

answer = random.randint(1, 100)

print("welcome to CREO ZESTY !!!")
print("im thinking a number between 1 and 100")
difficulty = input("choose difficulty type 'easy' or 'hard': ")

attempts = 0
if difficulty == 'easy':
    attempts = 10
if difficulty == 'hard':
    attempts = 5


for i in range(0, attempts-1):
    print(f"you have {attempts-i} attempts remaining to guess the number")
    guess = int(input("make a guess: "))
    if attempts - i == 0 :
        print("u lose loserrr")
    if guess == answer:
        print("u found it, you win ! congrats bitch")
        break
    elif guess > answer:
        print("thats too high bruh")
        print("guess again")
    elif guess < answer:
        print("thats too lowwwwwwwww")
        print("guess again")


