x=eval(input("enter first number   "))
y=eval(input("enter second number   "))
z=eval(input("enter third number   "))

if (x<y) and (x<z):
	print("the smallest number is ",x)
elif (y<z) and (y<x):
	print("the smallest number is ",y)
else:
	print("the smallest number is ",z)