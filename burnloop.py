num = eval(input('enter the highest number possible   '))

def burn_loop(num):
    for i in range(num + 1):
        for x in (range(i)):
            print(i)
    #while (i):
         #print("stuck in a loop")

burn_loop(num)