######################################################################
# Project Group:  1                                                  #
# Group Members:  Eric Cruz, Baljot Singh, Kayla Fitzsimmons         #
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
    def maxSubEnum(self, arr):
        sum = 0
        maxSum = float("-inf")
        for i in range(0, len(arr)):
            for j in range(i, len(arr)):
                for k in range(i, j + 1):
                    sum = sum + arr[k]
                if sum > maxSum:
                    maxSum = sum
                    temp = arr[i:j+1]
                sum = 0
        return maxSum, temp

    #Algorithm 2: Better Enumeration
    def maxSubEnum2(self, arr):
        sum = 0
        maxSum = float("-inf")
        for i in range(0, len(arr)):
            for j in range(i, len(arr)):
                sum = sum + arr[j]
                if sum > maxSum:
                    maxSum = sum
                    temp = arr[i:j + 1]
            sum = 0
        return maxSum, temp

    #Algorithm 3: Divide and Conquer
    def find_max_sub_array(self,arr,low,high):
        if high == low:
            return arr[low], arr[low:low+1]
        else:
            mid = (high+low)/2
            maxSum1, temp1 = self.find_max_sub_array(arr,low,mid)
            maxSum2, temp2 = self.find_max_sub_array(arr,mid+1,high)
            maxSumArray, temp3 = self.find_max_crossing_sub_array(arr,low,mid,high)
            
            if(maxSum1 >= maxSum2 and maxSum1 >= maxSumArray):
                return maxSum1, temp1
            elif(maxSum2 >= maxSum1 and maxSum2 >= maxSumArray):
                return maxSum2, temp2
            else:
                return maxSumArray, temp3


    # helper function finds Maximum crossing sub array
    def find_max_crossing_sub_array(self,arr,low,mid,high):
        left_sum = float('-inf')
        maxSum = 0
        i = mid
        while i >= low:
            maxSum = maxSum + arr[i]
            if maxSum > left_sum:
                left_sum = maxSum
                start = i
            i = i - 1
        
        maxSum = 0
        right_sum = float('-inf')
        i = mid + 1
        while i  <= high:
            maxSum = maxSum + arr[i]
            if maxSum > right_sum:
                right_sum = maxSum
                end = i
            i = i + 1
        
        return left_sum + right_sum, arr[start:end+1]

    # Algorithm 4: Linear-time
    def linearMSA(self, arr):
        
        if(len(arr) == 1):
            return arr[0], arr
        
        maxSoFar = arr[0]
        maxEndingHere = arr[0]
        start = 0
        startIndex = 0
        endIndex = -1
        for i in range(1, len(arr)):
            if maxEndingHere + arr[i] < arr[i]:
                maxEndingHere = arr[i]
                start = i
            
            else:
                maxEndingHere = maxEndingHere + arr[i]
            
            if maxSoFar < maxEndingHere:
                maxSoFar = maxEndingHere
                startIndex = start
                endIndex = i
        
        return maxSoFar, arr[startIndex:endIndex +1]
