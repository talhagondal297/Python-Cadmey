banned_users = ['Sam', 'Kiran', 'Naz', 'Sherry']
prompt = "\nAdd a player to your team."
prompt += "\nEnter 'quit' when you're done. "
players = []
while True:
    player = input(prompt)
    if player == 'quit':
        break
    elif player in banned_users:
        print(player + " is banned!")
        continue
    else:
        players.append(player)
        print("\nYour team:")


for player in players:
    print(player)

# ===============================

banned_users = ['Sam', 'Kiran', 'Naz', 'Sherry']
players = []

while True:
    player = input("Add a player to your team (enter 'quit' to exit): ").strip()

    if player.lower() == 'quit':
        break
    elif player in banned_users:
        print(player + " is banned! Choose another player.")
    else:
        players.append(player)
        print(player + " has been added to your team.")

print("\nYour team:")
print(", ".join(players))
