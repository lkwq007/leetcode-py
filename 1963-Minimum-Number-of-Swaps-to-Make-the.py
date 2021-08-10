class Solution:
    def minSwaps(self, s: str) -> int:
        # two points, swap each illegal pair
        left=0
        right=len(s)-1
        lstack=0
        rstack=0
        ret=0
        flag=False
        while left<right:
            if flag:
                if s[left]=="[":
                    lstack+=1
                else:
                    if lstack>0:
                        lstack-=1
                    else:
                        flag=True
                if not flag:
                    left+=1
            else:
                if s[right]=="]":
                    rstack+=1
                else:
                    if rstack>0:
                        rstack-=1
                    else:
                        flag=False
                        rstack+=1
                        lstack+=1
                        ret+=1
                        left+=1
                right-=1
        return ret