class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,j=0,len(nums)-1
        while i<=j:
            mid=(j+i)//2
            if nums[mid]==target:
                return mid 
            elif nums[mid]>target:
                j-=1
            elif nums[mid]<target:
                i+=1
        return -1