class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # i will try the bucket algorithm since in a list with length N 
        # so we will create an array that indexes are frequences 
        D={}
        A=[]
        L=[]
        for i in nums:
            D[i]=D.get(i,0)+1
        for i in range(len(nums)+1):
            L.append([])
        for i in D:
            L[D[i]].append(i)
        for i in range(len(L)-1,0,-1):# start from 0 to len
            for n in L[i]:
                A.append(n)
                if len(A)==k:
                    return A




        