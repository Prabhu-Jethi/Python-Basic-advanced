## Calculate the grade of a student from his marks from the following :
## 90-100 => Ex
## 80-90 => A
## 70-80 => B
## 60-70 => C
## 50-60 => D
## <50 => F

marks = int(input("Enter you marks: "))

if(marks>90 and marks<=100):
    print("Excellent!")
elif(marks>80 and marks<=90):
    print("You got 'A' ")
elif(marks>70 and marks<=80):
    print("You got 'B' ")
elif(marks>60 and marks<=70):
    print("You got 'C' ")
elif(marks>=50 and marks<=60):
    print("You got 'D' ")
else:
    print("You Failed!")