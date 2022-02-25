import functools
class Solution:
    def minimumTime(self, s: str) -> int:
        # brute force
        # 1<=len(s)<=2*10^5
        ret=len(s)
        min_lst=[len(s)-1]*len(s)
        min_idx=len(s)-1
        cnt=0
        for item in s:
            if item=="1":
                cnt+=1
        # first remove from middle
        right=[0]*(len(s)+1)
        last=len(s)
        lacc=0
        racc=0
        for i in range(len(s)-1,-1,-1):
            right[i]=(cnt-racc)*2+(len(s)-last)
            if right[i]<right[min_idx]:
                min_idx=i
            min_lst[i]=min_idx
            if s[i]=="1":
                last=i
                racc+=1
        last=-1
        for i in range(len(s)):
            idx=min_lst[i]
            ret=min(ret,right[idx]-2*lacc+last+1)
            if s[i]=="1":
                lacc+=1
                last=i
        return ret