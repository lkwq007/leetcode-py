class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        def get_pos(num):
            num-=1
            y=num//n
            x=num%n
            if y&1:
                x=n-1-x
            return n-1-y,x
        queue=[1]
        board[n-1][0]=0
        step=0
        goal=n*n
        while queue:
            step+=1
            target=[]
            for pos in queue:
                for offset in range(1,7):
                    next=pos+offset
                    if next>goal:
                        continue
                    if next==goal:
                        return step
                    y,x=get_pos(next)
                    if board[y][x]==-1:
                        board[y][x]=0
                        target.append(next)
                    elif board[y][x]>0:
                        next=board[y][x]
                        if next==goal:
                            return step
                        board[y][x]=0
                        y,x=get_pos(next)
                        if board[y][x]!=0:
                            target.append(next)
            queue=target
        return -1