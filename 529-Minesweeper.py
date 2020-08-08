class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        y=click[0]
        x=click[1]
        h=len(board)
        w=len(board[0])
        def rec_click(y,x):
            if board[y][x]=="M":
                board[y][x]="X"
            elif board[y][x]=="E":
                cnt=0
                for y_next in range(y-1,y+2):
                    for x_next in range(x-1,x+2):
                        if 0<=y_next<h and 0<=x_next<w and board[y_next][x_next]=="M":
                            cnt+=1
                board[y][x]="B" if cnt==0 else str(cnt)
                if cnt==0:
                    for y_next in range(y-1,y+2):
                        for x_next in range(x-1,x+2):
                            if 0<=y_next<h and 0<=x_next<w and board[y_next][x_next]=="E":
                                rec_click(y_next,x_next)
            return
        rec_click(y,x)
        return board

