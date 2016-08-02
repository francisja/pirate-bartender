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
    "salty": {"olive on a stick": 10, "salt-dusted rim": 10, "rasher of bacon": 10},
    "bitter": {"shake of bitters": 10, "splash of tonic": 10, "twist of lemon peel": 10},
    "sweet": {"sugar cube": 10, "spoonful of honey": 10, "splash of cola": 10},
    "fruity": {"slice of orange": 10, "dash of cassis": 10, "cherry on top": 10},
}

styles = ["strong", "salty", "bitter", "sweet", "fruity"]
def drink_likes():
    drinkS = {}
    print ("I be yer pirate bartender. I make pirates far and wide many a good drink. How do you like yer drink scallywag?")

    for style in styles:
        answer = input(questions[style] + (" yes or no? "))
        drinkS[style] = answer == "yes" or answer =="y"
    return drinkS

def make_cocktail(drinkS):
    cocktail = {}
    for style in styles:
        if drinkS[style] == True:
            ingredient = random.choice(list(ingredients[style].keys()))
            cocktail[style] = ingredient
    return cocktail
    
if __name__ == "__main__":
    request = drink_likes()
    print(make_cocktail(request))