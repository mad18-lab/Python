def number(a):
    c = 0
    while (a>0):
        b = a%10
        c = c * 10 + b
        a = a//10
    return c

a = int(input("Enter your number: "))
print("Reverse of", a, "is", number(a))