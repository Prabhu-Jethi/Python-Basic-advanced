## Write program to make a copy of a text file "this.txt"
    
with open(r"d:\Python\Chap 9\PractiseSet\txts\this.txt", "r") as f:  
    content = f.read()

with open(r"d:\Python\Chap 9\PractiseSet\txts\this_is_copy.txt", "w") as f:
    f.write(content)