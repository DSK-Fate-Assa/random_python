#a python program that prompts the user to enter a name and if the name is less than 4 characters
#it displays too short and if its more than it reverses the name
name = input("What is your name?  ")
namex = len(name)


if namex<4:
	print("The name is too short")
else:
	print("Your name is long")
	for x in reversed(name):
		print(x, end="")