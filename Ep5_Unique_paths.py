'''
Leetcode #62. Unique Paths (https://leetcode.com/problems/unique-paths/)

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(m,n,matrix=[[0 for j in range(n)] for i in range(m)]):
            if m==1 or n==1:
                matrix[m-1][n-1]=1
            if matrix[m-1][n-1]==0:
                matrix[m-2][n-1] = helper(m-1,n,matrix)
                matrix[m-1][n-2] = helper(m,n-1,matrix)
                matrix[m-1][n-1] = matrix[m-2][n-1] + matrix[m-1][n-2]
            return matrix[m-1][n-1]
        return helper(m,n)