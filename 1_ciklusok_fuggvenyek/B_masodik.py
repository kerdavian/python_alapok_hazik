players = ['Peter', 'Kate', 'John']

# 1. megoldás
for index, player in enumerate(players):
  print(f"{index +1}. {player}")

# 2. megoldás
for index in range(len(player) - 1):
  print(f"{index + 1}. {players[index]}")
