class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        low=0
        high=len(S)
        ret=[]
        for item in S:
            if item=="I":
                ret.append(low)
                low+=1
            elif item=="D":
                ret.append(high)
                high-=1
        ret.append(high)
        return ret