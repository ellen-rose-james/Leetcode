'''
1523. Count Odd Numbers in an Interval Range: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

Difficulty: Easy

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
'''

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2!=0 and high%2!=0:
            return (high-low+2)//2
        else:
            return (high-low+1)//2