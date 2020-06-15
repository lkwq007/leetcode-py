class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        row=m
        col=n
        for a,b in ops:
            row=min(row,a)
            col=min(col,b)
        return row*col
