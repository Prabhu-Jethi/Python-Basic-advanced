## Converts inch to cm
## 1 inch = 2.54 cm
## inch * 2.54cm

def inch_to_cm(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))
print(f"The corresponding value in cms is: {inch_to_cm(n)}")