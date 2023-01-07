'''
53. Maximum Subarray: https://leetcode.com/problems/maximum-subarray/

Difficulty: Medium

Given an integer array nums, find the subarray with the largest sum and return its sum.
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        
        sums = []
        sums.append(nums[0])
        max_sum = nums[0]
        
        for i in range(1, l):
            sums.append(max(sums[i - 1] + nums[i], nums[i]))
            max_sum = max(max_sum, sums[i])
        
        return max_sum