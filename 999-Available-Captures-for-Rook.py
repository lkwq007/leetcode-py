class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        h=len(board)
        w=len(board[0])
        for y in range(h):
            for x in range(w):
                if board[y][x]=="R":
                    y0=y
                    x0=x
                    break
        offset=[(0,1),(1,0),(-1,0),(0,-1)]
        ret=0
        for y_offset,x_offset in offset:
            y1=y0+y_offset
            x1=x0+x_offset
            while 0<=y1<h and 0<=x1<w and board[y1][x1]!="B":
                if board[y1][x1]=="p":
                    ret+=1
                    break
                y1=y1+y_offset
                x1=x1+x_offset
        return ret