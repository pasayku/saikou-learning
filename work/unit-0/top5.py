top5 = ["Cyberpunk 2077", "Black Myth: Wukong", "Ghost of Yotei", "Grand Theft Auto VI", "Phantom Blade 0" ]
import random
pick = random.choice(top5)

print("Games I'm playing first when I get a PS5:")
rank = 1
for game in top5:
    print(f" {rank}. {game}")
    rank += 1
print(f"Can't decide? Tonight's pick: {pick}")

# No. of stars = how much I'm currently hyped to play the game.
if pick == "Cyberpunk 2077":
    print("Cyberpunk 2077 | Rating: (⭐⭐⭐⭐⭐)")
if pick == "Black Myth: Wukong":
    print("Black Myth: Wukong |  Rating: (⭐⭐⭐⭐)")
if pick == "Ghost of Yotei":
    print("Ghost of Yotei | Rating: (⭐⭐⭐⭐)")
if pick == "Grand Theft Auto VI":
    print("Grand Theft Auto VI | Rating: (⭐⭐⭐)")
if pick == "Phantom Blade 0":
    print("Phantom Blade 0 | Rating: (⭐⭐⭐)") 