#to prompt the user to enter 2 numbers and print to say which one has a higher value
x=eval(input("enter the first number    "))
y=eval(input("enter the second number   "))
if y<x:
    print(x,"has a higher value than",y)
elif y>x:
    print(y,"has a higher value than",x)
else:
    print("both the numbers have the same value")
