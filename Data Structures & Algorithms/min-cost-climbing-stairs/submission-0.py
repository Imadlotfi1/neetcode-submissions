class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*(len(cost)+1) # define dynamic programming is the cost at the top 
        # you should pay either cost[i-1] or cost[i-2] you have the right so
        # you will pay the minimum between cost[i-1] and cost[i-2]
        # in plain english dp is the minimum cost to reach i-1
        dp[1]=0
        dp[2]=min(cost[0],cost[1])
        for i in range (3,len(cost)+1):
            dp[i]=min(cost[i-1]+dp[i-1],cost[i-2]+dp[i-2])
        return dp[len(cost)]


        