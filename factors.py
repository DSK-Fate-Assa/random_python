input("This program shows all the numbers with your choice of number of factors \nbetween a start number and a stop number, press enter to continue \n")
factors = eval(input("Enter the number of factors you want the number to have, (2 for prime numbers)\n"))
start = eval(input("Enter the start num \n"))
stop =  eval(input("Enter the stop num \n"))

def oof(start, stop):
    list_of_nums = []
    for i in range(start, stop+1):
        num_of_factors = 0
        for x in range(1, i+1):
            if i%x==0:
                num_of_factors += 1
            else:
                continue
        if num_of_factors==factors:
            list_of_nums.append(i)
        else:
            continue
    return list_of_nums

print(oof(start, stop))
