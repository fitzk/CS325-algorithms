######################################################################
# Project Group:  1                                                  #
# Group Members:  Eric Cruz, Baljot Singh, Kayla Fitzsimmons         #
# Course:         CS325-400                                          #
# Assignment:     Project 1                                          #
# File:           timer.py                                           #
# Description:    Calculates runtime for max sub array algorithms    #
######################################################################
from max_sub_array import MaxSub

#set up command line args for inputing testData

#instance of MaxSub object
maxSub = MaxSub()

#creates a file for output
f = open('output','w')

#header for output
header = Size of Input + '\t'+ Maximum Subarray +'\t'+ Run Time +'\n'
h_value = str(header)
f.write(h_value)

# time algorithm
start = time.time()
result = maxSub.maxSubEnum() # function to be tested
end = time.time()

# format output
r = #repr(size of input) + '\t'+ repr(result) +'\t'+repr(end - start)+'\n'
r_value = str(r)

# write result to file
f.write(r_value)

# close file
f.close()
