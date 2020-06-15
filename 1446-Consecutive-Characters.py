class Solution:
    def maxPower(self, s: str) -> int:
        if len(s)<1:
            return 0
        max_val=1
        cnt=1
        for idx in range(1,len(s)):
            if s[idx]==s[idx-1]:
                cnt+=1
                max_val=max(max_val,cnt)
            else:
                cnt=1
        return max_val