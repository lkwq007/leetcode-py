class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        # TLE
        h=len(grid)
        w=len(grid[0])
        template=[0]*w
        ret=0
        grid2=[template[:] for _ in range(h)]
        record={}
        for i in range(h):
            for j in range(w):
                val=grid[i][j]
                if val in record:
                    cnt=list(record[val])
                else:
                    cnt=[0]*3
                    tmp=val
                    while val>0:
                        if val%10==0:
                            cnt[0]+=1
                            val=val//10
                        elif val%5==0:
                            cnt[1]+=1
                            val=val//5
                        elif val%2==0:
                            cnt[2]+=1
                            val=val//2
                        else:
                            break
                    record[tmp]=tuple(cnt)
                grid[i][j]=cnt[:]
                if i>0:
                    for k in range(3):
                        grid[i][j][k]+=grid[i-1][j][k]
                grid2[i][j]=cnt[:]
                if j>0:
                    for k in range(3):
                        grid2[i][j][k]+=grid2[i][j-1][k]
                ret=max(ret,grid[i][j][0]+min(grid[i][j][1],grid[i][j][2]))
                ret=max(ret,grid2[i][j][0]+min(grid2[i][j][1],grid2[i][j][2]))
        if w==1 or h==1:
            return ret
        for i in range(h):
            grid[i].append([0,0,0])
            grid2[i].append([0,0,0])
        grid.append([[0]*3]*w)
        grid2.append([[0]*3]*w)
        cur=[0,0,0]
        for i in range(h):
            for j in range(w):
                for k in range(3):
                    cur[k]=grid2[i][j-1][k]+grid[i][j][k]
                ret=max(ret,cur[0]+max(min(cur[1],cur[2]),0))
                for k in range(3):
                    cur[k]=grid2[i][-2][k]-grid2[i][j][k]+grid[i][j][k]
                ret=max(ret,cur[0]+max(min(cur[1],cur[2]),0))
                for k in range(3):
                    cur[k]=grid2[i][j][k]+grid[-2][j][k]-grid[i][j][k]
                ret=max(ret,cur[0]+max(min(cur[1],cur[2]),0))
                for k in range(3):
                    cur[k]=grid2[i][-2][k]-grid2[i][j-1][k]+grid[-2][j][k]-grid[i][j][k]
                ret=max(ret,cur[0]+max(min(cur[1],cur[2]),0))
        return ret