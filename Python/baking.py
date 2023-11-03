import time

def menu():
    option = input("Please type the number of the function you would like to run: ")
    if option == "1":
        create()
    if option == "2":
        read()
    if option == "3":
        edit()

def create():
    ingredients = []
    amount = []
    title = input("Please enter the name of your recipe: ")
    people = int(input("Please enter the amount of people this will serve: "))
    ingredientss = int(input("How many ingridents do you need? "))
    for x in range(ingredientss):
        ask = input("Name of Ingredient: ")
        amountt = int(input("Please enter the amount needed: "))
        ingredients.append(ask)
        amount.append(amountt)
    instructions = input("Please enter the instructions for creating this recipe: ")
    print("Creating...")
    lengthi = len(ingredients)
    lengtha = len(amount)
    output = ""
    output2 = 0
    for x in range(lengthi):
        output = output + ", " + ingredients[x]
        output2 = output2, "", str(amount[x])

    time.sleep(2)
    f = open(f'{title}.txt', "x")
    f.write(f""" {people}

    Title: {title}
    Serves: {people}
    Items Needed: {output}  
    Amount Needed: {output2}         
    Instructions: {instructions} 
            
            
            
             """ )
    f.close()
    print("Created the recipe! Saved to files!")
    menu()

def read():
    name = input("Please enter the name of the recipe you would like to read? ")
    print("Reading...")
    time.sleep(2)
    f = open(f'{name}.txt', "r")
    print(f.read())
    f.close()
    print("Read the recipe!")

def edit():
    name = input("Please enter the name of the recipe you would like to edit? ")
    print("Loading...")
    time.sleep(2)
    ingredients = []
    amount = []
    title = input("Please enter the new name of your recipe: ")
    people = int(input("Please enter the amount of people this will serve: "))
    ingredientss = int(input("How many ingridents do you need? "))
    for x in range(ingredientss):
        ask = input("Name of Ingredient: ")
        amountt = int(input("Please enter the amount needed: "))
        ingredients.append(ask)
        amount.append(amountt)
    instructions = input("Please enter the instructions for creating this recipe: ")
    print("Creating...")
    lengthi = len(ingredients)
    lengtha = len(amount)
    output = ""
    output2 = 0
    for x in range(lengthi):
        output = output + ", " + ingredients[x]
        output2 = output2, "", str(amount[x])
    time.sleep(2)
    f = open(f'{name}.txt', "w")
    f.write(f""" {people}

    Title: {title}
    Serves: {people}
    Items Needed: {output}  
    Amount Needed: {output2}         
    Instructions: {instructions} 
            
            
            
             """ )
    f.close()
    print("Edited the recipe! Saved to files!")
menu()