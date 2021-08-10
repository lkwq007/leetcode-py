class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        board[rMove][cMove]="X"
        bcolor="W" if color=="B" else "B"
        h=len(board)
        w=len(board[0])
        offset=[1,0,-1]
        for yo in offset:
            for xo in offset:
                if yo==0 and xo==0:
                    continue
                y0=rMove+yo
                x0=cMove+xo
                cnt=0
                flag=False
                while 0<=y0<h and 0<=x0<w:
                    if board[y0][x0]==color:
                        if cnt>0:
                            flag=True
                        break
                    elif board[y0][x0]==bcolor:
                        cnt+=1
                    else:
                        break
                    y0+=yo
                    x0+=xo
                if flag:
                    return True
        return False