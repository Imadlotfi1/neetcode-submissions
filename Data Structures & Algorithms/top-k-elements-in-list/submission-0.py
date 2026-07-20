class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # so i will talk like in interview
        # this problem to solve i need heaps which is a tree
        # tree represented by parents and theire sons 
        # python has min heap by default 
        heap=[]
        D={}
        A=[]
        for i in nums:
            D[i]=D.get(i,0)+1
        for key,value in D.items():
            heapq.heappush(heap,(-value,key))
        for i in range (k):
            l=heapq.heappop(heap)
            A.append(l[1])
        return A


        