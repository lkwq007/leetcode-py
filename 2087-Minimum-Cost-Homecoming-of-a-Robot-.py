class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        ret=0
        yoffset=1 if startPos[0]<homePos[0] else -1
        xoffset=1 if startPos[1]<homePos[1] else -1
        for y in range(startPos[0],homePos[0],yoffset):
            ret+=rowCosts[y+yoffset]
        for x in range(startPos[1],homePos[1],xoffset):
            ret+=colCosts[x+xoffset]
        return ret