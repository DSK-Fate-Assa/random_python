unordered_students=[]
unordered_marks=[]

    
#this function takes the first element of a tuple in a list
def takeFirst(elem):
    return elem[0]
    
#this function takes the second element of a tuple in a list
def takeSecond(elem):
    return elem[1]

#this function takes the values of the key 'Name' of a dict in a list
''' def get_name(elem):
    dict.get('Name') '''


def names_and_marksa(number):    
    names_and_marks = []
    for i in range(number):
        names=(input("Enter students name   "))
        unordered_students.append(names.title())
        scores=int(input("Enter students score   "))
        unordered_marks.append(scores)

    names_and_marks = list(zip(unordered_students, unordered_marks))

    names_and_marks.sort(key = takeSecond, reverse = False)
    print(names_and_marks)

def names_and_marksl(number):    
    names_and_marks = []
    for i in range(number):
        names=(input("Enter students name   "))
        unordered_students.append(names.title())
        scores=int(input("Enter students score   "))
        unordered_marks.append(scores)

    names_and_marks = list(zip(unordered_students, unordered_marks))

    names_and_marks.sort(key = takeFirst, reverse = False)
    print(names_and_marks)

def names_and_marksd(number):    
    names_and_marks = []
    for i in range(number):
        names=(input("Enter students name   "))
        unordered_students.append(names.title())
        scores=int(input("Enter students score   "))
        unordered_marks.append(scores)

    names_and_marks = list(zip(unordered_students, unordered_marks))

    names_and_marks.sort(key = takeSecond, reverse = True)
    print(names_and_marks)

x = input("""Do you want your data to be outputted in Alphabetical order of names, 
Ascending order of marks or descending order of marks, reply with Alphabetical, Ascending or Descending?   """)

number=int(input("How many students   "))

if x.upper() == 'ALPHABETICAL':
    names_and_marksl(number)
elif x.upper() == 'ASCENDING':
    names_and_marksa(number)
elif x.upper() == 'DESCENDING': 
    names_and_marksd(number)
else:
    print("please type in something valid") 
