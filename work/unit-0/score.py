# A simple program to calculate the percentage of a mark in a subject
subject = input("Subject: ")
mark = int(input("Your mark: "))
total = int(input("Out of: "))
percentage = round(mark / total * 100, 1)
print(f"You got {mark} out of {total} in {subject}. That's {percentage}%.")

if percentage >= 75:
    print("Grade: A1. Your grade is epic.")
elif percentage < 74 and percentage >= 70:
    print("Grade: B2. Your grade is legendary.")
elif percentage < 69 and percentage >= 65:
    print("Grade: B3. Your grade is rare.")
elif percentage < 64 and percentage >= 60:
    print("Grade: C4. Your grade is uncommon.")
elif percentage < 59 and percentage >= 55:
    print("Grade: C5. Your grade is common.")  
elif percentage < 54 and percentage >= 50:
    print("Grade: C6. Your grade is the good kind of basic")
elif percentage < 49 and percentage >= 45:
    print("Grade: D7. Your grade is the bad kind of basic .")
elif percentage < 44 and percentage >= 40:
    print("Grade: E8. With your grade, there's a whole lot of room for improvement.")
elif percentage <= 39:
    print("Grade: F9. Your means you tried. So, keep trying.")