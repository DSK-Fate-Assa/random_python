og_str = input('Input the text you want to remove spaces from.   ')
finished_str = ''
num_of_spaces = 0
for i in og_str:
    if not(i == " "):
        finished_str += i 
    else:
        num_of_spaces += 1

print(finished_str)
print('The number of spaces ejected was ', num_of_spaces)

#OR

og_str2 = input('Input the text you want to remove spaces from.   ')
print(og_str2.replace(' ', ''))
print('The number of spaces ejected was ', num_of_spaces)