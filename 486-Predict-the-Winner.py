class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        import functools
        @functools.lru_cache(maxsize=None)
        def probe(start,end):
            if start==end:
                return nums[start]
            return max(nums[start]-probe(start+1,end),nums[end]-probe(start,end-1))
        return probe(0,len(nums)-1)>=0