from typing import List

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if len(colsum)<1:
            return []
        total=len(colsum)
        ret=[[0]*total,[0]*total]
        # two pass
        for idx in range(total):
            val=colsum[idx]
            if val==0:
                continue
            elif val==2:
                ret[0][idx]=1
                ret[1][idx]=1
                upper-=1
                lower-=1
            elif upper>=lower:
                ret[0][idx]=1
                upper-=1
            else:
                ret[1][idx]=1
                lower-=1
        if lower==0 and upper==0:
            return ret
        return []
        
x=Solution()
x.reconstructMatrix(5,5,[2,1,2,0,1,0,1,2,0,1])

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if len(colsum)<1:
            return []
        total=len(colsum)
        ret=[[0]*total,[0]*total]
        # two pass
        for idx,val in enumerate(colsum,0):
            if val==0:
                continue
            elif val==2:
                ret[0][idx]=1
                ret[1][idx]=1
                upper-=1
                lower-=1
        if upper<0 or lower<0:
            return []
        for idx,val in enumerate(colsum,0):
            if val==1:
                if upper>0:
                    ret[0][idx]=1
                    upper-=1
                elif lower>0:
                    ret[1][idx]=1
                    lower-=1
                else:
                    return []
        if lower==0 and upper==0:
            return ret
        return []

