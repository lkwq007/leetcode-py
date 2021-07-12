class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ret=set([])
        base=ord("a")
        left=[0]*26
        right=[0]*26
        for item in s:
            left[ord(item)-base]+=1
        for item in reversed(s):
            idx=ord(item)-base
            left[idx]-=1
            tmp=(idx+1)<<5
            for i in range(26):
                if left[i]>0 and right[i]>0:
                    ret.add(tmp+i+1)
            right[idx]+=1
        return len(ret)