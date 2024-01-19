import random

class Hat:

    
    houses=["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]

    @classmethod
    def sort(clf,name):
        if not name:
            raise ValueError("Missing name")
        print(name,"is in",random.choice(clf.houses))



Hat.sort("Harry")
