class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cur=0
        count=[0]*26
        base=ord("a")
        for item in s:
            count[ord(item)-base]+=1
            cur=count[ord(item)-base]
        for i in range(26):
            if count[i]>0 and count[i]!=cur:
                return False
        return True