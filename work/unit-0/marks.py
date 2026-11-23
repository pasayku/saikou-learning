marks = [72, 45, 88, 50, 39, 61, 54, 49,]
total = sum(marks)

print(f"No. of marks: {len(marks)} marks")
print(f"Average: {round(total / len(marks), 1)}")
print(f"Highest: {max(marks)}")
print(f"Lowest: {min(marks)}")
print("Credits:")
count = 0

for mark in marks:
    if mark >= 50:
        print(f"{mark}")
        count += 1
else:
    print(f"{count} out of {len(marks)} got a credit.")