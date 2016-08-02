import random

questions = {
    "strong": "Do ye like yer drinks with a strong kick?",
    "salty": "Do they go down the hatch salty like the sea?",
    "bitter": "Arr ye a lubber of that bitter taste in yer mouth?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Arr ye a matey that enjoys a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
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
            cocktail[style] = random.choice(ingredients[style])
    return cocktail