class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ret=0
        x=target
        while target!=1:
            if target%2==0 and maxDoubles>0:
                maxDoubles-=1
                target=target//2
            elif maxDoubles==0:
                ret+=target-1
                break
            else:
                target-=1
            ret+=1
        return ret
