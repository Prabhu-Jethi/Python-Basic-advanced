## Rename a file to "renamed_by_python.txt".

with open(r"d:\Python\Chap 9\PractiseSet\txts\old.txt") as f:
    content = f.read()
    
with open(r"d:\Python\Chap 9\PractiseSet\txts\renamed_by_python.txt", "w") as f:
    f.write(content)