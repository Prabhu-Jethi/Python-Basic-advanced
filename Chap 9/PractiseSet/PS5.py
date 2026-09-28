## Repeat problem 4 for a list of such words to be censored.

words = ["Donkey", "bad", "gadhaa"]

with open(r"d:\Python\Chap 9\PractiseSet\txts\file.txt", "r") as f:
    content = f.read()
    
for word in words:
    content = content.replace(word, "#" * len(word))
    
with open(r"d:\Python\Chap 9\PractiseSet\txts\file.txt", "w") as f:
    f.write(content)