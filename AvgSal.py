'''
1491. Average Salary Excluding the Minimum and Maximum Salary: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

Difficulty: Easy

You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.
'''

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(min(salary))
        salary.remove(max(salary))
        sum=0
        for i in salary:
            sum+=i
        return sum/len(salary)