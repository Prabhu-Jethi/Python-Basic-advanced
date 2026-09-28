# f = open(r"d:\Python\Chap 9\file.txt")
# print(f.read())
# f.close()

# The same can be written using with statement like this:
with open(r"d:\Python\Chap 9\file.txt") as f:
    print(f.read())