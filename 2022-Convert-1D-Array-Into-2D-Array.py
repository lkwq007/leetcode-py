class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!=len(original):
            return []
        ret=[[0]*n for _ in range(m)]
        idx=0
        for y in range(m):
            for x in range(n):
                ret[y][x]=original[idx]
                idx+=1
        return ret