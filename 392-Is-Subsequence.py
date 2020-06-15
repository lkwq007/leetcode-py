class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        total_s=len(s)
        cur=0
        for item in t:
            if cur==total_s:
                return True
            if item==s[cur]:
                cur+=1
        return cur==total_s
