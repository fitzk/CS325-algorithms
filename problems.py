import random
import time

array = []
count = 0
result = 0
cnt = 0

#creates a file for output
f = open('MSS_Problems.txt','a')
num = 50
while cnt < 10:
    while count < 10:
        while result < num:
            array.append(random.randint(-50,100))
            result = result + 1;
        s = str(array) + '\n'
        f.write(s)
        del array[:]
        array[:] = []
        result = 0
        count = count + 1
    cnt = cnt + 1
    count = 0
    num = num + 50

#set up command line args for inputing testData
# close file
f.close()
