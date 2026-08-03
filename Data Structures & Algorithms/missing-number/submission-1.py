class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        S=((len(nums)+1)*(len(nums)))//2
        L=0
        for i in nums:
            L+=i
        return S-L

