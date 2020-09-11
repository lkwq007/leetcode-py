class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        start=0
        ret=[len(S)]*len(S)
        current=len(S)
        for idx in range(len(S)):
            if S[idx]==C:
                current=0
                tmp=idx-1
                val=0
                while tmp>=start:
                    val+=1
                    if ret[tmp]<val:
                        break
                    ret[tmp]=val
                    tmp-=1
            ret[idx]=current
            current+=1
        return ret