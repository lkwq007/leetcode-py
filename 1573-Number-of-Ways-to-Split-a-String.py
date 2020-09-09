class Solution:
    def numWays(self, s: str) -> int:
        cnt=0
        for item in s:
            if item=="1":
                cnt+=1
        if cnt%3!=0:
            return 0
        split0=cnt//3
        split1=2*split0
        