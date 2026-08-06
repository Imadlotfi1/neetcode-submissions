class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j=0,len(matrix)-1
        while i <= j:
            r=(j+i)//2
            if matrix[r][0] <=target<=matrix[r][len(matrix[r])-1]:
                l,k=0,len(matrix[0])-1
                while  l <= k:
                    u=(k+l)//2
                    if matrix[r][u]==target:
                        return True
                    elif matrix[r][u]>target:
                        k-=1
                    elif matrix[r][u]<target:
                        l+=1
                return False
            elif matrix[r][0]>target :
                j=r-1
            elif matrix[r][0]<target:
                i=r+1
        return False
    
            # now we know each row with r so we will search on it with binary saerch
    



