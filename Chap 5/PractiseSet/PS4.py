## What will be the length of following set s:
## s = set()
## s.add(20)
## s.add(20.0)
## s.add('20')

s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(s)
print(len(s))

## The length of this str is 2, it doesn't include 20.0 as it is same as 20