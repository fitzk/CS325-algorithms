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
        temp = []
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
        temp = []
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
            return low, high, arr[low]
        else:
            mid = (high+low)/2
            left_low,left_high,left_sum = self.find_max_sub_array(arr,low,mid)
            right_low, right_high, right_sum = self.find_max_sub_array(arr,mid+1,high)
            cross_low, cross_high, cross_sum = self.find_max_crossing_sub_array(arr,low,mid,high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        if right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


    # helper function finds Maximum crossing sub array
    def find_max_crossing_sub_array(self,arr,low,mid,high):
        left_sum = float("-inf")
        is_sum = 0
        i = mid
        max_left = float("-inf")
        max_right=float("-inf")

        while i < low:
            is_sum = is_sum + arr[i]
            if is_sum > left_sum:
                left_sum = is_sum
                max_left = i
            i = i - 1

        j = mid + 1
        right_sum = float("-inf")
        is_sum = 0
        while j < high:
            is_sum = is_sum + arr[j]

            if is_sum > right_sum:
                right_sum = is_sum
                max_right = j
            j= j + 1

        return max_left,max_right,left_sum + right_sum


	# Algorithm 4: Linear-time
    def linearMSA(arr):
        maxSoFar = 0
        maxEndingHere = 0
        for i in arr[1:]:
            maxEndingHere = maxEndingHere + i
            if maxEndingHere < 0:
                maxEndingHere = 0
            if maxSoFar < maxEndingHere:
                maxSoFar = maxEndingHere

            return maxSoFar
