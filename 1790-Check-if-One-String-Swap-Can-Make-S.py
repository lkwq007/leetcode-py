class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff=0
        for a,b in zip(s1,s2):
            if a!=b:
                diff+=1
        return sorted(s1)==sorted(s2) and diff<3