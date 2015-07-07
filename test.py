######################################################################
# Project Group:  1                                                  #
# Group Members:  Eric Cruz, Baljot Singh, Kayla Fitzsimmons         #
# Course:         CS325-400                                          #
# Assignment:     Project 1                                          #
# File:           test.py                                            #
# Description:    Test max sub array algorithms for correctess       #
######################################################################
from max_sub_array import MaxSub

import time
import re
import sys

array = []
count = 0
result = 0
arr = []

#instance of MaxSub object
maxSub = MaxSub()

#creates a file object for input and output
try:
    f = open('MSS_Problems.txt','r')
except IOError:
    print 'Error in opening file MSS_Problems.txt'
    sys.exit(-1)

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

    #empty arr 
    del arr[:]
    arr[:] = []

    # time algorithm3
    start = time.clock()
    result, arr = maxSub.find_max_sub_array(array,0,len(array) - 1) # function to be tested
    end = time.clock()

    #Write to file results of algorithm3
    s = 'Algorithm 3' + '\n' + str(array)+'\n' + str(arr) + '\n' + str(result) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    f2.write(s)
    
    #empty arr 
    del arr[:]
    arr[:] = []

    # time algorithm4
    start = time.clock()
    result, arr = maxSub.linearMSA(array) # function to be tested
    end = time.clock()

    #Write to file results of algorithm4
    s = 'Algorithm 4' + '\n' + str(array)+'\n' + str(arr) + '\n' + str(result) + '\n' + 'Time Taken: ' + str(end - start) + '\n' + '\n'
    f2.write(s)

    #empty arr and array
    del arr[:]
    arr[:] = []
    del array[:]
    array[:] = []

# close file
f.close()
f2.close()
