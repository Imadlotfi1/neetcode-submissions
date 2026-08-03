class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_=set(nums)
        A=[]
        for i in nums:
            S=1
            if i-1 not in set_:
                while i+1 in set_:
                    S+=1
                    i+=1
                A.append(S)
        if len(A)!=0:
            return max(A)
        return 0
            



        



        


        
            
            
        
            
            

