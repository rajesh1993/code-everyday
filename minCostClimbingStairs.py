'''

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
'''

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        '''
        Input: Array containing costs at each ith step
        Start at 0th or 1st step. Can jump 1 or two steps at a time.
        Output: Min cost to reach top
        '''
        memo = [10000 for x in range(len(cost))]
        return min(self.minHelper(cost, memo, 0), self.minHelper(cost, memo, 1))
    
    def minHelper(self, cost, memo, step):  # [10, 15, 20], [10k, 10k, 10k], 1
        n = len(cost)
        # print(step, memo)
        if step == n:
            return 0
        if memo[step] != 10000:
            return memo[step]
        
        if step == n - 1:
            return cost[step]
        path1 = 10000
        path2 = 10000
        # Jump one step
        if step + 1 <= n: # 2 < 3
            path1 = self.minHelper(cost, memo, step + 1)
        # Jump two steps
        if step + 2 <= n:
            path2 = self.minHelper(cost, memo, step + 2)
        memo[step] = min(path1, path2) + cost[step]
        return memo[step]
        