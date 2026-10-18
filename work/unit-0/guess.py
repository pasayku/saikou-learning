# The plan for the number guessing game
# 1. Generate a random number between 1 and 100 (already done).
# 2. Ask the user for their guess.
# 3. Compare the guess to the secret number and provide feedback.  
# 4. Keep telling user, the guess is too high or too low. Until user gets the correct guess.
# 5. tell the user how many guesses it took to get the correct answer.

import random
secret = random.randint(1, 100)
secret = int(secret)

count = 0

print(secret)

print("I'm thinking of a number from 1 to 100.")
answer = (input("Your guess: "))
while not answer.isdigit():
    print("Please pick a number between 1 and 100, like 67.")
    answer = (input("Your guess: "))
answer = int(answer)

count += 1


if answer > (secret): 
    print("Too high.")
    while answer > (secret + 20):
        print("Your guess is off by aeons. Try lower.")
    answer = int(input("Your guess: "))
    
    count += 1
while answer < (secret):
    print("Too low.")
    while answer < (secret - 20):
        print("Your guess is lower than my self-esteem. Aim higher.")
    answer = int(input("Your guess: "))

    count += 1
else:
    if answer == (secret): 
        print("You got it in", 0 + count, "guesses")
