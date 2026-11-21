# Practce with lists and for loops
subjects = ["Maths", "English", "Biology", "Physics"]
for subject in subjects:
    print(f"I Study {subject}.")
print("That's all my subjects.")

index = 0
while index < len(subjects):
    print(f"I study {subjects[index]}.")
    index += 1
