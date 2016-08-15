import random

questions = {
    "strong": "Do ye like yer drinks with a strong kick?",
    "salty": "Do they go down the hatch salty like the sea?",
    "bitter": "Arr ye a lubber of that bitter taste in yer mouth?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Arr ye a matey that enjoys a fruity finish?",
}

ingredients = {
    "strong": {"glug of rum": 10, "slug of whisky": 10, "splash of gin": 10},
    "salty": {"skewered olive": 10, "salt-dusted rim": 10, "rasher of bacon": 10},
    "bitter": {"shake of bitters": 10, "splash of tonic": 10, "twist of lemon peel": 10},
    "sweet": {"sugar cube": 10, "spoonful of honey": 10, "splash of cola": 10},
    "fruity": {"slice of orange": 10, "dash of cassis": 10, "cherry on top": 10},
}

styles = ["strong", "salty", "bitter", "sweet", "fruity"]
name = input("Arr me matey! What do ye go by?")


def drink_likes(): #a function to find out the style of drink the user wants
    drinkSelection = {}
    print ("I be yer pirate bartender. I make pirates, far and wide, many a good drink. How do you like yer drink scallywag?")
    for style in styles:
        answer = input(questions[style] + (" yes or no? ")) #for each item in the styles a question is asked to see if the user enjoys that preference
        drinkSelection[style] = answer == "yes" or answer =="y"
    return drinkSelection #adds the preferences to the drinkSelection list

def make_cocktail(drinkSelection): #a function to create a drink from the user's drink preferences
    cocktail = {}
    for style in styles:
        if drinkSelection[style]:
            ingredient = (random.choice(list(ingredients[style].keys()))) #from the user's preference, a random ingredient is selected to be added to the cocktail
            cocktail[style] = ingredient
            ingredients[style][ingredient] -= 1 #for every ingredient used, the stock goes down 1
#            print (ingredients[style][ingredient]) #check
    return cocktail #adds the drink mix to the cocktail list

if __name__ == "__main__":
    request = drink_likes() #sets the variable request to the function of drink_likes
    mix = make_cocktail(request) #sets the variable mix to the function of make_coctail
    drinkName = [mix] #drinkName creates a dictionary of the drink style preference with the random ingredient selected
#    print(drinkName) #check
    print("Here come yer drink ye wench")
    for alcohol in mix:
        print("A " + mix['{}'.format(alcohol)])

    want_drink = input("Would ye like summor poison? yes or no?")
    while want_drink == "yes" or want_drink == "y":
        for index, mix in enumerate(drinkName, start = 1): #creates a count in the index for each mix made
            same = input("Would you like another " + name + "-" + str(index) + "? yes or no?")
            if same == "yes" or same == "y": #creates the same drink as before
                print("Yer drink be up.")
                print("Another " + name + "-" + str(index) + ". " + "Just like the last one it has...")
                for style, ingredient in mix.items():
                    print("A " + ingredient + " has been added to yer drink") # with the tuple pair of style and ingredient in mix, ingredient is printed out
            else: #creates a new drink for the user that's different from the last one made
                request = drink_likes()
                mix = make_cocktail(request)
                drinkName.append(mix) #adds the new drink to the mix list
                for style, ingredient in mix.items():
                    print("A " + ingredient + " has been added to yer drink")
                break #stops the "for style, ingredient in mix.items()" loop
        want_drink = input("Would ye like summor poison? yes or no?") #starts the while loop again