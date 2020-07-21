class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        h=len(board)
        w=len(board[0])
        first=word[0]
        total=len(word)
        direction=[[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(y,x,i):
            if i==total:
                return True
            if 0<=y<h and 0<=x<w:
                if board[y][x]==word[i]:
                    board[y][x]=""
                    for y_offset,x_offset in direction:
                        if dfs(y+y_offset,x+x_offset,i+1):
                            return True
                    board[y][x]=word[i]
            return False
        for y in range(h):
            for x in range(w):
                if board[y][x]==first:
                    if dfs(y,x,0):
                        return True
        return False