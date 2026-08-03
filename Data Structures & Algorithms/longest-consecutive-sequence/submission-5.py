class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        D={}
        # we start by defining the first element 
        A=[]
        B=[]
        set_=set(nums)
        for i in nums:
            if i-1 not in set_:
                A.append(i)
        for i in nums:
            D[i]=D.get(i,0)+1
        for i in A:
            S=1
            while i+1 in D:
                S+=1
                i+=1
            B.append(S)
        if len(B)!=0:
            b=max(B)
            return b
        else:
            return 0
        



        


        
            
            
        
            
            

