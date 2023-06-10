x, y = 0, 1
b = int(input('Enter your range: '))
print(x)
print(y)
for i in range(b):
    z=x+y
    x=y
    y=z
    print(z)