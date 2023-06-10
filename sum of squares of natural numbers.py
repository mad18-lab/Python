a = int(input("Enter the number of natural numbers you want: "))
sm = 0
for i in range(1, a+1):
    sm = sm + (i * i)

print("The sum of squares of ", a, " natural numbers is: ", sm)