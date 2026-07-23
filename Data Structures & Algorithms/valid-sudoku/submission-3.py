class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # i will start by checking the rows 
        for i in range (len(board)):
            D={}
            for j in range (len(board)):
                
                if board[i][j]!='.':
                    D[int(board[i][j])]=D.get(int(board[i][j]),0)+1
            for l in D.values():
                if l>1:
                    return False 
        # i will check every column 
        transposed = [list(row) for row in zip(*board)]
        for i in range (len(transposed)):
            D={}
            for j in range (len(transposed)):
    
                if transposed[i][j]!='.':
                    D[int(transposed[i][j])]=D.get(int(transposed[i][j]),0)+1
            for l in D.values():
                if l>1:
                    return False 
        # i will check the boxes 
        for i in range (0,9,3):
            for j in range (0,9,3):
                D={}
                for u in range (3):
                    for o in range (3):
                        if board[i+u][j+o]!='.':
                            D[int(board[i+u][j+o])]=D.get(int(board[i+u][j+o]),0)+1
                            print(D)
                for l in D.values():
                    if l>1:
                        return False 
        return True


            
            

            
        



    
                
                

        