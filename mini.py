foods = {"Tuwo": "Available",
        "Goat": "Available",
        "Beef": "Available",
        "Chicken": "Available",
}
isIt = (foods.get(input("Enter your food (Don't forget to capitalize): ")))!= None
#print(isIt)
if isIt == True:
    print("Food is Available")
else:
    print("Sorry, food is not Available in your region")


