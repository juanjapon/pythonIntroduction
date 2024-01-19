class Student:
    def __init__(self,name,house,pathronus):

        self.name=name
        self.house=house
        self.pathronus=pathronus

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name")
        self._name=name
        

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self,house):
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid house")
        self._house=house

    def __str__(self):
        return (f"{self.name} from {self.house}")
    
    def charm(self):
        match self.pathronus:
            case "Stag":
                return "🐎"
            case "Otter":
                return "🐌"
            case "Jack Russell Terrier":
                return "🐶"
            case _:
                return "/"

def main():
    student = get_student()
    print("Expecto Patronum!!!!")
    print(student.charm())

def get_student():
    name=input("Name: ")
    house=input("House: ")
    pathronus=input("Pathronus: ")
    return Student(name,house,pathronus)

     
    

if __name__=="__main__":
    main()
    