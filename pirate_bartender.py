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

drinkS = {}
print ("I be yer pirate bartender. I make pirates far and wide many a good drink. How do you like yer drink scallywag?")

stro = input(questions["strong"] + (" yes or no?"))
if stro == "y" or stro == "Y":
    drinkS["strong"] = True
else:
    drinkS["strong"] = False
salt = input(questions["salty"] + (" yes or no?"))
if salt == "yes" or salt == "y":
    drinkS["salty"] = True
else:
    drinkS["salty"] = False
bitt = input(questions["bitter"] + (" yes or no?"))
if bitt == "yes" or bitt == "y":
    drinkS["bitter"] = True
else:
    drinkS["bitter"] = False
swee = input(questions["sweet"] + (" yes or no?"))
if swee == "yes" or swee == "y":
    drinkS["sweet"] = True
else:
    drinkS["sweet"] = False
frui = input(questions["fruity"] + (" Yes or no?"))
if frui == "y" or frui == "Y":
    drinkS["fruity"] = True
else:
    drinkS["fruity"] = False
print(drinkS)
