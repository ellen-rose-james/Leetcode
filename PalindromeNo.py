'''
9. Palindrome Number: https://leetcode.com/problems/palindrome-number/

Difficulty: Easy

Given an integer x, return true if x is a palindrome, and false otherwise.

'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr=str(x)
        return xstr[::-1]==xstr