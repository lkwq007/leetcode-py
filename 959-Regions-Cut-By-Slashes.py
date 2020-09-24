class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n=len(grid)
        total=0
        mapping={" ":0,"/":1,"\\":2}
        # upper/lower
        direction=[
            [(1,0),(-1,0),(0,1),(0,-1)],
            [(1,0),(-1,0),(0,1),(0,-1)]
            [(-1,0),(0,-1)],
            [(1,0),(1,0)],
            [(-1,0),(0,1)],
            [(1,0),(-1,0)]
            ]
        def dfs(y0,x0,dir):
            