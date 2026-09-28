## Create a class with a class attribute a; create an object from it and set 'a' directly using object.a.obj. Does this change the class attribute?

class Demo:
    a = 4
    
obj = Demo()
print(obj.a)

obj.a = 0 # instance attr
print(obj.a) 

print(Demo.a) #prints class attr
