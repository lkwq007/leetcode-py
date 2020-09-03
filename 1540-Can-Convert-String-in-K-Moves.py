class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s)!=len(t):
            return False
        lst=[[a,b] for a,b in zip(s,t) if a!=b]

