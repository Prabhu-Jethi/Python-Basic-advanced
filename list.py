#move the zeroes to the end of list

list = [1,4,7,0,2,3,0,6]
for item in list:
    if item == 0:
        list.remove(item)
        list.append(item)
print("Sorted list : ", list)