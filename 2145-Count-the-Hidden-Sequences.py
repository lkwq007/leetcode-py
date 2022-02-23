from functools import reduce
import itertools


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_val=0
        max_val=0
        acc=0
        for item in differences:
            acc+=item
            min_val=min(acc,min_val)
            max_val=max(acc,max_val)
        diff=max_val-min_val
        return max(0,upper-lower-diff+1)