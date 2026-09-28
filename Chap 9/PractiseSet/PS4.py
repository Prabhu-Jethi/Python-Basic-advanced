## A file contains a word "Donkey" multiple times. You need to write a program which replace this word with ##### by updating the same file.

word = "Donkey"
# word = "######"

with open(r"d:\Python\Chap 9\PractiseSet\txts\file.txt", "r") as f:
    content = f.read()
    
newContent = content.replace(word, "######")
# newContent = content.replace(word, "Donkey")

with open(r"d:\Python\Chap 9\PractiseSet\txts\file.txt", "w") as f:
    f.write(newContent)