# A simple program to calculate the percentage of a mark in a subject
subject = input("Subject: ")
mark = int(input("Your mark: "))
total = int(input("Out of: "))
print(f"You got {mark} out of {total} in {subject}. That's {round(mark / total * 100, 1)}%.")