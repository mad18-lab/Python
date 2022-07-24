a=int(input("Enter your limit: "))
i=1
S1=0
S2=0
while (i<=a):
    if (i%2==0):
        S1=S1+i
        i=i+1
    else:
        S2=S2+i
        i=i+1
print("Sum of Even Numbers: ", S1)
print("Sum of Odd Numbers: ", S2)


