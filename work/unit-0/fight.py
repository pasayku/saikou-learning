# A fight in a roguelike game
health = 20
damage = 5
health = health - damage
print(f"You take {damage} damage. Health left: {health}")

if health <= 0:
    print("You died. Back to the start of the run.")
elif health < 20:
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
