class Solution:
    def minSteps(self, s: str, t: str) -> int:
        base=ord("a")
        cnt1=[0]*26
        cnt2=[0]*26
        for item in s:
            cnt1[ord(item)-base]+=1
        for item in t:
            cnt2[ord(item)-base]+=1
        ret=0
        for i in range(26):
            ret+=abs(cnt1[i]-cnt2[i])
        return ret