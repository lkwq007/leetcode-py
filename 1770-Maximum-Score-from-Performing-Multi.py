import functools
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        total=len(nums)
        M=len(multipliers)
        @functools.lru_cache(maxsize=None)
        def probe(start,end):
            idx=start+total-end-1
            if idx==M:
                return 0
            val=multipliers[idx]
            return max(val*nums[start]+probe(start+1,end),val*nums[end]+probe(start,end-1))
        ret=probe(0,total-1)
        probe.cache_clear()
        return ret

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        total=len(nums)
        M=len(multipliers)
        record=[{} for i in range(1001)]
        def probe(start,end):
            if end in record[start]:
                return record[start][end]
            idx=start+total-end-1
            if idx==M:
                record[start][end]=0
                return 0
            val=multipliers[idx]
            ret=max(val*nums[start]+probe(start+1,end),val*nums[end]+probe(start,end-1))
            record[start][end]=ret
            return ret
        ret=probe(0,total-1)
        # del record
        return ret
