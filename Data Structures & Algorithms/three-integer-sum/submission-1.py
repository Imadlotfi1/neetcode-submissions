class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Sort first: O(N log N)
        L=[]
        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            i,k=l+1,len(nums)-1
            
            while i<k:
                if nums[i]+nums[l]+nums[k]==0 :
                    L.append([nums[i],nums[l],nums[k]])
    
                    k-=1
                    while i < k and nums[i] == nums[i - 1]:
                        i += 1

                    while i < k and nums[k] == nums[k + 1]:
                        k -= 1        
                elif nums[i]+nums[l]+nums[k]>0 :
                    k-=1
                elif nums[i]+nums[l]+nums[k]<0 :
                   i+=1

        
        return L


                

