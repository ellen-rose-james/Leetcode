'''
1281. Subtract the Product and Sum of Digits of an Integer: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

Difficulty: Easy

Given an integer number n, return the difference between the product of its digits and the sum of its digits.
'''
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        prod=1
        for i in str(n):
            sum+=int(i)
            prod*=int(i)
        return prod-sum