import random

x = random.randint(1,10)
y = eval(input("Guess a number      -    "))
num_of_tries = 4
th_or_tl = ""

while True:
	if x == y:
 		print("Correct, veree noice ")
 		break
	else:
		if num_of_tries>0:
			if y > x:
				th_or_tl = "Too high"
			else:
				th_or_tl = "Too low"
			y = eval(input("OOf thats incorrect,your answer is {}, you have {} number of tries   -  ".format(th_or_tl, num_of_tries)))
			num_of_tries = num_of_tries - 1 
		else:
			print("You are out of tries, YOU LOSE LMFAOO")
			exit()

if num_of_tries==4:
	print("You got 100%")
elif num_of_tries==3:
	print("You got 90%")
elif num_of_tries==2:
	print("You got 70%")
else:
	print("You got 60%")