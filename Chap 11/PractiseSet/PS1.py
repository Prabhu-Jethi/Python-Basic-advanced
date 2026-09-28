## Create a class (2D vector) and use it to create another class representing a 3D vector.

class twoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The 2D-vector is: {self.i}i + {self.j}j")
        
class threeDVector(twoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def show(self):
        print(f"The 3D-vector is: {self.i}i + {self.j}j + {self.k}k")
        
a = twoDVector(2,4)
a.show()

b = threeDVector(2,4,6)
b.show()