def bitwise(a,b,c):
    if (c=='**'):
        print("a**b:", a**b)
    elif (c=='~'):
        print("~a:", ~a)
        print("~b:", ~b)
    elif (c=='*'):
        print("a*b:", a*b)
    elif (c=='/'):
        print("a/b:", a/b)
    elif (c=='%'):
        print("a%b:", a%b)
    elif (c=='//'):
        print("a//b:", a//b)
    elif (c=='+'):
        print("a+b:", a+b)
    elif (c=='-'):
        print("a-b:", a-b)
    elif (c=='&'):
        print ("a&b:", a&b)
    elif (c=='^'):
        print("a^b:", a^b)
    elif (c=='|'):
        print("a|b:", a|b)
    else:
        print("INVALID OPERATOR")
d=str(input("Enter the bitwise operator you wanna use: "))
e=int(input("Enter number one: "))
f=int(input("Enter number two: "))
r=bitwise(e,f,d)
