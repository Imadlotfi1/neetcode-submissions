class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        D={}
        A={}
        for i in s:
            D[i]=D.get(i,0)+1
        for i in t:
            A[i]=A.get(i,0)+1
        if A==D:
            return True
        return False
        
            