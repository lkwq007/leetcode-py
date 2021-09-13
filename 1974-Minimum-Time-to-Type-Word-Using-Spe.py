class Solution:
    def minTimeToType(self, word: str) -> int:
        base=ord("a")
        ret=0
        cur=0
        for item in word:
            val=ord(item)-base
            diff=min(abs(val-cur),abs(26+cur-val),abs(26+val-cur))
            cur=val
            ret+=diff+1
        return ret
