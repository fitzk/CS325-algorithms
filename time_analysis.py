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
count = 0
result = 0
runTime = 0
f3 = open('Time_Results.txt','a')
while count < 10:
    while result < 500:
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
s = 'Average time for 10 arrays of different values for algorithm 1 for size ' + str(size) + ': ' +  str(runTime/10) +'\n'
f3.write(s)
f3.close()
