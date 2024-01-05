import random


b1=random.randint(1,43)

b2=random.randint(1,43)
while(b2==b1):
    b2=random.randint(1,43)
b3=random.randint(1,43)
while(b3==b1 or b3==b2):
    b3=random.randint(1,43)
b4=random.randint(1,43)
while(b4==b3 or b4==b2 or b4==b1):
    b4=random.randint(1,43)
b5=random.randint(1,43)
while(b5==b4 or b5==b3 or b5==b2 or b5==b1):
    b5=random.randint(1,43)

sb=random.randint(1,16)

print(b1,b2,b3,b4,b5,sb)