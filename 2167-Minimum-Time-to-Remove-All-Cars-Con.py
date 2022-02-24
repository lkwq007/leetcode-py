import functools
class Solution:
    def minimumTime(self, s: str) -> int:
        # brute force
        # 1<=len(s)<=2*10^5
        ret=len(s)
        left_lst=[0]*len(s)
        right_lst=[0]*len(s)