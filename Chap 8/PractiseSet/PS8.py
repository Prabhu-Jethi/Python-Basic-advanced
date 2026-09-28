## Print multiplication table of a given number

def multiply(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n*i}")
    return ""
n = int(input("Enter a number: "))
print(multiply(n))
