class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        D={}
        for i in nums:
            D[i]=D.get(i,0)+1
        for i in D:
            if D[i]>1:
                return True
        return False