from random import choice as ch
from random import randint as ri
import random

coin=ch(["heads","tails"])
print("Coin flip is "+coin)

number=ri(1,10)
print(number)

cards=["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)