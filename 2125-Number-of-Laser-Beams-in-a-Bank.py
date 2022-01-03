class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        last=0
        ret=0
        for row in bank:
            total=sum(map(int,row))
            if total>0:
                ret+=total*last
                last=total
        return ret