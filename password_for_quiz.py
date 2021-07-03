name = input("Enter your email   ")
num = input("Set your new password   ")
num_of_tries = 3

num1 = input("""
..
..
..
..
..
..
..
..
..
..
..
..
..
..
TO ENTER THE QUIZ, ENTER THE PASSWORD OF YOUR EMAIL
""")

while True:
	if num1 == num:
		input("You have logged in, press enter to continue to the quiz")
		break	 
	else:
		if num_of_tries > 0:
			num1 = input("Incorrect password for {} try again, you only have {} number of tries left   ".format(name, num_of_tries))
			num_of_tries -= 1
		else:
			print("You are out of tries haha, we have sent your account to be hacked, ggs")
			exit()

def level_one():
	marks_for_level_1 = 0

	x = int(input("If Logx (1 / 8) = - 3 / 2, then x is equal to     "))
	if x == 4:
		print("\n Correct \n")
		marks_for_level_1 += 1
	else:
		print("Wrong, the answer is 4")

	y = input("""

f is a quadratic function whose graph is a parabola opening upward and has a vertex on the x-axis.
The graph of the new function g defined by g(x) = 2 - f(x - 5) has a range defined by the interval, Answer with A, B, C or D

A. [ -5 , + infinity)
B. [ 2 , + infinity)
C. ( - infinity , 2]
D. ( - infinity , 0]

""")

	if (y=="c" or y=="C"):
		print("Correct")
		marks_for_level_1 += 1
	else:
		print("Wrong the answer is C")

	if marks_for_level_1 == 2:
		print("Great you qualified for the next level")
	else:
		print("Hahahaha you didn't qualify, try again later")

try:
    level_one()
except ValueError:
    print("Answer with the required type of answer")
    exit()
