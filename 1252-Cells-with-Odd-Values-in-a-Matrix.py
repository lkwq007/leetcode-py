class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows=[0]*n
        cols=[0]*m
        for r,c in indices:
            rows[r]+=1
            cols[c]+=1
        ret=0
        for y in range(n):
            for x in range(m):
                if (rows[y]+cols[x])&1:
                    ret+=1
        return ret