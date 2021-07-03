name = input("What is your name?  ")
namex = len(name)

for x in range(namex):
	if x<4:
		print("The name is too short")
	if x>4:
		print("Your name is long")