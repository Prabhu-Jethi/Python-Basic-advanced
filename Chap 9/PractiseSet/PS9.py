## Find out whether a file is identical & matches the content of another file.

with open(r"d:\Python\Chap 9\PractiseSet\txts\this.txt") as f:
    content1 = f.read()

with open(r"d:\Python\Chap 9\PractiseSet\txts\this_is_copy.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes")

else: 
    print("No")