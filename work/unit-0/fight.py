# A fight in a rougelike game
health = 30
damage = 45
health = health - damage
print(f"You take {damage} damage. Health left: {health}")

if health <= 20:
    print("You died. Back to the start of the run.")
elif health < 0:
    print("Low health! Drink a potion.")
else:
    print("Still standing. Keep going.")
print("Thanks for playing.")

level = 5
has_key = False

if level >= 5 and has_key:
    print("The boss door opens.")
else:
    print("The boss door stays shut.")
