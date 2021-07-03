#to find the average of the marks and print if they failed or passed
x = eval(input("enter your physics mark    "))
y = eval(input("enter your chemistry mark    "))
z = eval(input("enter your biology mark    "))

total= x+y+z
average = total/3

print("your total mark was ",total)

if average < 50:
	print("your average was ",average,"so you failed")
elif average > 69:
	print("your average was ",average,"so you passed")
else:
	print("your average was ",average,"so you got an average mark")