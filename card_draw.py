# Intentionally flawed Python program

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# dictionary for rank names
rank_names = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}

# draw five cards
print("You got:")
for i in range(5):
    rank = rank_names.get(deck[i][0], deck[i][0])
    print(rank, "of", deck[i][1])