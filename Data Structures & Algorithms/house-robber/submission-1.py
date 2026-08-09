class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i] is the max that i will get if i rob from door 1 to i 
        dp=[0]*(len(nums)+1)
        if len(nums)==1:
            return nums[0]
        dp[0]=nums[0]
        dp[1]=max(dp[0],nums[1])

        #dp[2]=max(dp[1],dp[0]+nums[2])
        #dp[len(nums)-1]=max(dp[len(nums)-2],dp[len(nums)-3]+nums[len(nums)-1])
        for i in range (2,len(nums)):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return max(dp)