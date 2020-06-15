class Solution:
    def freqAlphabets(self, s: str) -> str:
        ret=""
        base=ord("a")-1
        idx=0
        total=len(s)
        while idx<total:
            if idx+2<total and s[idx+2]=="#":
                ret+=chr(base+int(s[idx:(idx+2)]))
                idx+=3
            else:
                ret+=chr(base+int(s[idx]))
                idx+=1  
        return ret