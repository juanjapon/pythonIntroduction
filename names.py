names=[]
with open("namess.txt") as file:
    for line in sorted(file):
        print("hello,",line.rstrip())



