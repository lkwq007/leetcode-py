class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        part=sum(rolls)
        total=mean*(len(rolls)+n)
        total-=part
        if n<=total<=6*n:
            ret=[1]*n
            total-=n
            idx=0
            while total>0:
                if total>=5:
                    ret[idx]+=5
                    total-=5
                else:
                    ret[idx]+=total
                    total=0
                idx+=1
            return ret
        return []