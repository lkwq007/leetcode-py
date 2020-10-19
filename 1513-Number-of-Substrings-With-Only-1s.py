class Solution:
    def numSub(self, s: str) -> int:
        ret=0
        term=10**9+7
        cnt=0
        for item in s:
            if item=="1":
                cnt+=1
                ret=(ret+cnt)%term
            else:
                cnt=0
        return ret
