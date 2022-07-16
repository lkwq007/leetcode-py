class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        h=len(board)
        w=len(board[0])
        def check(y0,x0):
            ref=word
            offset=[(0,1),(1,0),(0,-1),(-1,0)]
            for yo,xo in offset:
                y=y0-yo
                x=x0-xo
                if 0<=y<h and 0<=x<w and board[y][x]!="#":
                    continue
                cnt=0
                for i in range(len(ref)):
                    y+=yo
                    x+=xo
                    if 0<=y<h and 0<=x<w:
                        if board[y][x]==ref[i] or board[y][x]==" ":
                            cnt+=1
                        else:
                            break
                    else:
                        break
                y+=yo
                x+=xo
                if cnt==len(ref) and not (0<=y<h and 0<=x<w and board[y][x]!="#"):
                    return True
            return False
        for y in range(h):
            for x in range(w):
                if board[y][x] in (word[0]," "):
                    if check(y,x):
                        return True
        return False