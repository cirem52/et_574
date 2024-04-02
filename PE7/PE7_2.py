#for number in range(1,1001):
#    if number % 2 == 0:        #goes through every number between 1-1000 and prints it if it is divisible by 2
#        print(str(number),end="|") 

counter = 1
while counter <= 1000:
    if counter % 2 == 0:    #if counter is even, prints counter and adds 1. otherwise, just adds 1.
        print(counter,end="|")
        counter += 1
    else:
        counter += 1