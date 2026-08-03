class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        i,j=0,len(heights)-1
        while i<j:
            width=j-i
            height=min(heights[i],heights[j])
            max_area=max(max_area,height*width)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max_area

            
        

            
        