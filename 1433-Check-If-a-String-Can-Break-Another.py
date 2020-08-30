class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1.sort()
        s2.sort()
        greater=0
        less=0
        for a,b in zip(s1,s2):
            if a>=b:
                greater+=1
            if a<=b:
                less+=1
        return greater==len(s1) or less==len(s1)