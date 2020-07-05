class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mapping={}
        rmapping={}
        for idx in range(len(s)):
            if s[idx] in mapping:
                if mapping[s[idx]]!=t[idx]:
                    return False
            else:
                if t[idx] in rmapping:
                    return False
                mapping[s[idx]]=t[idx]
                rmapping[t[idx]]=s[idx]
        return True
