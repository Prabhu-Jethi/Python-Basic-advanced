## Write program to mine a log file and find out whether it contains 'python'.

with open(r"d:\Python\Chap 9\PractiseSet\txts\log.txt", "r") as f:
    content = f.read()
    
if("python" in content):
    print("Yes")
else:
    print("No")
