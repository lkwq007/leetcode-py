class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        if len(stones)<3:
            return sum(stones)
        # alice max
        # bob min
        prefix=stones[:]
        acc=0
        for i in range(len(prefix)):
            acc+=prefix[i]
            prefix[i]=acc
        dp=prefix[-1]
        for i in range(len(prefix)-2,-1,-1):
            dp=max(dp,prefix[i]-dp)
        return dp
        