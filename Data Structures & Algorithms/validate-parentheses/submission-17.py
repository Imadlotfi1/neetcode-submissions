class Solution:
    def isValid(self, s: str) -> bool:
        D={"(":")","{":"}","[":"]"}
        stack=[]
        if len(s)%2!=0:
            return False
        for i in s:
            if i in D:
                stack.append(i)
            elif len(stack)==0:
                return False
            elif i not in D and len(stack)!=0 and  D[stack[-1]]!=i:
                return False
            elif i not in D and len(stack)!=0 and  D[stack[-1]]==i:
                stack.pop()   
        return len(stack)==0
        
    

