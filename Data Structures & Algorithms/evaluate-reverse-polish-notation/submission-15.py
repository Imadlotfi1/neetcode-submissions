class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        if len(tokens)==1:
            return int(tokens[0])
  
        S=1
        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            elif i in '+-*/':
                a=stack.pop() # the last element 
                b=stack.pop() #last element Lifo we add the element at the end
                a=int(a)
                b=int(b)
                if i=='+':
                    S=a+b
                elif i=='-':
                    S=b-a
                elif i=='*':
                    S=b*a
                elif i=='/':
                    S=int(b/a)
                stack.append(S)
        return S
                

                    
            
