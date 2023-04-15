class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ret=0
        acc=0
        cnt=0
        old_acc=0
        for item in s:
            if item=="0":
                cnt=0
                acc+=1
            else:
                if acc>0:
                    old_acc=acc
                acc=0
                cnt+=1
                cnt=min(old_acc,cnt)
            ret=max(cnt,ret)
        return ret