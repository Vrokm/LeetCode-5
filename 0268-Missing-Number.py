'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''

from typing import List

# Using Math Formula to find sum

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n*(n+1)//2
        for n in nums:
            total -= n
        return total

# Using Bit Manipulation

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) + 1):
            res ^= i
            if i < len(nums):
                res ^= nums[i]
        return res

# Using Math Formula and in-built sum function

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        current_sum = sum(nums)
        intended_sum = len(nums) * (len(nums) + 1) // 2
        return intended_sum - current_sum

# Check Custom Input

s = Solution()
answer = s.missingNumber([0, 3, 1, 2, 5]) # 4
print(answer)