class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        minval=grid[0][0]
        h=len(grid)
        w=len(grid[0])
        for i in range(h):
            for j in range(w):
                item=grid[i][j]
                minval=min(minval,item)
        lst=[0]*10001
        maxval=0
        for i in range(h):
            for j in range(w):
                item=grid[i][j]-minval
                if item%x!=0:
                    return -1
                lst[item//x]+=1
                maxval=max(maxval,item//x)
        left=0
        right=maxval
        ret=0
        while left<right:
            if lst[left]<lst[right]:
                ret+=lst[left]
                lst[left+1]+=lst[left]
                lst[left]=0
                left+=1
            else:
                ret+=lst[right]
                lst[right-1]+=lst[right]
                lst[right]=0
                right-=1
        return ret