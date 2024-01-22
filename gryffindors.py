students=[
    {"name":"Hermione","house":"Gryffindor"},
    {"name":"Harry","house":"Gryffindor"},
    {"name":"Ron","house":"Gryffindor"},
    {"name":"Draco","house":"Slytherin"},
    {"name":"Padma","house":"Ravenclaw"}
]

gryffindors=[
    student["name"] for student in students if student["house"]=="Gryffindor"
]

def is_Ravenclaw(s):
    return s["house"]=="Ravenclaw"

print(*gryffindors)
print("Ravenclaw\n",*filter(is_Ravenclaw,students))