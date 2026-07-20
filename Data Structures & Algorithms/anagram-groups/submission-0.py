class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # the idea is we sorted the arrays then we regoupe the equality 
        # my idea is to stock the str in a hash map as key then its 
        #sorted str 
        D={}
        A=[]
        for str in strs:
            l="".join(sorted(str))
            if l not in D:
                D[l]=[]
                D[l].append(str)
            else:
                D[l].append(str)
        for i in D:
            A.append(D[i])
        return A
        




            
