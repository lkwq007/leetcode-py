class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        template=[0]*10
        row=[template[:] for _ in range(9)]
        col=[template[:] for _ in range(9)]
        square=[template[:] for _ in range(9)]
        lst=[]
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    val=int(board[i][j])
                    row[i][val]=1
                    col[j][val]=1
                    square[i//3*3+j//3][val]=1
                else:
                    lst.append((i,j))
        def probe(idx):
            if idx==len(lst):
                return True
            y,x=lst[idx]
            for i in range(1,10):
                if row[y][i]==0 and col[x][i]==0 and square[y//3*3+x//3][i]==0:
                    board[y][x]=str(i)
                    row[y][i]=1
                    col[x][i]=1
                    square[y//3*3+x//3][i]=1
                    if probe(idx+1):
                        return True
                    row[y][i]=0
                    col[x][i]=0
                    square[y//3*3+x//3][i]=0
                    board[y][x]="."
            return False
        probe(0)
        return 

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        template=[0]*10
        row=[template[:] for _ in range(9)]
        col=[template[:] for _ in range(9)]
        square=[template[:] for _ in range(9)]
        lst=[]
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    val=int(board[i][j])
                    row[i][val]=1
                    col[j][val]=1
                    square[i//3*3+j//3][val]=1
                else:
                    lst.append((i,j))
        row_sum=list(map(sum,row))
        col_sum=list(map(sum,col))
        square_sum=list(map(sum,square))
        def key(item):
            y,x=item
            return -max(row_sum[y],col_sum[x],square_sum[y//3*3+x//3])
        lst.sort(key=key)
        def probe(idx):
            if idx==len(lst):
                return True
            y,x=lst[idx]
            for i in range(1,10):
                if row[y][i]==0 and col[x][i]==0 and square[y//3*3+x//3][i]==0:
                    board[y][x]=str(i)
                    row[y][i]=1
                    col[x][i]=1
                    square[y//3*3+x//3][i]=1
                    if probe(idx+1):
                        return True
                    row[y][i]=0
                    col[x][i]=0
                    square[y//3*3+x//3][i]=0
                    board[y][x]="."
            return False
        probe(0)
        return 