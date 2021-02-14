class Solution:
    def minOperations(self, s: str) -> int:
        ret1=0
        ret2=0
        ref1="0"
        ref2="1"
        for item in s:
            if item!=ref1:
                ret1+=1
            else:
                ret2+=1
            ref1,ref2=ref2,ref1
        return min(ret1,ret2)
            