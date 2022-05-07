class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        x=[(ax1,0),(ax2,0),(bx1,1),(bx2,1)]
        y=[(ay1,0),(ay2,0),(by1,1),(by2,1)]
        x.sort()
        y.sort()
        total=(ax2-ax1)*(ay2-ay1)+(bx2-bx1)*(by2-by1)
        if x[0][1]==x[1][1] or y[0][1]==y[1][1]:
            return total
        return total-(x[2][0]-x[1][0])*(y[2][0]-y[1][0])