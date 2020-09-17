class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # simulate and treat whole insturction as one inst
        y=0
        x=0
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        idx=0
        for item in instructions:
            if item=="G":
                y+=directions[idx][0]
                x+=directions[idx][1]
            elif item=="L":
                idx=(idx-1+4)%4
            else:
                idx=(idx+1)%4
        return idx!=0 or y==0 and x==0