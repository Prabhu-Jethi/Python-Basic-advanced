## Can you change the values inside a list which is contained in set S ?
## s = {8, 7, 12, "prabhu", [1,2]}

s = {8, 7, 12, "prabhu", [1,2]}

s[4][0] = 9

## No we can't, cause its showing typeerror of unhashable type of list...