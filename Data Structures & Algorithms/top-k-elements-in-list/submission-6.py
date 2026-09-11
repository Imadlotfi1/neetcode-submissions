class Solution:
    import heapq 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        L=[]
        D={}
        for i in nums:
            D[i]=D.get(i,0)+1
        for i in D:
            heapq.heappush(heap,(-D[i],i))
        for i in range (k):
            x=heapq.heappop(heap)
            L.append(x[1])
        return L 



        
            
        


        