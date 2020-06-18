class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board)<1 or len(board[0])<1:
            return
        h=len(board)
        w=len(board[0])
        # first pass, scan boundary and dfs
        direction=[(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(y,x):
            if board[y][x]=="O":
                board[y][x]="A"
                for y_offset,x_offset in direction:
                    y_next=y+y_offset
                    x_next=x+x_offset
                    if y_next<0 or y_next>=h or x_next<0 or x_next>=w:
                        continue
                    dfs(y_next,x_next)
            return
        for x in range(w):
            dfs(0,x)
            dfs(h-1,x)
        for y in range(h):
            dfs(y,0)
            dfs(y,w-1)
        for y in range(h):
            for x in range(w):
                if board[y][x]=="O":
                    board[y][x]="X"
                elif board[y][x]=="A":
                    board[y][x]="O"
        return