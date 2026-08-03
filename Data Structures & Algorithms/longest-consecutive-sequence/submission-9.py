class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_=set(nums)
        max_streak=0
        for i in nums:
            S=1
            if i-1 not in set_:
                while i+1 in set_:
                    S+=1
                    i+=1
                max_streak=max(max_streak,S)
        return max_streak
            



        



        


        
            
            
        
            
            

