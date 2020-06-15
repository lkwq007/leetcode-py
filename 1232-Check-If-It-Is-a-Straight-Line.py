class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)<2:
            return False
        if len(coordinates)==2:
            return True
        pos0=coordinates[0]
        pos1=coordinates[1]
        for idx in range(2,len(coordinates)):
            cur=coordinates[idx]
            if (pos0[0]-pos1[0])*(pos0[1]-cur[1])!=(pos0[0]-cur[0])*(pos0[1]-pos1[1]):
                return False
        return True