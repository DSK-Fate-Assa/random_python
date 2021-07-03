side1 = eval(input("enter the first side of you triangle.   "))
side2 = eval(input("enter the second side of you triangle.   "))
side3 = eval(input("enter the third side of you triangle.   "))

if side1==side2==side3 :
	print("it is an equilateral triangle")
elif side1==side2 or side1==side3 or side2==side3:
	print("it is an isosceles triangle")
else:
	print("It is a scalene triangle")
