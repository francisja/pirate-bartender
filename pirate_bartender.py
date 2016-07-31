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
print("I be yer pirate bartender. I make pirates far and wide many a good drink. How do you like yer drink scallywag?")
input(questions["strong"] + (" yes or no?"))
if input == "yes":
    questions["strong"] = True
elif input == "no":
    questions["strong"] = False
input(questions["salty"] + (" yes or no?"))
if input == "yes":
    questions["salty"] = True
elif input == "no":
    questions["salty"] = False
input(questions["bitter"] + (" yes or no?"))
if input == "yes":
    questions["bitter"] = True
elif input == "no":
    questions["bitter"] = False
input(questions["sweet"] + (" yes or no?"))
if input == "yes":
    questions["sweet"] = True
elif input == "no":
    questions["sweet"] = False
input(questions["fruity"] + (" Yes or no?"))
if input == "yes":
    questions["fruity"] = True
elif input == "no":
    questions["fruity"] = False