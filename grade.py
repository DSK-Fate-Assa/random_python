english_marks = eval(input("How much did you get in English??    "))
maths_marks = eval(input("How much did you get in Maths??    "))
science_marks = eval(input("How much did you get in Science??    "))

def average(english_marks, maths_marks, science_marks):
	return (english_marks+maths_marks+science_marks)/3

average_mark = average(english_marks, maths_marks, science_marks)
def grade(average_mark):
	grade = ""
	if average_mark>=90:
		grade = "A*"
	elif average_mark>=80:
		grade = "A"
	elif average_mark>=70:
		grade = "B"
	elif average_mark>=60:
		grade = "C"
	elif average_mark>=50:
		grade = "D"
	elif average_mark>=40:
		grade = "E"
	else:
		grade = "U"
	return grade

grade = grade(average_mark)

print("Your grade is ",grade,"!!")