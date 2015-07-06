######################################################################
# Project Group:  1                                                  #
# Group Members:  Eric Cruz, Baljot Singh, Kayla Fitzsimmons         #
# Course:         CS325-400                                          #
# Assignment:     Project 1                                          #
# File:           timer.py                                           #
# Description:    Calculates runtime for max sub array algorithms    #
######################################################################
from max_sub_array import MaxSub
import random
import time

#instance of MaxSub object
maxSub = MaxSub()

array = []
f3 = open('Time_Results.txt','a')
count = 0
result = 0
runTime = 0
cnt = 0
num = 100
while cnt < 10:
    while count < 10:
        while result < num:
            array.append(random.randint(-50,100))
            result = result + 1;
        start = time.clock()
        maxSub.maxSubEnum(array)
        end = time.clock()
        size = len(array) 
        runTime = runTime + (end - start)
        count = count + 1
        result = 0
        del array[:]
        array[:] = []
    count = 0
    cnt = cnt + 1
    num = num + 100
    s = 'Average time for 10 arrays of different values for algorithm 1 for size ' + str(size) + ': ' +  str(runTime/10) +'\n'
    f3.write(s)
    runTime = 0
    
count = 0
result = 0
runTime = 0
cnt = 0
num = 100
while cnt < 10:
    while count < 10:
        while result < num:
            array.append(random.randint(-50,100))
            result = result + 1;
        start = time.clock()
        maxSub.maxSubEnum2(array)
        end = time.clock()
        size = len(array) 
        runTime = runTime + (end - start)
        count = count + 1
        result = 0
        del array[:]
        array[:] = []
    count = 0
    cnt = cnt + 1
    num = num + 100
    s = 'Average time for 10 arrays of different values for algorithm 2 for size ' + str(size) + ': ' +  str(runTime/10) +'\n'
    f3.write(s)
    runTime = 0
    
count = 0
result = 0
runTime = 0
cnt = 0
num = 100
while cnt < 10:
    while count < 10:
        while result < num:
            array.append(random.randint(-50,100))
            result = result + 1;
        start = time.clock()
        maxSub.find_max_sub_array(array, 0, len(array)-1)
        end = time.clock()
        size = len(array) 
        runTime = runTime + (end - start)
        count = count + 1
        result = 0
        del array[:]
        array[:] = []
    count = 0
    cnt = cnt + 1
    num = num + 100
    s = 'Average time for 10 arrays of different values for algorithm 3 for size ' + str(size) + ': ' +  str(runTime/10) +'\n'
    f3.write(s)
    runTime = 0
    
count = 0
result = 0
runTime = 0
cnt = 0
num = 100
while cnt < 10:
    while count < 10:
        while result < num:
            array.append(random.randint(-50,100))
            result = result + 1;
        start = time.clock()
        maxSub.linearMSA(array)
        end = time.clock()
        size = len(array) 
        runTime = runTime + (end - start)
        count = count + 1
        result = 0
        del array[:]
        array[:] = []
    count = 0
    cnt = cnt + 1
    num = num + 100
    s = 'Average time for 10 arrays of different values for algorithm 4 for size ' + str(size) + ': ' +  str(runTime/10) +'\n'
    f3.write(s)
    runTime = 0
f3.close()
