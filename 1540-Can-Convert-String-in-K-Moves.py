class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s)!=len(t):
            return False
        record={}
        base=ord("a")
        for a,b in zip(s,t):
            if a==b:
                continue
            a=ord(a)-base
            b=ord(b)-base
            if b<a:
                b+=26
            diff=b-a
            cur=record.get(diff,diff)
            if cur>k:
                return False
            record[cur]=1
            record[diff]=cur+26
        return True