## Create an empty dictionary. Allow 4 friends to enter their favourite language as value and use key as their names. Assume that the names are unique.

friends = {
    "khushi": "python",
    "kalyan": "typescript",
    "reetika": "java",
    "isha": "c++"
}

lang = input("Enter your name to get your language: ")
print(friends[lang])