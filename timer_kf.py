######################################################################
# Project Group:  1                                                  #
# Group Members:  Eric Cruz, Baljot Singh, Kayla Fitzsimmons         #
# Course:         CS325-400                                          #
# Assignment:     Project 1                                          #
# File:           timer.py                                           #
# Description:    Calculates runtime for max sub array algorithms    #
######################################################################
from max_sub_array import MaxSub
import sys
import re
import fileinput
import time

#function to run
functionNum = 3
#set up command line args for inputing testData

def testFunction(arr):
        if functionNum == 1:
            start = time.clock()
            result,temp = maxSub.maxSubEnum(arr)
            end = time.clock()
            r = '\t\t\t'+repr(len(arr)) + '\t\t\t'+ repr(result) +"="+ repr(temp)+'\t\t\t'+ repr(end - start)+'\n'

        if functionNum == 2:
            start = time.clock()
            result,temp = maxSub.maxSubEnum2(arr)
            end = time.clock()
            r = '\t\t\t'+repr(len(arr)) + '\t\t\t'+ repr(result) + '='+ repr(temp)+'\t\t\t'+ repr(end - start)+'\n'

        if functionNum == 3:
            start = time.clock()
            low, high, result = maxSub.findMaxSubArray(arr,1,len(arr)-1)
            end = time.clock()
            r = '\t\t\t'+ repr(len(arr)) + '\t\t\t'+"["+repr(low)+","+repr(high)+"]"+"="+repr(result)+'\t\t\t'+ repr(end - start)+'\n'

        if functionNum == 4:
            start = time.clock()
            result = None #Insert 4th function call here
            end = time.clock()
            r = repr(len(arr)) + '\t\t'+ repr(result) + '\t\t'+ repr(temp)+'\t\t'+ repr(end - start)+'\n'
        # format output
        r_value = str(r)

        # write result to file
        f.write(r_value)


#instance of MaxSub object
maxSub = MaxSub()

#creates a file for output
output = "output2.txt"
f = open(output,'w')

#header for output
header = "Size of Input" + '\t\t\t'+ "Maximum Sub-Array" +'\t\t\t'+ "Run Time" +'\n'
h_value = str(header)
f.write(h_value)
# time algorithm
# for line in fileinput.input():
#     testFunction(repr(line))

testFunction([1,2,-5,4,6])

f.close()
