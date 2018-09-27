'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

'''


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        1 3 1 
        1 5 1
        4 2 1 <--- start from here
        
        you can get to it from the top 1 or the left 2
        similarly we go on till we reach the goal state of the first cell
        
        Possible memoization: path to a node will always be optimal and can be stored
        {Optimal substructure property}
        
        '''
        # Initialize storage
        optGrid = [[10000 for x in range(len(grid[0]))] for y in range(len(grid))]
        return self.minPathHelper(grid, optGrid, len(grid) - 1, len(grid[0]) - 1)
        
        ## Need to memoize as time limit exceeds
    def minPathHelper(self, grid, optGrid, x, y):
        
        if optGrid[x][y] != 10000:
            return optGrid[x][y]
        # Base case (goal)
        if x == 0 and y == 0:
            return grid[x][y]
        
        path1 = 100000
        path2 = 100000
        
        # Go left 
        if y - 1 >= 0 and y - 1 < len(grid[0]):
            path1 = self.minPathHelper(grid, optGrid, x, y - 1)
        
        # Go up
        if x - 1 >= 0 and x - 1 < len(grid):
            path2 = self.minPathHelper(grid, optGrid, x - 1 , y)
        
        optGrid[x][y] = min(path1, path2) + grid[x][y]
        return optGrid[x][y]