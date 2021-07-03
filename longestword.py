print("input 2 names")
name1 = input("1. ")
name2 = input("2. ")

x = len(name1)
y = len(name2)

if x>y:
	print(name1," is the longer name")
elif x<y:
	print(name2," is the longer name")
else:
	print(" they have the same number of letters")
