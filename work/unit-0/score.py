# A simple program to calculate the percentage of a mark in a subject
subject = input("Subject: ")
mark = (input("Your mark: "))
while not mark.isdigit():
    print("Please type a whole number, like 42.")
    mark = input("Your mark: ")
mark = int(mark)

total = (input("Out of: "))
while not total.isdigit():
    print("Please type a whole number, like 42.")
    total = int(total)

if (total) == 0:
    print("The total can't be 0.")
elif int(mark) > int(total):
    print("Your mark can't be more than the total.")
else:
    percentage = round(int(mark) / int(total) * 100,1)
    print(f"You got {int(mark)} out of {int(total)} in {subject}. That's {percentage}%.")

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
        print("Grade: F9. Your grade isn't good, atleast you tried. You can do better next time.")
