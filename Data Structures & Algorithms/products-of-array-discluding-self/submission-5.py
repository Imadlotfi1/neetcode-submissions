class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1]*len(nums)
        prefix=[1]*len(nums)
        suffix=[1]*len(nums)
        a = nums[0]
        
        prefix[0]=1
        prefix[1]=prefix[0]*nums[0]
        for i in range (2,len(nums)):
            a*=nums[i-1]
            prefix[i]=a

        b=1
        for i in range (len(nums)-1,-1,-1):
            suffix[i]=b
            b*=nums[i]
        for i in range (len(nums)):
            output[i]=suffix[i]*prefix[i]
        return output


            
            

        
        