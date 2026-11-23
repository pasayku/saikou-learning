top5 = ["Cyberpunk 2077", "Black Myth: Wukong", "Ghost of Yotei", "Grand Theft Auto VI", "Phantom Blade 0" ]
import random
pick = random.choice(top5)

print("Games I'm playing first when I get a PS5:")
rank = 5
for game in top5:
    print(f" {rank}. {game}")
    rank -= 1
print(f"Can't decide? Tonight's pick: {pick}")