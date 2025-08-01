student = {
        "name": "Tom",
        "department":"Computer Science",
        "grades":[{"csc 111": 90, "Maths 101": 50, "physics": 70}],
        "address": {"city": "Jos", "town": "Rayfield", "house no.": "PL/ray/00001"},
        "fav_colors": ["Pink", "Red", "Black", "White"]
}
#Accessing dictionary items
print(student["name"])
print(student["department"])
print(f"CSC 111 Score:", student["grades"][0]["csc 111"])
print("Favorite color:", student["fav_colors"][2])
#student["fav_colors"].remove("Red")
#print(student["fav_colors"])

#Dictionary Methods
print(student.get("name"))
print(student.keys())
print(student.items())

print("-----------------Updating Student Data--------------------")
student["name"] = "Jerry"
print(student)
student.pop("fav_colors")
print("------------------After popping-------------------")
print(student)

