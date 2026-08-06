class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        D={'+':1,'-':2,'*':3,'/':4}
        stack=[]
        S=0
        if len(tokens)==1:
            return int(tokens[0])
        for i in tokens:
            if i not in D:
                stack.append(i)
            if i in D:
                a=stack.pop()
                b=stack.pop()
                a=int(a)
                b=int(b)
                if i == '+':
                    S = a + b
                elif i == '-':
                    S = b - a
                elif i == '*':
                    S = a * b
                elif i == '/':
                   S = int(b / a)
                stack.append(S)
        return S
                    
            
