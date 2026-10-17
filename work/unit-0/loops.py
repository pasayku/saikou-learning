# Practie with while loops
count = 5
while count > 0:
    print(count)
    count -= 1
print("Go!")

answer = input("What's 7 times 8?")
while answer != "56":
    print("Not quite. Try agian.")
    answer = input("What's 7 times 8?")
print("Correct!")