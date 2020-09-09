class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x=0
        for lst in (s1,s2):
            for item in lst:
                if item=="x":
                    x+=1
        if x%2==1:
            return -1
        xy=0
        yx=0
        for a,b in zip(s1,s2):
            if a!=b:
                if a=="x":
                    xy+=1
                else:
                    yx+=1
        ret=0
        if xy%2==1:
            xy+=1
            yx-=1
            ret=1
        return xy//2+yx//2+ret