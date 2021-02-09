'''

Leetcode #287. Find the Duplicate Number (https://leetcode.com/problems/find-the-duplicate-number/)

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [1,1]
Output: 1

Example 4:
Input: nums = [1,1,2]
Output: 1
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        '''
        #iterate through the list of nums
        #swap the number i with the number in [i-1]th position
        
        Time complexity - O(n)
        Space complexity - O(1)
        '''
        #Code
        for i in range(len(nums)):
            while nums[i] != i+1 :
                val = nums[i]
                if val == nums[val-1]:
                    break
                nums[val-1], nums[i]  = val, nums[val-1]
        return nums[-1]
        

       
        '''
        #Time complexity = O(n)
        #Space complexity = O(n)
        '''

        '''
        #Code
        num_set = set()
        for num in nums:
            if num in num_set:
                return num
            num_set.add(num)
        
        
        '''
            