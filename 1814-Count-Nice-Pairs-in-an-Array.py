class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev_func(x):
            return int(str(x)[::-1])
        term=10**9+7
        record={}
        for item in nums:
            rev=rev_func(item)
            diff=item-rev
            record[diff]=record.get(diff,0)+1
        acc=0
        for k,v in record.items():
            acc+=v*(v-1)//2
            acc%=term
        return acc