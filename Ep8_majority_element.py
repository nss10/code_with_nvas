'''
Leetcode #169. Majority Element (https://leetcode.com/problems/majority-element/)

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Time complexity O(nlogn)
        Space complexity(O(1)) 
        # sort the list
        # identify the middle element 
        '''
        
        #Code
        nums.sort()
        n = len(nums)
        return nums[n//2]
        
        
                
        #length of the list
        #iterate through the list to find out frequency of each element. 
        # if freq of any element is greater than int(n/2) then return that element
       
        ''' 
        # time complexity is O(n)
        # Space complexity is O(n) 
        '''
        
        '''
        #Code
        element_counter = {}
        n = len(nums)
        for num in nums:
            if num in element_counter:
                element_counter[num]+=1
            else:
                element_counter[num]=1
            if element_counter[num] > n//2:
                return num
        return -1
        '''
        
        
                