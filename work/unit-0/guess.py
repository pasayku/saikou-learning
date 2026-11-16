import random
secret = random.randint(1, 100)
secret = int(secret)

count = 0

print("I'm thinking of a number from 1 to 100.")
answer = (input("Your guess: "))
while not answer.isdigit():
    print("Please pick a number between 1 and 100, like 67.")
    answer = (input("Your guess: "))
    count += 1
answer = int(answer)

while answer != (secret):
    
    if answer > (secret + 20):
        print("Your guess is off by aeons. Try lower.")
        answer = (input("Your guess: "))
        while not answer.isdigit():
            print("Please pick a number between 1 and 100, like 67.")
            answer = (input("Your guess: "))
            count += 1
        answer = int(answer)
        count += 1
    else:
        if answer > secret:
            print("Too high. Try lower.")
            answer = (input("Your guess: "))
            while not answer.isdigit():
                print("Please pick a number between 1 and 100, like 67.")
                answer = (input("Your guess: "))
                count += 1
            answer = int(answer)
            count += 1

    if answer < (secret - 20):
        print("Your guess is lower than my self-esteem. Aim higher.")
        answer = (input("Your guess: "))
        while not answer.isdigit():
            print("Please pick a number between 1 and 100, like 67.")
            answer = (input("Your guess: "))
            count += 1
        answer = int(answer)
        count += 1
    else:
        if answer < secret:
            print("Too low. Try higher.")
            answer = (input("Your guess: "))
            while not answer.isdigit():
                print("Please pick a number between 1 and 100, like 67.")
                answer = (input("Your guess: "))
                count += 1
            answer = int(answer)
            count += 1
answer = int(answer)

if answer == (secret):
    print("You got it! The number was", secret)
    print("You got it in", 1 + count, "guesses.")
answer = int(answer)

