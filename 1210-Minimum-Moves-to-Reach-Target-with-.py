class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # quick check
        h=len(grid)
        w=len(grid[0])
        if grid[h-1][w-1]+grid[h-1][w-2]>0:
            return -1
        # It is guaranteed that the snake starts at empty cells.
        queue=[(0,0,0)]
        tempalte=[-1]*w
        visited_horizontal=[tempalte[:] for _ in range(h)]
        visited_vertical=[tempalte[:] for _ in range(h)]
        visited=[visited_horizontal,visited_vertical]
        step=0

        def check(y,x):
            cnt=0
            for i in range(2):
                for j in range(2):
                    if y+i>=h or x+j>=w:
                        return False
                    cnt+=grid[y+i][x+j]
            return cnt==0
        while queue:
            target=[]
            step+=1
            for y,x,state in queue:
                if y==h-1 and x==w-2 and state==0:
                    return visited[state][y][x]
                if check(y,x) and visited[1-state][y][x]==-1:
                    visited[1-state][y][x]=step
                    target.append((y,x,1-state))
                if state==0:
                    if x+1<w-1 and grid[y][x+2]==0 and visited[0][y][x+1]==-1:
                        target.append((y,x+1,state))
                        visited[state][y][x+1]=step
                    if y+1<h and grid[y+1][x]+grid[y+1][x+1]==0 and visited[0][y+1][x]==-1:
                        target.append((y+1,x,state))
                        visited[state][y+1][x]=step
                else:
                    if y+1<h-1 and grid[y+2][x]==0 and visited[state][y+1][x]==-1:
                        target.append((y+1,x,state))
                        visited[state][y+1][x]=step
                    if x+1<w and grid[y][x+1]+grid[y+1][x+1]==0 and visited[state][y][x+1]==-1:
                        target.append((y,x+1,state))                      
                        visited[state][y][x+1]=step
            queue=target
        return -1
                        