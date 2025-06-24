# DOBBLE GAME
import string
import random

sym = list(string.ascii_letters)      # getting list of symbols
card1 = [0] * 5
card2 = [0] * 5      # making 2 cards of 5 elements
pos1 = random.randint(0, 4)      # getting a random position for same symbol in card1
pos2 = random.randint(0, 4)      # getting a random position for same symbol in card2
sameSym = random.choice(sym)     # getting the same symbol
sym.remove(sameSym)     # remove the same symbol so that it occurs only once

if pos1 == pos2:    # if pos1 == pos2 then put samesym at those indices
    card1[pos1] = card2[pos2] = sameSym
else:
    card1[pos1] = sameSym
    card2[pos2] = sameSym
    card1[pos2] = random.choice(sym)  # becuase of if condition in while loop,
    sym.remove(card1[pos2])           # one of the pos1 or pos2 indexes wont be able to get
    card2[pos1] = random.choice(sym)  # values, hence we give value to both cards at both the indexes
    sym.remove(card2[pos1])

i = 0
while i < 5:     # filling rest of the indices
    if i != pos1 and i != pos2:     # so that we dont replace the same symbol
        uniqueSym1 = random.choice(sym)
        sym.remove(uniqueSym1)
        card1[i] = uniqueSym1
        uniqueSym2 = random.choice(sym)
        sym.remove(uniqueSym2)
        card2[i] = uniqueSym2
        print("Unique sym in card1: ", uniqueSym1, " at ", i, "in card1: ", card1[i])
        print("Unique sym in card2: ", uniqueSym2, " at ", i, "in card2", card2[i])

    i += 1
print("\t!!!Find the Common Symbol!!!")
print(card1)
print(card2)
ch = input("Common Symbol at: ")
if ch == sameSym:
    print("CORRECT!!")
else:
    print("WRONG")








