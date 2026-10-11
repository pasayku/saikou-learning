mark = int(input("your mark: "))
total = int(input("Out of: "))
print(mark / total * 100) 
print(f"You got {mark} out of {total} in Maths. That's {round(mark / total * 100, 1)}%")