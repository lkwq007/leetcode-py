class Solution:
    def longestAwesome(self, s: str) -> int:
        record={}
        acc=0
        ret=0
        for idx in range(len(s)):
            item=s[idx]
            acc^=int(item)
            if acc in record:
                ret=max(ret,idx-record[acc]+1)
            else:
                record[acc]=idx
        if ret<len(s):
            return ret+1
        else:
            return ret