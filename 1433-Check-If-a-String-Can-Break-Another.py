class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        greater=0
        less=0
        for a,b in zip(sorted(s1),sorted(s2)):
            if a>=b:
                greater+=1
            if a<=b:
                less+=1
        return greater==len(s1) or less==len(s1)