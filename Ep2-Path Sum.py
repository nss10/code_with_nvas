'''
Ep2-Path Sum
Problem - https://leetcode.com/problems/path-sum/
Youtube link - https://www.youtube.com/watch?v=-vbAQeUeNec&feature=youtu.be 

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if root is None or root.val < 0:
            return False
      
        # base condition
        if root.left== None and root.right==None:
            return sum==root.val

        '''
            Now that we have a check for root being None in line:10,
            I could save all that hassle and just straight away return the response of left child "or" right child! 
        '''
        #recursive condition
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
