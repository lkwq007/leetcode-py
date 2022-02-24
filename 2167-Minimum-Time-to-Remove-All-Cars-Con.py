import functools
class Solution:
    def minimumTime(self, s: str) -> int:
        # brute force
        ret=len(s)
        left_lst=[0]*len(s)
        right_lst=[0]*len(s)