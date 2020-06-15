class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if len(grid)<1 or len(grid[0])<1:
            return 0
        def count(lst):
            left=0
            right=len(lst)
            while left<right:
                middle=left+(right-left)//2
                if lst[middle]>=0:
                    left=middle+1
                else:
                    right=middle
            return len(lst)-left
        return sum(map(count,grid))
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt=0
        row=0
        height=len(grid)
        for idx in range(len(grid[0])-1,-1,-1):
            while row<height and grid[row][idx]>=0:
                row+=1
            if row>=height:
                break
            cnt+=height-row
        return cnt            
