'''
Ep3- InorderSuccessor
Problem - https://www.lintcode.com/problem/inorder-successor-in-bst/description
Youtube link - #pending


'''

"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.

    https://www.linkedin.com/in/qi-chen-a9841176/
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        if p is None:
           return None 
        
        #Returns the leftmost node for the given node
        def findLeftMostNode(root):
            while root.left is not None:
                root=root.left
            return root

         # has a right child
             # Go to right child and then i'll traverse left until I find a leaf
        if p.right is not None:
            return findLeftMostNode(p.right) 
        
        # doesn't have a right child
        # navigate up to the parent until you find a node whose val is greater than cur val
        else:
            stack=[]
            node = root
            while node!=p:
                stack.append(node)
                if node.val< p.val:
                    node=node.right
                else:
                    node = node.left
            for parent in stack[::-1]:
                if parent.val>p.val:
                    return parent
            return None
'''
Test cases

{8,3,10,1,6,#,14,#,#,4,7,13}
node with value 1
{8,3,10,1,6,#,14,#,#,4,7,13}
node with value 6
{8,3,10,1,6,#,14,#,#,4,7,13}
node with value 8
{8,3,10,1,6,#,14,#,#,4,7,13}
node with value 14

'''