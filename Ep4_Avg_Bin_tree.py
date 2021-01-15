# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        if root is None:
            return []
        #add root node
        nodeList=[root]
        
        #for each iteration
            #I take all the elements from the list between the start and endIndex
                #I'll add it's kids to the list
                #Take the average of all the elements
            #add it to the result list
            #if no new elements added in an iteration, break

        #return resultList
        start,end=0,len(nodeList)
        result_list=[]
        while True:
            #next_level_count=0 # Got rid of this variable
            sum_val,count=0,0 #count is number of elements iterated in the for loop
            for node in nodeList[start:end]:
                if node is not None:
                    sum_val+=node.val
                    count+=1
                    nodeList.append(node.left)           
                    nodeList.append(node.right)
            
            result_list.append(sum_val/count)
            if end==len(nodeList):
                break
                
            start=end
            end = len(nodeList)
        return result_list