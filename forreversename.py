#write a python program that inputs the users name backwards
name = input("What is your name?  ")

namex = len(name)
print("Your name in reverse is ", end="")
for x in reversed(name):
	print(x, end="")