import random


def guess_number():
    print("Hi, What is your name?")
    name = input()

    print(f"Well {name}, I'm thinking of a number between 1 and 20")
    print("Take a guess")

    number = random.randint(1, 20)

    while True:
        guess = int(input())
        if guess < number:
            print("Too low")
        elif guess == number:
            print("Correct")
            break
        elif guess > number:
            print("Too high")


guess_number()
