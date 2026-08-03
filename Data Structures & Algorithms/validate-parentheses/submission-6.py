class Solution:
    def isValid(self, s: str) -> bool:
        D={"(":")","{":"}","[":"]"}
        stack=[]
        if len(s)%2!=0:
            return False
        for i in s:
            if i in D:
                stack.append(i)
            if len(stack)==0:
                return False
            if i in D.values():
                if D[stack[-1]]==i:
                    stack.pop()
                else:
                    return False
        return len(stack)==0
                
    

