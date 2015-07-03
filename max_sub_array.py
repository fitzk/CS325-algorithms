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

    # def MaxSubEnum(a):
        # for each pair(i,j) with 1 <= i <= j <= n
        #   compute a[i]+a[i+1]+...+a[j-1]+a[j]
        #   keep max sum found so far
        # keep max sum found

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
    def findMaxSubArray(self,arr,low,high):
        if high == low:
            return low, high, arr[low]
        else:
            mid = (low + high) // 2
            leftLow,leftHigh,leftSum = self.findMaxSubArray(arr,low,mid)
            rightLow, rightHigh, rightSum = self.findMaxSubArray(arr,mid+1, high)
            crossLow, crossHigh, crossSum = self.findMaxCrossingSubArray(arr,low,mid,high)

        if leftSum >= rightSum and leftSum >= crossSum:
            return leftLow, leftHigh, leftSum
        if rightSum >= leftSum and rightSum >= crossSum:
            return rightLow, rightHigh, rightSum
        else:
            return crossLow, crossHigh, crossSum

    # helper function finds Maximum crossing sub array
    def findMaxCrossingSubArray(self,arr,low,mid,high):
        leftSum = float("-inf")
        isSum = 0
        i = mid
        maxLeft = float("-inf")
        maxRight=float("-inf")

        while i < low:
            isSum = isSum + arr[i]
            if isSum > leftSum:
                leftSum = isSum
                maxLeft = i
            i = i - 1

        j = mid + 1
        rightSum = float("-inf")
        isSum = 0
        while j < high:
            isSum = isSum + arr[j]

            if isSum > rightSum:
                rightSum = isSum
                maxRight = j
            j= j + 1

        return maxLeft,maxRight,leftSum+rightSum
