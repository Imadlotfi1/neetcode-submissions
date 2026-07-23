class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        D={}
        s=[]
        # i will start by the same list the move to a column
        for i in range (len(board)):
            D={}   
            for j in board[i]:
                if j=='.':
                    pass
                else:
                    D[str(j)]=D.get(str(j),0)+1
    
            for l in D.values():
                if l>1:
                    return False
        # i checked the rows now i should check columns
        transposed = [list(row) for row in zip(*board)]
        for i in range (len(board)):
            D={}   
            for j in transposed[i]:
                if j=='.':
                    pass
                else:
                    D[str(j)]=D.get(str(j),0)+1
            for l in D.values():
                if l>1:
                    return False

        for i in range (0,9,3):
            for j in range (0,9,3):
                D={}
                for l in range (3):
                    for r in range(3):
                        if board[i+l][j+r]!='.':
                            D[int(board[i+l][j+r])]=D.get(int(board[i+l][j+r]),0)+1
                print(D)
                for g in D.values():
                    if g>1:
                       return False
        return True
            
            

            
        



    
                
                

        