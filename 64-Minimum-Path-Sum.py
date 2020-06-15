from typing import List
def dump(lstLst):
    print("[")
    for item in lst:
        print(item)
    print("]")
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid)<1:
            return 0
        if len(grid[0])<1:
            return 0
        h=len(grid)
        w=len(grid[0])
        print(h,w)
        # can only move right or down
        # a simple scan may work
        # consider it as two pass
        def scan_right(y0,x0):
            if y0==0:
                acc=0
                for x in range(0,w):
                    if grid[y0][x]>=0:
                        grid[y0][x]=acc-grid[y0][x]
                    acc=grid[y0][x]
            else:
                for x in range(x0,w):
                    left=grid[y0][x-1]
                    top=grid[y0-1][x]
                    if grid[y0][x]>=0:
                        grid[y0][x]=max(left,top)-grid[y0][x]                        
        
        def scan_down(y0,x0):
            if x0==0:
                acc=0
                for y in range(0,h):
                    if grid[y][x0]>=0:
                        grid[y][x0]=acc-grid[y][x0]
                    acc=grid[y][x0]
            else:
                for y in range(y0,h):
                    left=grid[y][x0-1]
                    top=grid[y-1][x0]
                    if grid[y][x0]>=0:
                        grid[y][x0]=max(left,top)-grid[y][x0]
        first_pass=scan_right
        second_pass=scan_down
        if w<h:
            first_pass,second_pass=second_pass,first_pass
        x0=0
        y0=0
        while x0<w-1 and y0<h-1:
            first_pass(y0,x0)
            second_pass(y0,x0)
            x0+=1
            y0+=1
        first_pass(y0,x0)
        return -grid[h-1][w-1]

x=Solution()
lst=[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
lst=[[6,2,4,4,6,2,2,9],[6,4,5,1,0,8,3,5],[9,3,0,5,9,8,1,7],[7,9,9,3,1,9,1,9],[3,7,5,0,0,8,9,8],[4,6,9,4,4,3,0,4],[6,2,9,7,2,3,5,9],[2,4,3,5,5,6,5,9],[3,0,1,5,0,0,4,5],[9,3,9,3,8,1,7,6]]
print(x.minPathSum(lst))