input("Hello, thank you for doing this quiz, if you are ready press enter")

def level_one():
	marks_for_level_1 = 0

	x = int(input("If Logx (1 / 8) = - 3 / 2, then x is equal to     "))
	if x == 4:
		print("Correct")
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