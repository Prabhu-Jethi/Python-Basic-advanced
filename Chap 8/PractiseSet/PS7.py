## Remove a given word from a list and strip it at the same time.

def remove(list, word):
    n = []
    for i in list:
        if not(i == word):
            n.append(i.strip(word))
        return n
    
list = ["Prabhu", "bkl", "mc", "bc"]

print(remove(list, "bc"))