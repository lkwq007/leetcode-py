import heapq
import itertools
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        queue=[]
        record={}
        counter=itertools.count()
        nums.sort()
        def add(idx,priority):
            