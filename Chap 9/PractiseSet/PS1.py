## Read the text from a given file 'poems.txt' and find out whether it contains the word 'stars'

with open(r"d:\Python\Chap 9\PractiseSet\txts\poems.txt") as f:
    content = f.read()
    if("stars" in content):
        print("The word is present")
    else:
        print("The word is absent")
        
f.close()