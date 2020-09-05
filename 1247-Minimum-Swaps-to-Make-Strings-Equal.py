class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x=0
        for lst in (s1,s2):
            for item in lst:
                if item=="x":
                    x+=1
        if x%2==1:
            return -1
        
        