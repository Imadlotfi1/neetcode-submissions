class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range (len(nums)):
            if nums[i]-target==0:
                return i
        return -1