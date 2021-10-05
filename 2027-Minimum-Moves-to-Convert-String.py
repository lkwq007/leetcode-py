class Solution:
    def minimumMoves(self, s: str) -> int:
        i=0
        ret=0
        while i<len(s):
            if s[i]=="X":
                i+=3
                ret+=1
            else:
                i+=1
        return ret