class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        total=minutesToTest//minutesToDie
        if total<1:
            return 0
        acc=total+1
        term=acc
        cnt=1
        while acc<buckets:
            acc*=term
            cnt+=1
        return cnt