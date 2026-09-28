## Find out the line number where python is present from ques 6.

with open(r"d:\Python\Chap 9\PractiseSet\txts\log.txt") as f:
    lines = f.readlines()
    
line_no = 1
for line in lines:
    if("python" in line):
        print(f"Yes at : {line_no}")
        break
    line_no += 1
else:
    print("No")