class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2:
            return False
        free=0
        left=0
        for i in range(len(s)):
            if locked[i]=="0":
                free+=1
            elif s[i]=="(":
                left+=1
            else:
                if left>0:
                    left-=1
                elif free>0:
                    free-=1
                else:
                    return False
