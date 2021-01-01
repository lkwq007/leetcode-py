class Solution:
    def numSplits(self, s: str) -> int:
        left={}
        right={}
        ret=0
        for item in s:
            right[item]=right.get(item,0)+1
        for i in range(len(s)):
            item=s[i]
            right[item]-=1
            if right[item]==0:
                del right[item]
            left[item]=1
            if len(left)==len(right):
                ret+=1
        return ret