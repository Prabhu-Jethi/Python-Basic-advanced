## Generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 year old.

# def generateTable(n):
#     table = ""
#     for i in range(1, 11):
#         table += f"{n} * {i} = {n*i}\n"
        
#     path = r"d:\Python\Chap 9\PractiseSet\tables\table_{0}.txt".format(n)
    
#     with open(path, "w") as f:
#         f.write(table)
        
#     for i in range(2,21):
#         generateTable(i)
        
# print("All tables created")


import os

# Create the folder if it doesn't exist
folder = r"d:\Python\Chap 9\PractiseSet\tables"
os.makedirs(folder, exist_ok=True)

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} * {i} = {n*i}\n"
    
    with open(os.path.join(folder, f"table_{n}.txt"), "w") as f:
        f.write(table)

# Call the function for numbers 2 to 20
for i in range(2, 21):
    generateTable(i)
