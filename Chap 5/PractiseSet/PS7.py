## If the names of 2 friends are same, what will happen to the program in PS6 ?

friends = {
    "khushi": "python",
    "kalyan": "typescript",
    "reetika": "java",
    "kalyan": "c++"
}

lang = input("Enter your name to get your language: ")
print(friends[lang])

## In this case the friend whose name is displayed at the end will be shown.