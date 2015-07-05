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
import re

array = []
count = 0
result = 0
arr = []

#while count < 10:
    #array.append(random.randint(-50,100))
    #count = count + 1;

#set up command line args for inputing testData

#instance of MaxSub object
maxSub = MaxSub()

#creates a file for output
f = open('MSS_Problems.txt','r')
f2 = open('MSS_Results.txt','w')


for line in f:
    array =  map(int, re.findall(r"[-+]?\d*\-\d+|\d+", line))

    # time algorithm1
    start = time.clock()
    result, arr = maxSub.maxSubEnum(array) # function to be tested
    end = time.clock()

    #Write to file results of algorithm1
    s = 'Algorithm 1' + '\n' + str(array)+'\n' + str(arr) + '\n' + str(result) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    f2.write(s)

    #empty arr
    del arr[:]
    arr[:] = []

    # time algorithm2
    start = time.clock()
    result, arr = maxSub.maxSubEnum2(array) # function to be tested
    end = time.clock()

    #Write to file results of algorithm2
    s = 'Algorithm 2' + '\n' + str(array)+'\n' + str(arr) + '\n' + str(result) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    f2.write(s)

    #empty arr and array
    del arr[:]
    arr[:] = []

    # time algorithm3
    start = time.clock()
    low, high, result = maxSub.find_max_sub_array(array,0,len(array)-1) # function to be tested
    end = time.clock()

    #Write to file results of algorithm3
    s = 'Algorithm 3' + '\n' + str(array)+'\n' + str(arr) + '\n' + str(result) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    f2.write(s)

    #empty arr and array
    del arr[:]
    arr[:] = []
    del array[:]
    array[:] = []

# close file
f.close()
f2.close()
