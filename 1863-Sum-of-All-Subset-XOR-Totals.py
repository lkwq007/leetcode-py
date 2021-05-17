class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ret=0
        def probe(idx,acc):
            if idx==len(nums):
                self.ret+=acc
                return
            probe(idx+1,nums[idx]^acc)
            probe(idx+1,acc)
        probe(0,0)
        return self.ret