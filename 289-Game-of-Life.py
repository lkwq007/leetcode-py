class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # two pass and stored in-place
        if len(board)<1 or len(board[0])<1:
            return
        h=len(board)
        w=len(board[0])
        direction=[-1,0,1]
        def check(y,x):
            total=0
            for y_offset in direction:
                for x_offset in direction:
                    if y_offset==0 and x_offset==0:
                        continue
                    y_next=y+y_offset
                    x_next=x+x_offset
                    if y_next<0 or y_next>=h or x_next<0 or x_next>=w:
                        continue
                    total+=board[y_next][x_next]&1
            return total
        for y in range(h):
            for x in range(w):
                cnt=check(y,x)
                if board[y][x]&1 and 2<=cnt<=3 or (board[y][x]&1==0 and cnt==3):
                    board[y][x]=board[y][x]|2
        for y in range(h):
            for x in range(w):
                board[y][x]=board[y][x]>>1
