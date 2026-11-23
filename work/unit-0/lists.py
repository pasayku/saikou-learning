# Practce with lists and for loops
subjects = ["Maths", "English", "Biology", "Physics"]
for subject in subjects:
    print(f"I Study {subject}.")
print("That's all my subjects.")

marks = [72, 45, 88, 50]
total = 0
for mark in marks:
    total += mark
print(f"Total: {total}")
print(f"Average: {total / len(marks)}")

sum(marks)