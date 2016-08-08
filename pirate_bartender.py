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
name = input("Arr me matey! What do ye go by? ")
print("I be yer pirate bartender, " + (name) + ". I make pirates, far and wide, many a good drink. How do you like yer drink scallywag?")

while True:
    try:
        def drink_likes():
            drinkSelection = {}
            for style in styles:
                answer = input(questions[style] + (" yes or no? "))
                drinkSelection[style] = answer == "yes" or answer =="y"
            return drinkSelection

        def make_cocktail(drinkSelection):
            cocktail = {}
            for style in styles:
                if drinkSelection[style] == True:
                    ingredient = (random.choice(list(ingredients[style].keys())))
                    cocktail[style] = ingredient
                    ingredients[style][ingredient] -= 1
        #            print (ingredients[style][ingredient]) #check
            return cocktail

        if __name__ == "__main__":
            request = drink_likes()
            mix = make_cocktail(request)
            drinkName = {}
            drinkName[name] = mix
        #    print(drinkName) #check
            print("HERE COME YER DRINK YE WENCH!")
            for title in drinkName.keys():
                print("Yer will like what I put in ye drink. I call it the " + title + ". " + "It has...")
            for alcohol in mix:
                print("A " + mix['{}'.format(alcohol)])

        another = input("Would ye like summor poison? yes or no? ")
        if another == "yes" or another == "y":
            for title in drinkName.keys():
                same = input("Would you like another " + title + "? yes or no? ")
            if same == "yes" or same == "y":
                print("YER DRINK BE UP!!!")
                print("Another " + title + ". " + "Just like the last one, it has...")
                for alcohol in drinkName[title]:
                    print("A " + drinkName[title]['{}'.format(alcohol)])
                break
        else:
            break
    except:
        break