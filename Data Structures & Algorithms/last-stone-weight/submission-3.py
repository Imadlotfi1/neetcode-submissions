class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones_=[]
        for i in stones:
            stones_.append(-i)
        heapq.heapify(stones_)

        while len(stones_)>1:
            a=heapq.heappop(stones_)
            b=heapq.heappop(stones_)
            a=-a
            b=-b
            if a==b:
                pass
            if a>b:
                a=a-b
                heapq.heappush(stones_,-a)
        if len(stones_)==0:
            return 0
        if len(stones_)==1:
            return -stones_[0]





        