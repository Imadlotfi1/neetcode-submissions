class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Prefix=[1]*len(nums)
        Post=[1]*len(nums)
        P=[1]*len(nums)
        L=[]
        # I WILL use prefix product and post product so let's go
        for i in range (len(nums)):
            for j in range(i):
                Prefix[i]*=nums[j]
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                Post[i]*=nums[j]
        for i in range (len(nums)):
            P[i]=Prefix[i]*Post[i]
            L.append(P[i])
        return L

        
        