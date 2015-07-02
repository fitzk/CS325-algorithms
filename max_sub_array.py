######################################################################
# Project Group:  1                                                  #
# Group Members:  Eric Cruz, Baljot Sighn, Kayla Fitzsimmons         #
# Course:         CS325-400                                          #
# Assignment:     Project 1                                          #
# File:           max_sub_array.py                                   #
# Description:    Object that contains Four algorithms that solve    #
#                 the max sub array problem                          #
######################################################################
class MaxSub(object):
    # Algorithm 1: Enumeration
    #   enumeration for max subarray
    #   evaluates every possible solution
    #   analysis (O(n^2) pairs) x (O(n) time to compute each sum)= O(n^3) time

    # def MaxSubEnum(a):
        # for each pair(i,j) with 1 <= i <= j <= n
        #   compute a[i]+a[i+1]+...+a[j-1]+a[j]
        #   keep max sum found so far
        # keep max sum found




    #Algorithm 2: Better Enumeration
