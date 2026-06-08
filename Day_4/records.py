people=[ 
    {"name":"kasi" , "age":24},
    {"name":"vinay" , "age":23},
    {"name":"Haneesh" , "age":2} 
]
x=len(people)
for i in range(len(people)):
    print(f"{people[i]["name"]} is {people[i]["age"]} years old.")