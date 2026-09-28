## A spam comment is defined as a text containing following keywords:
## "Make a lot of money", "buy now", "subscribe this", "click this". 
## Wap to detect these spams.

c1 = "Make a lot of money"
c2 = "buy now"
c3 = "subscribe this"
c4 = "click this"

msg = input("Enter your comment: ")

if((c1 in msg) or (c2 in msg) or (c3 in msg) or (c4 in msg)):
    print("This comment is spam")
else:
    print("This comment is not spam")